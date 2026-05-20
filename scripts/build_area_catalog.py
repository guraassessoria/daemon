from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json
from audit_entity_highlights import quality_flags
from presentation_quality import is_quarantined, presentation_status, CRITICAL_PRESENTATION_FLAGS
from editorial_classifier import classify_source_part, content_kind_for_entity


BOOKS_DATA_DIR = DATA_DIR / "books"
ENTITIES_DIR = DATA_DIR / "entities"
AREAS_DIR = DATA_DIR / "areas"
DOCS_DIR = ROOT / "docs"
WORK_DIR = DATA_DIR / "work"

NEGATIVE_APRIMORAMENTO_COST_RE = re.compile(
    r"(?<![\w+])[-\u2010-\u2015\u2212]\s*[1-9]\d?\s*(?:pontos?|pts?\.?)\b",
    re.IGNORECASE,
)
APRIMORAMENTO_COST_MARKER_RE = re.compile(
    r"(?<!\w)([-\u2010-\u2015\u2212]?)\s*[1-9]\d?\s*(?:pontos?|pts?\.?)\s*:",
    re.IGNORECASE,
)


AREA_LABELS = {
    "regras_base": "Regras Base",
    "aprimoramentos": "Aprimoramentos",
    "kits": "Kits",
    "classes": "Classes",
    "racas": "Racas",
    "linhagens": "Linhagens",
    "poderes": "Poderes",
    "magias": "Magias",
    "rituais": "Rituais",
    "itens_equipamentos": "Itens e Equipamentos",
    "criaturas_npcs": "Criaturas e NPCs",
    "cenarios_lore": "Cenarios e Lore",
    "aventuras": "Aventuras",
    "tabelas": "Tabelas e Geradores",
}


CATEGORY_TO_AREA = {
    "source": "regras_base",
    "core_rule": "regras_base",
    "attribute_skill": "regras_base",
    "combat": "regras_base",
    "character_option": "aprimoramentos",
    "character_class": "classes",
    "kit_class": "kits",
    "race_lineage": "racas",
    "power_magic": "poderes",
    "ritual_spell": "rituais",
    "item_equipment": "itens_equipamentos",
    "creature_npc": "criaturas_npcs",
    "setting_lore": "cenarios_lore",
    "adventure": "aventuras",
    "table_generator": "tabelas",
}


AREA_KEYWORDS = [
    ("regras_base", ("regra", "regras", "sistema", "modulo", "daemon", "atributo", "atributos", "pericia", "pericias", "especializacao", "especializacoes", "combate", "manobra", "manobras", "ataque", "defesa", "dano")),
    ("aprimoramentos", ("aprimoramento", "aprimoramentos", "vantagem", "desvantagem", "talento", "talentos")),
    ("classes", ("classe", "classes", "classe de prestigio", "profissao", "profissoes", "ocupacao", "ocupacoes")),
    ("kits", ("kit", "kits", "arquetipo", "arquetipos")),
    ("racas", ("raca", "racas", "elfo", "elfos", "anao", "anoes", "sprite", "sereia", "orc", "goblin", "ogre")),
    ("linhagens", ("linhagem", "linhagens", "vampiro", "vampiros", "youkai", "youkais", "imortal", "imortais", "fera", "feras")),
    ("rituais", ("ritual", "rituais", "grimorio", "invocacao", "encantamento", "circulo", "circulos")),
    ("poderes", ("poder", "poderes", "superpoder", "superpoderes", "psiquismo", "psionico", "milagre", "reiatsu")),
    ("magias", ("magia", "magias", "caminho", "caminhos", "kidou", "kidous", "focus", "feitico", "feiticos")),
    ("itens_equipamentos", ("item", "itens", "equipamento", "equipamentos", "arma", "armas", "armadura", "veiculo", "veiculos")),
    ("criaturas_npcs", ("criatura", "criaturas", "monstro", "monstros", "npc", "npcs", "demonio", "anjos", "dragao", "dragoes")),
    ("aventuras", ("aventura", "aventuras", "campanha", "campanhas", "cenario pronto", "quick start")),
    ("tabelas", ("tabela", "tabelas", "gerador", "geradores", "aleatorio", "aleatorios")),
]


def normalize_for_search(value: str) -> str:
    return slugify(value).replace("-", " ")


def duplicate_map() -> dict[str, str]:
    report = read_json(INDEX_DIR / "deleted-duplicates-report.json", {})
    return {
        record["duplicate"]: record["canonical"]
        for record in report.get("records", [])
        if record.get("duplicate") and record.get("canonical")
    }


def current_source_lookup() -> dict[str, dict[str, Any]]:
    payload = read_json(INDEX_DIR / "sources.json", {"sources": []})
    return {source["id"]: source for source in payload.get("sources", [])}


def source_classification_lookup() -> dict[str, dict[str, Any]]:
    payload = read_json(INDEX_DIR / "source-classification.json", {"sources": {}})
    sources = payload.get("sources", {}) if isinstance(payload, dict) else {}
    return sources if isinstance(sources, dict) else {}


SOURCE_FAMILY_LABELS = {
    "official_core": "Oficiais / linha principal",
    "rules_system": "Regras e sistema",
    "equipment_items": "Equipamentos, armas e itens",
    "creatures_bestiary": "Criaturas, monstros e NPCs",
    "powers_magic": "Poderes, magia e rituais",
    "races_options": "Raças, kits e opções de personagem",
    "campaign_adventure": "Campanhas e aventuras",
    "setting_lore": "Cenários, lore e organizações",
    "myth_history": "Mitologia, história e religião",
    "adaptation_pop": "Adaptações, anime, supers e cultura pop",
    "supplement_misc": "Suplementos gerais",
}


def infer_source_family(source_id: str, title: str, kind: str) -> dict[str, str]:
    text = normalize_for_search(f"{source_id} {title}")
    if kind == "official":
        return {"id": "official_core", "label": SOURCE_FAMILY_LABELS["official_core"]}
    rules_words = ("sistema", "modulo", "regras", "combate", "pericia", "atributo", "daemon 2", "daemon 3")
    equipment_words = ("arma", "armas", "item", "itens", "equipamento", "veiculo", "veneno")
    creature_words = ("monstro", "monstros", "inimigo", "inimigos", "criatura", "npc", "bestiario", "zoologico")
    power_words = ("grimorio", "magia", "magias", "ritual", "rituais", "poder", "poderes", "psi", "cabalistico", "fe", "vodu")
    option_words = ("raca", "racas", "linhagem", "vantagem", "vantagens", "aprimoramento", "talento", "kit", "classe")
    campaign_words = ("campanha", "aventura", "quick start", "quick-start", "cenario pronto", "segredo", "sussurro")
    lore_words = ("ark", "nun", "trevas", "vaticano", "ordem", "ordens", "seita", "seitas", "umbral", "metropolis")
    myth_words = ("mitologia", "egipcia", "celta", "nordica", "assirio", "babilonica", "viking", "vikings", "templario", "templarios", "revolucao francesa", "mitraismo")
    pop_words = ("anime", "naruto", "dragon ball", "yuyu", "yu yu", "samurai x", "samurai shodown", "mortal kombat", "watchmen", "spawn", "one punch", "tartarugas", "supers", "sda", "tagmar")
    checks = [
        ("adaptation_pop", pop_words),
        ("equipment_items", equipment_words),
        ("creatures_bestiary", creature_words),
        ("powers_magic", power_words),
        ("races_options", option_words),
        ("campaign_adventure", campaign_words),
        ("myth_history", myth_words),
        ("rules_system", rules_words),
        ("setting_lore", lore_words),
    ]
    for family_id, words in checks:
        if any(word in text for word in words):
            return {"id": family_id, "label": SOURCE_FAMILY_LABELS[family_id]}
    return {"id": "supplement_misc", "label": SOURCE_FAMILY_LABELS["supplement_misc"]}


def source_classification_for(source_id: str, classifications: dict[str, dict[str, Any]], title: str | None = None) -> dict[str, Any]:
    default_kind = "supplement"
    data = classifications.get(source_id) or {}
    kind = data.get("kind") or default_kind
    label = data.get("label") or ("Livro oficial" if kind == "official" else "Suplemento de jogo/campanha")
    family = data.get("family") if isinstance(data.get("family"), dict) else None
    if not family:
        family = infer_source_family(source_id, title or data.get("officialName") or source_id, kind)
    return {
        "kind": kind,
        "label": label,
        "officialName": data.get("officialName"),
        "classificationNote": data.get("note"),
        "family": family,
    }


def display_source_title(source_id: str, source_lookup: dict[str, dict[str, Any]], book: dict[str, Any] | None = None) -> str:
    raw = (book or {}).get("title") or source_lookup.get(source_id, {}).get("title") or source_id
    return normalize_uppercase_name(str(raw).replace("_", " "))


def all_entity_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted(ENTITIES_DIR.glob("*.json")):
        payload = read_json(path, [])
        if not isinstance(payload, list):
            continue
        for entity in payload:
            if isinstance(entity, dict) and entity.get("id"):
                ids.add(str(entity["id"]))
    return ids


def valid_entity_refs(refs: list[Any], known_entity_ids: set[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for ref in refs or []:
        ref_id = str(ref)
        if ref_id in known_entity_ids and ref_id not in seen:
            seen.add(ref_id)
            result.append(ref_id)
    return result


def ready_source_ids() -> list[str]:
    sources = current_source_lookup()
    books = {path.stem for path in BOOKS_DATA_DIR.glob("*.json")}
    duplicate_to_canonical = duplicate_map()

    good = read_json(INDEX_DIR / "good-sources-page-coherence.json", {"sources": []})
    usable = read_json(INDEX_DIR / "usable-sources-page-coherence-after-easy-cleanup.json", {"sources": []})

    selected: set[str] = set()
    for source in good.get("sources", []):
        if source.get("status") in {"ok", "notes_only"}:
            selected.add(source["id"])
    for source in usable.get("sources", []):
        if source.get("status") == "ok":
            selected.add(source["id"])

    extra = read_json(INDEX_DIR / "publishable-extra-sources.json", {"sources": []})
    for source in extra.get("sources", []):
        if source.get("publish") and source.get("extractionStatus") != "critical":
            selected.add(source["id"])

    resolved = {duplicate_to_canonical.get(source_id, source_id) for source_id in selected}
    return sorted(source_id for source_id in resolved if source_id in sources and source_id in books)


_LOCK_FILES: dict[str, str] = {
    "aprimoramentos": "aprimoramentos-certified-lock.json",
    "kits": "kits-certified-lock.json",
    "classes": "classes-certified-lock.json",
    "racas": "racas-certified-lock.json",
    "linhagens": "linhagens-certified-lock.json",
    "poderes": "poderes-certified-lock.json",
    "magias": "magias-certified-lock.json",
    "rituais": "rituais-certified-lock.json",
    "regras_base": "regras-base-certified-lock.json",
}


def load_lock(entity_type: str) -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock_file = _LOCK_FILES[entity_type]
    lock = read_json(INDEX_DIR / lock_file, {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


def aprimoramento_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("aprimoramentos")


def kit_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("kits")


def class_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("classes")


def race_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("racas")


def lineage_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("linhagens")


def power_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("poderes")


def magic_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("magias")


def ritual_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("rituais")


def regras_base_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    return load_lock("regras_base")


def is_aprimoramento_claim(entity: dict[str, Any], category: str, name: str) -> bool:
    tags = {normalize_for_search(str(tag)) for tag in entity.get("tags", [])}
    normalized_name = normalize_for_search(name)
    entity_id = str(entity.get("id") or "")
    return (
        entity.get("subtype") == "aprimoramento"
        or entity_id.startswith("aprimoramento-")
        or category == "character_option"
        or "aprimoramento" in tags
        or "aprimoramentos" in tags
        or "fraqueza" in tags
        or "aprimoramento" in normalized_name
    )


def aprimoramento_subgroup(entity: dict[str, Any]) -> tuple[str, str, str]:
    searchable = " ".join(
        str(value)
        for value in [
            entity.get("name", ""),
            entity.get("costText", ""),
            " ".join(str(cost) for cost in entity.get("costs", []) if cost),
            " ".join(str(entry) for entry in entity.get("entries", []) if entry),
        ]
        if value
    )
    first_marker = APRIMORAMENTO_COST_MARKER_RE.search(searchable)
    if first_marker:
        marker_sign = first_marker.group(1)
        if marker_sign:
            return "aprimoramentos_negativos", "Aprimoramentos Negativos", "aprimoramento-negativo"
        return "aprimoramentos_positivos", "Aprimoramentos Positivos", "aprimoramento-positivo"
    if NEGATIVE_APRIMORAMENTO_COST_RE.search(searchable):
        return "aprimoramentos_negativos", "Aprimoramentos Negativos", "aprimoramento-negativo"
    return "aprimoramentos_positivos", "Aprimoramentos Positivos", "aprimoramento-positivo"


def is_kit_claim(entity: dict[str, Any], category: str, name: str) -> bool:
    tags = {normalize_for_search(str(tag)) for tag in entity.get("tags", [])}
    normalized_name = normalize_for_search(name)
    entity_id = str(entity.get("id") or "")
    return (
        entity.get("subtype") == "kit"
        or entity_id.startswith("kit-")
        or category == "kit_class"
        or "kit" in tags
        or "kits" in tags
        or "kit" in normalized_name
    )


def is_class_claim(entity: dict[str, Any], category: str, name: str) -> bool:
    tags = {normalize_for_search(str(tag)) for tag in entity.get("tags", [])}
    normalized_name = normalize_for_search(name)
    entity_id = str(entity.get("id") or "")
    return (
        entity.get("subtype") == "class"
        or entity_id.startswith("classe-")
        or category == "character_class"
        or "class" in tags
        or "classe" in tags
        or "classes" in tags
        or "classe" in normalized_name
    )


def is_race_claim(entity: dict[str, Any], category: str, name: str) -> bool:
    tags = {normalize_for_search(str(tag)) for tag in entity.get("tags", [])}
    normalized_name = normalize_for_search(name)
    name_terms = set(normalized_name.split())
    entity_id = str(entity.get("id") or "")
    return (
        entity.get("subtype") in {"raca", "race"}
        or entity_id.startswith("raca-")
        or category == "race_lineage"
        or "raca" in tags
        or "racas" in tags
        or "raca" in name_terms
        or "racas" in name_terms
    )


def is_lineage_claim(entity: dict[str, Any], category: str, name: str) -> bool:
    tags = {normalize_for_search(str(tag)) for tag in entity.get("tags", [])}
    normalized_name = normalize_for_search(name)
    name_terms = set(normalized_name.split())
    return (
        entity.get("subtype") in {"linhagem", "lineage"}
        or "linhagem" in tags
        or "linhagens" in tags
        or "linhagem" in name_terms
        or "linhagens" in name_terms
    )


def is_power_claim(entity: dict[str, Any], category: str, name: str) -> bool:
    tags = {normalize_for_search(str(tag)) for tag in entity.get("tags", [])}
    normalized_name = normalize_for_search(name)
    name_terms = set(normalized_name.split())
    entity_id = str(entity.get("id") or "")
    return (
        entity.get("subtype") == "poder"
        or entity_id.startswith("poder-")
        or "poder" in tags
        or "poderes" in tags
        or "superpoder" in tags
        or "superpoderes" in tags
        or "poder" in name_terms
        or "poderes" in name_terms
        or (category == "power_magic" and "magia" not in tags and "magias" not in tags)
    )


def is_magic_claim(entity: dict[str, Any], category: str, name: str) -> bool:
    tags = {normalize_for_search(str(tag)) for tag in entity.get("tags", [])}
    normalized_name = normalize_for_search(name)
    name_terms = set(normalized_name.split())
    entity_id = str(entity.get("id") or "")
    return (
        entity.get("subtype") == "magia"
        or entity_id.startswith("magia-")
        or "magia" in tags
        or "magias" in tags
        or "caminho" in tags
        or "caminhos" in tags
        or "magia" in name_terms
        or "magias" in name_terms
        or (category == "power_magic" and ("magia" in tags or "magias" in tags))
    )


def is_regras_base_claim(entity: dict[str, Any], category: str, name: str) -> bool:
    if category not in {"core_rule", "attribute_skill", "combat"}:
        return False
    tags = {normalize_for_search(str(tag)) for tag in entity.get("tags", [])}
    entity_id = str(entity.get("id") or "")
    return (
        entity_id.startswith(("regra-", "core-rule-", "combat-", "pericia-", "atributo-"))
        or bool(tags & {"regra", "regras", "regras basicas", "sistema", "atributo", "atributos", "pericia", "pericias", "combate"})
        or normalize_for_search(name) in {"regra", "regras", "sistema", "atributos", "pericias", "combate"}
    )


_CONFIDENCE_EXPLICIT = 0.84
_CONFIDENCE_SPECIFIC_AREA_BASE = 0.76
_CONFIDENCE_SPECIFIC_AREA_MAX = 0.92
_CONFIDENCE_SPECIFIC_AREA_STEP = 0.04
_CONFIDENCE_GENERIC_BASE = 0.72
_CONFIDENCE_GENERIC_MAX = 0.88
_CONFIDENCE_CATEGORY_MATCH = 0.78
_CONFIDENCE_FALLBACK = 0.64

_HIGH_CONFIDENCE_AREAS = {"aprimoramentos", "classes", "kits", "racas", "linhagens", "poderes", "magias"}


def infer_area(category: str, name: str, summary: str, source_title: str) -> tuple[str, float, list[str]]:
    explicit_area = CATEGORY_TO_AREA.get(category)
    if explicit_area and category != "source":
        return explicit_area, _CONFIDENCE_EXPLICIT, [explicit_area]

    haystack = normalize_for_search(" ".join([name, summary, source_title]))
    matches: list[str] = []
    for area, keywords in AREA_KEYWORDS:
        normalized_keywords = [normalize_for_search(keyword) for keyword in keywords]
        hit_count = sum(1 for keyword in normalized_keywords if keyword in haystack)
        if hit_count:
            matches.append(area)
            if area in _HIGH_CONFIDENCE_AREAS:
                return area, min(_CONFIDENCE_SPECIFIC_AREA_MAX, _CONFIDENCE_SPECIFIC_AREA_BASE + hit_count * _CONFIDENCE_SPECIFIC_AREA_STEP), matches
            if area != CATEGORY_TO_AREA.get(category):
                return area, min(_CONFIDENCE_GENERIC_MAX, _CONFIDENCE_GENERIC_BASE + hit_count * _CONFIDENCE_SPECIFIC_AREA_STEP), matches

    area = CATEGORY_TO_AREA.get(category, "fontes")
    confidence = _CONFIDENCE_CATEGORY_MATCH if area != "fontes" else _CONFIDENCE_FALLBACK
    return area, confidence, matches


def catalog_sort_key(item: dict[str, Any]) -> tuple[str, str, int, str]:
    return (
        slugify(str(item.get("name") or "")),
        slugify(str(item.get("sourceTitle") or item.get("source") or "")),
        int(item.get("page") or 0),
        str(item.get("id") or ""),
    )


TITLE_LOWERCASE_WORDS = {"a", "as", "ao", "aos", "com", "da", "das", "de", "do", "dos", "e", "em", "na", "nas", "no", "nos", "para", "por"}
TEXT_ACRONYMS = {
    "agi": "AGI",
    "car": "CAR",
    "con": "CON",
    "dex": "DEX",
    "fbi": "FBI",
    "fr": "FR",
    "int": "INT",
    "ip": "IP",
    "npc": "NPC",
    "npcs": "NPCs",
    "per": "PER",
    "pm": "PM",
    "pms": "PMs",
    "pv": "PV",
    "pvs": "PVs",
    "will": "WILL",
}


def uppercase_ratio(value: str) -> float:
    letters = [char for char in value if char.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for char in letters if char.isupper()) / len(letters)


def is_mostly_uppercase(value: str, minimum_letters: int = 8, threshold: float = 0.78) -> bool:
    letters = [char for char in value if char.isalpha()]
    return len(letters) >= minimum_letters and uppercase_ratio(value) >= threshold


def normalize_uppercase_name(value: str) -> str:
    if not is_mostly_uppercase(value, minimum_letters=4):
        return value
    words = value.lower().split()
    normalized: list[str] = []
    for index, word in enumerate(words):
        if index > 0 and word in TITLE_LOWERCASE_WORDS:
            normalized.append(word)
        else:
            normalized.append(word[:1].upper() + word[1:])
    return " ".join(normalized)


def normalize_uppercase_text(value: str) -> str:
    if not is_mostly_uppercase(value, minimum_letters=20):
        return value
    text = value.lower()
    for source, replacement in TEXT_ACRONYMS.items():
        text = re.sub(rf"\b{re.escape(source)}\b", replacement, text, flags=re.IGNORECASE)

    def capitalize_match(match: re.Match[str]) -> str:
        return f"{match.group(1)}{match.group(2).upper()}"

    return re.sub(r"(^|[.!?]\s+)([a-zà-ÿ])", capitalize_match, text)


def normalize_display_entries(entries: list[Any]) -> list[Any]:
    return [normalize_uppercase_text(entry) if isinstance(entry, str) else entry for entry in entries]


def area_for_entity(entity: dict[str, Any], category: str, name: str, summary: str, source_title: str) -> tuple[str, float, list[str]]:
    subtype = entity.get("subtype")
    if subtype == "aprimoramento":
        return "aprimoramentos", 0.9, ["aprimoramentos"]
    if subtype in {"kit", "class"}:
        return "kits" if subtype == "kit" else "classes", 0.9, [subtype]
    if subtype in {"raca", "race"}:
        return "racas", 0.9, ["racas"]
    if subtype in {"linhagem", "lineage"}:
        return "linhagens", 0.9, ["linhagens"]
    if subtype == "poder":
        return "poderes", 0.9, ["poderes"]
    if subtype == "magia":
        return "magias", 0.9, ["magias"]
    area, confidence, matches = infer_area(category, name, summary, source_title)
    if area in {"classes", "kits"} and category != "kit_class":
        return CATEGORY_TO_AREA.get(category, "fontes"), 0.78, matches
    if area == "racas" and category != "race_lineage":
        return CATEGORY_TO_AREA.get(category, "fontes"), 0.78, matches
    if area == "linhagens" and category != "race_lineage":
        return CATEGORY_TO_AREA.get(category, "fontes"), 0.78, matches
    if area in {"poderes", "magias"} and category != "power_magic":
        return CATEGORY_TO_AREA.get(category, "fontes"), 0.78, matches
    return area, confidence, matches


def page_value(part: dict[str, Any]) -> int | None:
    pages = part.get("pages") or []
    if pages and isinstance(pages[0], int):
        return pages[0]
    page = part.get("page")
    return page if isinstance(page, int) else None


def build_source_part_items(
    source_ids: list[str],
    source_lookup: dict[str, dict[str, Any]],
    known_entity_ids: set[str],
    classifications: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for source_id in source_ids:
        book = read_json(BOOKS_DATA_DIR / f"{source_id}.json", {})
        source_title = display_source_title(source_id, source_lookup, book)
        for part in book.get("parts", []):
            name = part.get("name") or part.get("id") or source_title
            category = part.get("category") or "source"
            summary = part.get("summary") or ""
            area, confidence, matched_areas = infer_area(category, name, summary, source_title)
            classification = source_classification_for(source_id, classifications, source_title)
            item = {
                "id": f"{source_id}--{slugify(part.get('id') or name)}",
                "name": name,
                "area": area,
                "category": category,
                "source": source_id,
                "sourceTitle": source_title,
                "pages": part.get("pages", []),
                "page": page_value(part),
                "summary": summary,
                "entityRefs": valid_entity_refs(part.get("entityRefs", []), known_entity_ids),
                "tags": sorted(set([area, category, *matched_areas])),
                "confidence": round(confidence, 2),
                "extractionMethod": "book-part-area-pass-1",
                "sourceKind": classification["kind"],
                "sourceKindLabel": classification["label"],
                "officialSource": classification["kind"] == "official",
                "sourceFamily": classification["family"]["id"],
                "sourceFamilyLabel": classification["family"]["label"],
            }
            item.update(classify_source_part(item, source_title))
            items.append(item)
    return items


def build_entity_items(
    source_ids: set[str],
    source_lookup: dict[str, dict[str, Any]],
    classifications: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    lock_by_id, lock_by_source_name = aprimoramento_locks()
    kit_lock_by_id, kit_lock_by_source_name = kit_locks()
    class_lock_by_id, class_lock_by_source_name = class_locks()
    race_lock_by_id, race_lock_by_source_name = race_locks()
    lineage_lock_by_id, lineage_lock_by_source_name = lineage_locks()
    power_lock_by_id, power_lock_by_source_name = power_locks()
    magic_lock_by_id, magic_lock_by_source_name = magic_locks()
    ritual_lock_by_id, ritual_lock_by_source_name = ritual_locks()
    rules_lock_by_id, rules_lock_by_source_name = regras_base_locks()
    quarantined_aprimoramentos: list[dict[str, Any]] = []
    duplicate_aprimoramentos: list[dict[str, Any]] = []
    quarantined_kits: list[dict[str, Any]] = []
    duplicate_kits: list[dict[str, Any]] = []
    quarantined_classes: list[dict[str, Any]] = []
    duplicate_classes: list[dict[str, Any]] = []
    quarantined_races: list[dict[str, Any]] = []
    duplicate_races: list[dict[str, Any]] = []
    quarantined_lineages: list[dict[str, Any]] = []
    duplicate_lineages: list[dict[str, Any]] = []
    quarantined_powers: list[dict[str, Any]] = []
    duplicate_powers: list[dict[str, Any]] = []
    quarantined_magics: list[dict[str, Any]] = []
    duplicate_magics: list[dict[str, Any]] = []
    duplicate_rituals: list[dict[str, Any]] = []
    quarantined_rules: list[dict[str, Any]] = []
    duplicate_rules: list[dict[str, Any]] = []
    for path in sorted(ENTITIES_DIR.glob("*.json")):
        if path.name == "source.json":
            continue
        category_entities = read_json(path, [])
        if not isinstance(category_entities, list):
            continue
        for entity in category_entities:
            source_id = entity.get("source")
            if source_id not in source_ids:
                continue
            category = entity.get("category") or CATEGORY_TO_AREA.get(path.stem, "source")
            name = entity.get("name", entity.get("id", ""))
            entity_id = entity.get("id")
            source_name_key = (source_id, slugify(str(name)))
            is_certified_aprimoramento = entity_id in lock_by_id
            is_certified_kit = entity_id in kit_lock_by_id
            is_certified_class = entity_id in class_lock_by_id
            is_certified_race = entity_id in race_lock_by_id
            is_certified_lineage = entity_id in lineage_lock_by_id
            is_certified_power = entity_id in power_lock_by_id
            is_certified_magic = entity_id in magic_lock_by_id
            is_certified_ritual = entity_id in ritual_lock_by_id
            is_certified_rule = entity_id in rules_lock_by_id
            is_structured_docx = entity.get("extractionMethod") == "docx-structured-import-v1"
            if source_name_key in lock_by_source_name and not is_certified_aprimoramento:
                duplicate_aprimoramentos.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if source_name_key in kit_lock_by_source_name and not is_certified_kit:
                duplicate_kits.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": kit_lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if source_name_key in class_lock_by_source_name and not is_certified_class:
                duplicate_classes.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": class_lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if source_name_key in race_lock_by_source_name and not is_certified_race:
                duplicate_races.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": race_lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if source_name_key in lineage_lock_by_source_name and not is_certified_lineage:
                duplicate_lineages.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": lineage_lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if source_name_key in power_lock_by_source_name and not is_certified_power:
                duplicate_powers.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": power_lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if source_name_key in magic_lock_by_source_name and not is_certified_magic:
                duplicate_magics.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": magic_lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if source_name_key in ritual_lock_by_source_name and not is_certified_ritual:
                duplicate_rituals.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": ritual_lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if source_name_key in rules_lock_by_source_name and not is_certified_rule:
                duplicate_rules.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "duplicateOf": rules_lock_by_source_name[source_name_key]["id"],
                    }
                )
                continue
            if not is_structured_docx and is_aprimoramento_claim(entity, category, str(name)) and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_power and not is_certified_magic and not is_certified_ritual and not is_certified_rule:
                quarantined_aprimoramentos.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "reason": "uncertified_aprimoramento_claim",
                    }
                )
                continue
            if not is_structured_docx and is_kit_claim(entity, category, str(name)) and not is_certified_kit and not is_certified_aprimoramento and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_power and not is_certified_magic and not is_certified_ritual and not is_certified_rule:
                quarantined_kits.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "reason": "uncertified_kit_claim",
                    }
                )
                continue
            if not is_structured_docx and is_class_claim(entity, category, str(name)) and not is_certified_class and not is_certified_aprimoramento and not is_certified_kit and not is_certified_race and not is_certified_lineage and not is_certified_power and not is_certified_magic and not is_certified_ritual and not is_certified_rule:
                quarantined_classes.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "reason": "uncertified_class_claim",
                    }
                )
                continue
            if not is_structured_docx and is_lineage_claim(entity, category, str(name)) and not is_certified_lineage and not is_certified_race and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_power and not is_certified_magic and not is_certified_ritual and not is_certified_rule:
                quarantined_lineages.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "reason": "uncertified_lineage_claim",
                    }
                )
                continue
            if not is_structured_docx and is_race_claim(entity, category, str(name)) and not is_certified_race and not is_certified_lineage and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_power and not is_certified_magic and not is_certified_ritual and not is_certified_rule:
                quarantined_races.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "reason": "uncertified_race_claim",
                    }
                )
                continue
            if not is_structured_docx and is_power_claim(entity, category, str(name)) and not is_certified_power and not is_certified_magic and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_ritual and not is_certified_rule:
                quarantined_powers.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "reason": "uncertified_power_claim",
                    }
                )
                continue
            if not is_structured_docx and is_magic_claim(entity, category, str(name)) and not is_certified_magic and not is_certified_power and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_ritual and not is_certified_rule:
                quarantined_magics.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "reason": "uncertified_magic_claim",
                    }
                )
                continue
            if not is_structured_docx and is_regras_base_claim(entity, category, str(name)) and not is_certified_rule and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_power and not is_certified_magic and not is_certified_ritual:
                quarantined_rules.append(
                    {
                        "id": entity_id,
                        "name": name,
                        "source": source_id,
                        "category": category,
                        "subtype": entity.get("subtype"),
                        "entityFile": path.name,
                        "reason": "uncertified_regras_base_claim",
                    }
                )
                continue
            if is_certified_aprimoramento:
                category = "character_option"
            if is_certified_kit:
                category = "kit_class"
            if is_certified_class:
                category = "character_class"
            if is_certified_race:
                category = "race_lineage"
            if is_certified_lineage:
                category = "race_lineage"
            if is_certified_power:
                category = "power_magic"
            if is_certified_magic:
                category = "power_magic"
            if is_certified_ritual:
                category = "ritual_spell"
            if is_certified_rule:
                category = entity.get("category") if entity.get("category") in {"core_rule", "attribute_skill", "combat"} else "core_rule"
            entries = entity.get("entries") or []
            display_name = normalize_uppercase_name(str(name))
            display_entries = normalize_display_entries(entries)
            summary = " ".join(entry for entry in entries if isinstance(entry, str))
            source_title = display_source_title(source_id, source_lookup)
            classification = source_classification_for(source_id, classifications, source_title)
            if is_certified_aprimoramento:
                area, confidence, matched_areas = "aprimoramentos", 1.0, ["aprimoramentos", "certificado"]
            elif is_certified_kit:
                area, confidence, matched_areas = "kits", 1.0, ["kits", "certificado"]
            elif is_certified_class:
                area, confidence, matched_areas = "classes", 1.0, ["classes", "certificado"]
            elif is_certified_race:
                area, confidence, matched_areas = "racas", 1.0, ["racas", "certificado"]
            elif is_certified_lineage:
                area, confidence, matched_areas = "linhagens", 1.0, ["linhagens", "certificado"]
            elif is_certified_power:
                area, confidence, matched_areas = "poderes", 1.0, ["poderes", "certificado"]
            elif is_certified_magic:
                area, confidence, matched_areas = "magias", 1.0, ["magias", "certificado"]
            elif is_certified_ritual:
                area, confidence, matched_areas = "rituais", 1.0, ["rituais", "certificado"]
            elif is_certified_rule:
                area, confidence, matched_areas = "regras_base", 1.0, ["regras_base", "certificado"]
            else:
                area, confidence, matched_areas = area_for_entity(
                    entity,
                    category,
                    str(name),
                    summary,
                    source_title,
                )
            # Entidades criadas por importação DOCX já vêm com uma área editorial
            # deliberada (ex.: tabelas, combate, magias). A etapa automática não
            # deve reclassificá-las apenas porque uma tabela cita "aprimoramento"
            # ou outro termo secundário.
            if entity.get("extractionMethod") == "docx-structured-import-v1" and entity.get("area") in AREA_LABELS:
                area = str(entity["area"])
                confidence = max(confidence, float(entity.get("confidence", confidence)))
            subgroup: str | None = None
            subgroup_label: str | None = None
            subgroup_tag: str | None = None
            if area == "aprimoramentos":
                subgroup, subgroup_label, subgroup_tag = aprimoramento_subgroup(entity)
                matched_areas = [*matched_areas, subgroup_tag]
            item = {
                "id": entity_id,
                "name": display_name,
                "area": area,
                "category": category,
                "source": source_id,
                "sourceTitle": source_title,
                "page": entity.get("page"),
                "entries": display_entries,
                "tags": sorted(set([area, category, *entity.get("tags", []), *matched_areas])),
                "confidence": round(float(entity.get("confidence", confidence)), 2),
                "extractionMethod": entity.get("extractionMethod", "entity-area-pass-1"),
                "sourceKind": classification["kind"],
                "sourceKindLabel": classification["label"],
                "officialSource": classification["kind"] == "official",
                "sourceFamily": classification["family"]["id"],
                "sourceFamilyLabel": classification["family"]["label"],
            }
            if subgroup and subgroup_label:
                item["subgroup"] = subgroup
                item["subgroupLabel"] = subgroup_label
            item.update(content_kind_for_entity(item))
            for optional_field in [
                "subtype",
                "pages",
                "costs",
                "costText",
                "aprimoramentoCost",
                "periciaCost",
                "skillsText",
                "aprimoramentosText",
                "requirements",
                "primaryAttributes",
                "requiredSkillsText",
                "suggestedSkillsText",
                "classKind",
                "certificationStatus",
                "certifiedAs",
                "certifiedArea",
                "lockedArea",
                "certificationId",
                "certificationMethod",
                "kitContext",
                "classContext",
                "raceContext",
                "powerMagicContext",
                "ritualContext",
                "initialAgeText",
                "attributesText",
                "advantagesText",
                "disadvantagesText",
                "weaknessesText",
                "tables",
            ]:
                if optional_field in entity:
                    item[optional_field] = entity[optional_field]
            items.append(item)
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    write_json(WORK_DIR / "aprimoramentos-quarantine.json", quarantined_aprimoramentos)
    write_json(WORK_DIR / "aprimoramentos-duplicate-blocks.json", duplicate_aprimoramentos)
    write_json(WORK_DIR / "kits-quarantine.json", quarantined_kits)
    write_json(WORK_DIR / "kits-duplicate-blocks.json", duplicate_kits)
    write_json(WORK_DIR / "classes-quarantine.json", quarantined_classes)
    write_json(WORK_DIR / "classes-duplicate-blocks.json", duplicate_classes)
    write_json(WORK_DIR / "racas-quarantine.json", quarantined_races)
    write_json(WORK_DIR / "racas-duplicate-blocks.json", duplicate_races)
    write_json(WORK_DIR / "linhagens-quarantine.json", quarantined_lineages)
    write_json(WORK_DIR / "linhagens-duplicate-blocks.json", duplicate_lineages)
    write_json(WORK_DIR / "poderes-quarantine.json", quarantined_powers)
    write_json(WORK_DIR / "poderes-duplicate-blocks.json", duplicate_powers)
    write_json(WORK_DIR / "magias-quarantine.json", quarantined_magics)
    write_json(WORK_DIR / "magias-duplicate-blocks.json", duplicate_magics)
    write_json(WORK_DIR / "rituais-duplicate-blocks.json", duplicate_rituals)
    write_json(WORK_DIR / "regras-base-quarantine.json", quarantined_rules)
    write_json(WORK_DIR / "regras-base-duplicate-blocks.json", duplicate_rules)
    return items


def build_source_entities(source_ids: list[str], source_lookup: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    classifications = source_classification_lookup()
    source_entities_payload = read_json(ENTITIES_DIR / "source.json", [])
    source_entities_by_source = {
        str(entity.get("source")): entity
        for entity in source_entities_payload
        if isinstance(entity, dict) and entity.get("source")
    }
    items: list[dict[str, Any]] = []
    for source_id in source_ids:
        book = read_json(BOOKS_DATA_DIR / f"{source_id}.json", {})
        source_title = display_source_title(source_id, source_lookup, book)
        source_entity = source_entities_by_source.get(source_id, {})
        classification = source_classification_for(source_id, classifications, source_title)
        entries = source_entity.get("entries") or [
            f"Fonte processada para consulta digital: {source_title}.",
        ]
        tags = set(source_entity.get("tags", []))
        tags.update(["fontes", "source", classification["kind"]])
        item = {
            "id": f"source-{source_id}",
            "name": source_title,
            "area": "fontes",
            "category": "source",
            "source": source_id,
            "sourceTitle": source_title,
            "page": source_entity.get("page") or 1,
            "entries": normalize_display_entries(entries),
            "tags": sorted(tags),
            "confidence": round(float(source_entity.get("confidence", 1 if classification["kind"] == "official" else 0.8)), 2),
            "extractionMethod": "source-catalog-pass-1",
            "sourceKind": classification["kind"],
            "sourceKindLabel": classification["label"],
            "officialSource": classification["kind"] == "official",
            "sourceFamily": classification["family"]["id"],
            "sourceFamilyLabel": classification["family"]["label"],
        }
        if classification.get("officialName"):
            item["officialName"] = classification["officialName"]
        if classification.get("classificationNote"):
            item["classificationNote"] = classification["classificationNote"]
        item.update(content_kind_for_entity(item))
        items.append(item)
    return items



def enrich_display_quality(item: dict[str, Any], item_type: str) -> dict[str, Any]:
    if item_type == "entity" and (item.get("area") == "fontes" or item.get("category") == "source"):
        item.setdefault("qualityStatus", "ok")
        item.setdefault("qualityFlags", [])
        item.setdefault("qualitySeverity", "ok")
        item.setdefault("presentationStatus", "public")
        return item
    flags = quality_flags({**item, "itemType": item_type})
    flags = sorted(set([*flags, *item.get("editorialFlags", [])]))
    item["qualityFlags"] = flags
    item["qualitySeverity"] = "critical" if set(flags) & CRITICAL_PRESENTATION_FLAGS else ("warning" if flags else "ok")
    status_hint = item.get("presentationStatusHint")
    if item_type == "sourcePart" and flags:
        item["presentationStatus"] = "quarantine"
    else:
        item["presentationStatus"] = "quarantine" if status_hint == "quarantine" else presentation_status({**item, "itemType": item_type}, flags)
    item["qualityStatus"] = "quarentena" if item["presentationStatus"] == "quarantine" else ("revisar" if flags else "ok")
    return item


def facet_records(items: list[dict[str, Any]]) -> dict[str, Any]:
    sources: dict[str, dict[str, Any]] = {}
    categories: dict[str, int] = {}
    subtypes: dict[str, int] = {}
    source_kinds: dict[str, dict[str, Any]] = {}
    source_families: dict[str, dict[str, Any]] = {}
    areas: dict[str, int] = {}
    for item in items:
        source_id = str(item.get("source") or "")
        if source_id:
            source = sources.setdefault(
                source_id,
                {
                    "id": source_id,
                    "title": item.get("sourceTitle") or source_id,
                    "sourceKind": item.get("sourceKind") or "supplement",
                    "sourceKindLabel": item.get("sourceKindLabel") or "Suplemento de jogo/campanha",
                    "officialSource": bool(item.get("officialSource")),
                    "sourceFamily": item.get("sourceFamily") or "supplement_misc",
                    "sourceFamilyLabel": item.get("sourceFamilyLabel") or SOURCE_FAMILY_LABELS["supplement_misc"],
                    "count": 0,
                },
            )
            source["count"] += 1
        category = item.get("category")
        if category:
            categories[str(category)] = categories.get(str(category), 0) + 1
        subtype = item.get("contentKind") or item.get("subtype") or item.get("itemType")
        if subtype:
            subtypes[str(subtype)] = subtypes.get(str(subtype), 0) + 1
        kind = item.get("sourceKind") or "supplement"
        kind_record = source_kinds.setdefault(
            str(kind),
            {
                "id": str(kind),
                "label": item.get("sourceKindLabel") or ("Livro oficial" if kind == "official" else "Suplemento de jogo/campanha"),
                "count": 0,
            },
        )
        kind_record["count"] += 1
        family = item.get("sourceFamily") or "supplement_misc"
        family_record = source_families.setdefault(
            str(family),
            {
                "id": str(family),
                "label": item.get("sourceFamilyLabel") or SOURCE_FAMILY_LABELS.get(str(family), str(family)),
                "count": 0,
            },
        )
        family_record["count"] += 1
        area = item.get("area")
        if area:
            areas[str(area)] = areas.get(str(area), 0) + 1
    return {
        "sources": sorted(sources.values(), key=lambda row: (not row.get("officialSource"), slugify(str(row.get("title") or "")))),
        "categories": [{"id": key, "count": value} for key, value in sorted(categories.items())],
        "subtypes": [{"id": key, "count": value} for key, value in sorted(subtypes.items())],
        "sourceKinds": sorted(source_kinds.values(), key=lambda row: row["id"]),
        "sourceFamilies": sorted(source_families.values(), key=lambda row: row["label"]),
        "areas": [{"id": key, "count": value} for key, value in sorted(areas.items())],
    }

def write_area_files(source_ids: list[str], part_items: list[dict[str, Any]], entity_items: list[dict[str, Any]]) -> dict[str, Any]:
    AREAS_DIR.mkdir(parents=True, exist_ok=True)
    expected_area_files = {f"{area}.json" for area in AREA_LABELS}
    for stale_path in AREAS_DIR.glob("*.json"):
        if stale_path.name not in expected_area_files:
            stale_path.unlink()
    by_area: dict[str, dict[str, list[dict[str, Any]]]] = {
        area: {"entities": [], "sourceParts": []} for area in AREA_LABELS
    }
    for item in part_items:
        if item["area"] in {"regras_base", "aprimoramentos", "kits", "classes", "racas", "linhagens", "poderes", "magias", "rituais"}:
            continue
        by_area.setdefault(item["area"], {"entities": [], "sourceParts": []})["sourceParts"].append(enrich_display_quality(item, "sourcePart"))
    for item in entity_items:
        by_area.setdefault(item["area"], {"entities": [], "sourceParts": []})["entities"].append(enrich_display_quality(item, "entity"))

    area_summaries: list[dict[str, Any]] = []
    for area in AREA_LABELS:
        subgroup_counts: dict[str, dict[str, Any]] = {}
        for item in by_area[area]["entities"]:
            subgroup = item.get("subgroup")
            if not subgroup:
                continue
            current = subgroup_counts.setdefault(
                subgroup,
                {"id": subgroup, "name": item.get("subgroupLabel", subgroup), "entityCount": 0},
            )
            current["entityCount"] += 1
        all_area_items = [*by_area[area]["entities"], *by_area[area]["sourceParts"]]
        payload = {
            "version": 1,
            "id": area,
            "name": AREA_LABELS[area],
            "readySourceCount": len(source_ids),
            "entityCount": len(by_area[area]["entities"]),
            "sourcePartCount": len(by_area[area]["sourceParts"]),
            "subgroups": sorted(subgroup_counts.values(), key=lambda item: item["name"]),
            "filters": facet_records(all_area_items),
            "entities": sorted(by_area[area]["entities"], key=catalog_sort_key),
            "sourceParts": sorted(by_area[area]["sourceParts"], key=lambda item: (item.get("sourceTitle") or "", item.get("page") or 0, item.get("name") or "")),
        }
        write_json(AREAS_DIR / f"{area}.json", payload)
        area_summaries.append(
            {
                "id": area,
                "name": AREA_LABELS[area],
                "entityCount": payload["entityCount"],
                "sourcePartCount": payload["sourcePartCount"],
            }
        )

    summary = {
        "version": 1,
        "readySourceCount": len(source_ids),
        "areaCount": len(AREA_LABELS),
        "entityCount": len(entity_items),
        "sourcePartCount": len(part_items),
        "areas": area_summaries,
        "readySources": source_ids,
        "filters": facet_records([*entity_items, *part_items]),
    }
    write_json(INDEX_DIR / "area-summary.json", summary)
    return summary


def write_report(summary: dict[str, Any]) -> None:
    lines = [
        "# Area catalog pass 001",
        "",
        "Initial navigation/population layer for the sources marked as ready to proceed.",
        "",
        f"- Ready sources: {summary['readySourceCount']}",
        f"- Areas: {summary['areaCount']}",
        f"- Curated entities included: {summary['entityCount']}",
        f"- Book parts indexed: {summary['sourcePartCount']}",
        "",
        "## Areas",
        "",
        "| Area | Entities | Source parts |",
        "| --- | ---: | ---: |",
    ]
    for area in summary["areas"]:
        lines.append(f"| {area['name']} (`{area['id']}`) | {area['entityCount']} | {area['sourcePartCount']} |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This is a pass-1 catalog based on existing book parts plus curated entities already extracted.",
            "- Duplicate IDs are resolved to their canonical source before the ready-source list is built.",
            "- The next pass should keep splitting high-value source parts into individual mechanical records, including pericias and remaining uncategorized rules.",
            "",
        ]
    )
    report_dir = DOCS_DIR / "reports" / "catalog"
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "area-catalog-pass-001.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    source_lookup = current_source_lookup()
    source_ids = ready_source_ids()
    known_entity_ids = all_entity_ids()
    classifications = source_classification_lookup()
    part_items = build_source_part_items(source_ids, source_lookup, known_entity_ids, classifications)
    entity_items = build_entity_items(set(source_ids), source_lookup, classifications)
    summary = write_area_files(source_ids, part_items, entity_items)
    write_report(summary)
    print(
        f"Area catalog built: {summary['readySourceCount']} sources, "
        f"{summary['sourcePartCount']} source parts, {summary['entityCount']} entities."
    )


if __name__ == "__main__":
    main()
