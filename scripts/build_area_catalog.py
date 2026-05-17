from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


BOOKS_DATA_DIR = DATA_DIR / "books"
ENTITIES_DIR = DATA_DIR / "entities"
AREAS_DIR = DATA_DIR / "areas"
DOCS_DIR = ROOT / "docs"
WORK_DIR = DATA_DIR / "work"


AREA_LABELS = {
    "fontes": "Fontes",
    "regras_base": "Regras Base",
    "atributos_pericias": "Atributos e Pericias",
    "combate": "Combate",
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
    "source": "fontes",
    "core_rule": "regras_base",
    "attribute_skill": "atributos_pericias",
    "combat": "combate",
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
    ("aprimoramentos", ("aprimoramento", "aprimoramentos", "vantagem", "desvantagem", "talento", "talentos")),
    ("classes", ("classe", "classes", "classe de prestigio", "profissao", "profissoes", "ocupacao", "ocupacoes")),
    ("kits", ("kit", "kits", "arquetipo", "arquetipos")),
    ("racas", ("raca", "racas", "elfo", "elfos", "anao", "anoes", "sprite", "sereia", "orc", "goblin", "ogre")),
    ("linhagens", ("linhagem", "linhagens", "vampiro", "vampiros", "youkai", "youkais", "imortal", "imortais", "fera", "feras")),
    ("atributos_pericias", ("atributo", "atributos", "pericia", "pericias", "especializacao", "especializacoes")),
    ("combate", ("combate", "manobra", "manobras", "ataque", "defesa", "dano", "armas", "armaduras")),
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

    resolved = {duplicate_to_canonical.get(source_id, source_id) for source_id in selected}
    return sorted(source_id for source_id in resolved if source_id in sources and source_id in books)


def aprimoramento_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock = read_json(INDEX_DIR / "aprimoramentos-certified-lock.json", {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


def kit_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock = read_json(INDEX_DIR / "kits-certified-lock.json", {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


def class_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock = read_json(INDEX_DIR / "classes-certified-lock.json", {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


def race_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock = read_json(INDEX_DIR / "racas-certified-lock.json", {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


def lineage_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock = read_json(INDEX_DIR / "linhagens-certified-lock.json", {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


def power_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock = read_json(INDEX_DIR / "poderes-certified-lock.json", {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


def magic_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock = read_json(INDEX_DIR / "magias-certified-lock.json", {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


def ritual_locks() -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    lock = read_json(INDEX_DIR / "rituais-certified-lock.json", {"records": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_source_name: dict[tuple[str, str], dict[str, Any]] = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name


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


def infer_area(category: str, name: str, summary: str, source_title: str) -> tuple[str, float, list[str]]:
    haystack = normalize_for_search(" ".join([name, summary, source_title]))
    matches: list[str] = []
    for area, keywords in AREA_KEYWORDS:
        normalized_keywords = [normalize_for_search(keyword) for keyword in keywords]
        hit_count = sum(1 for keyword in normalized_keywords if keyword in haystack)
        if hit_count:
            matches.append(area)
            if area in {"aprimoramentos", "classes", "kits", "racas", "linhagens", "poderes", "magias"}:
                return area, min(0.92, 0.76 + hit_count * 0.04), matches
            if area != CATEGORY_TO_AREA.get(category):
                return area, min(0.88, 0.72 + hit_count * 0.04), matches

    area = CATEGORY_TO_AREA.get(category, "fontes")
    confidence = 0.78 if area != "fontes" else 0.64
    return area, confidence, matches


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


def build_source_part_items(source_ids: list[str], source_lookup: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for source_id in source_ids:
        book = read_json(BOOKS_DATA_DIR / f"{source_id}.json", {})
        source_title = book.get("title") or source_lookup[source_id].get("title") or source_id
        for part in book.get("parts", []):
            name = part.get("name") or part.get("id") or source_title
            category = part.get("category") or "source"
            summary = part.get("summary") or ""
            area, confidence, matched_areas = infer_area(category, name, summary, source_title)
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
                "entityRefs": part.get("entityRefs", []),
                "tags": sorted(set([area, category, *matched_areas])),
                "confidence": round(confidence, 2),
                "extractionMethod": "book-part-area-pass-1",
            }
            items.append(item)
    return items


def build_entity_items(source_ids: set[str], source_lookup: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    lock_by_id, lock_by_source_name = aprimoramento_locks()
    kit_lock_by_id, kit_lock_by_source_name = kit_locks()
    class_lock_by_id, class_lock_by_source_name = class_locks()
    race_lock_by_id, race_lock_by_source_name = race_locks()
    lineage_lock_by_id, lineage_lock_by_source_name = lineage_locks()
    power_lock_by_id, power_lock_by_source_name = power_locks()
    magic_lock_by_id, magic_lock_by_source_name = magic_locks()
    ritual_lock_by_id, ritual_lock_by_source_name = ritual_locks()
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
            if is_aprimoramento_claim(entity, category, str(name)) and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_power and not is_certified_magic and not is_certified_ritual:
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
            if is_kit_claim(entity, category, str(name)) and not is_certified_kit and not is_certified_aprimoramento and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_power and not is_certified_magic and not is_certified_ritual:
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
            if is_class_claim(entity, category, str(name)) and not is_certified_class and not is_certified_aprimoramento and not is_certified_kit and not is_certified_race and not is_certified_lineage and not is_certified_power and not is_certified_magic and not is_certified_ritual:
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
            if is_lineage_claim(entity, category, str(name)) and not is_certified_lineage and not is_certified_race and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_power and not is_certified_magic and not is_certified_ritual:
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
            if is_race_claim(entity, category, str(name)) and not is_certified_race and not is_certified_lineage and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_power and not is_certified_magic and not is_certified_ritual:
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
            if is_power_claim(entity, category, str(name)) and not is_certified_power and not is_certified_magic and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_ritual:
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
            if is_magic_claim(entity, category, str(name)) and not is_certified_magic and not is_certified_power and not is_certified_aprimoramento and not is_certified_kit and not is_certified_class and not is_certified_race and not is_certified_lineage and not is_certified_ritual:
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
            entries = entity.get("entries") or []
            summary = " ".join(entry for entry in entries if isinstance(entry, str))
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
            else:
                area, confidence, matched_areas = area_for_entity(
                    entity,
                    category,
                    str(name),
                    summary,
                    source_lookup.get(source_id, {}).get("title", source_id),
                )
            item = {
                "id": entity_id,
                "name": name,
                "area": area,
                "category": category,
                "source": source_id,
                "sourceTitle": source_lookup.get(source_id, {}).get("title", source_id),
                "page": entity.get("page"),
                "entries": entries,
                "tags": sorted(set([area, category, *entity.get("tags", []), *matched_areas])),
                "confidence": round(float(entity.get("confidence", confidence)), 2),
                "extractionMethod": entity.get("extractionMethod", "entity-area-pass-1"),
            }
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
    return items


def write_area_files(source_ids: list[str], part_items: list[dict[str, Any]], entity_items: list[dict[str, Any]]) -> dict[str, Any]:
    AREAS_DIR.mkdir(parents=True, exist_ok=True)
    by_area: dict[str, dict[str, list[dict[str, Any]]]] = {
        area: {"entities": [], "sourceParts": []} for area in AREA_LABELS
    }
    for item in part_items:
        if item["area"] in {"aprimoramentos", "kits", "classes", "racas", "linhagens", "poderes", "magias"}:
            continue
        by_area.setdefault(item["area"], {"entities": [], "sourceParts": []})["sourceParts"].append(item)
    for item in entity_items:
        by_area.setdefault(item["area"], {"entities": [], "sourceParts": []})["entities"].append(item)

    area_summaries: list[dict[str, Any]] = []
    for area in AREA_LABELS:
        payload = {
            "version": 1,
            "id": area,
            "name": AREA_LABELS[area],
            "readySourceCount": len(source_ids),
            "entityCount": len(by_area[area]["entities"]),
            "sourcePartCount": len(by_area[area]["sourceParts"]),
            "entities": sorted(by_area[area]["entities"], key=lambda item: (item.get("name") or "", item.get("source") or "")),
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
    part_items = build_source_part_items(source_ids, source_lookup)
    entity_items = build_entity_items(set(source_ids), source_lookup)
    summary = write_area_files(source_ids, part_items, entity_items)
    write_report(summary)
    print(
        f"Area catalog built: {summary['readySourceCount']} sources, "
        f"{summary['sourcePartCount']} source parts, {summary['entityCount']} entities."
    )


if __name__ == "__main__":
    main()
