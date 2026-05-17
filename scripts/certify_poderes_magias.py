from __future__ import annotations

import hashlib
import re
from collections import Counter
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


ENTITIES_PATH = DATA_DIR / "entities" / "power_magic_granular.json"
POWERS_LOCK_PATH = INDEX_DIR / "poderes-certified-lock.json"
MAGICS_LOCK_PATH = INDEX_DIR / "magias-certified-lock.json"
REJECTED_PATH = DATA_DIR / "work" / "poderes-magias-certification-rejected.json"
REPORT_PATH = ROOT / "docs" / "reports" / "certification" / "poderes-magias-certification.md"

CONTEXT_RE = re.compile(
    r"power-magic-book-part|power-source|magic-source|power-term|magic-term|manual-power-magic|auto-inline-cabalistic",
    re.IGNORECASE,
)
RAW_POWER_SIGNAL_RE = re.compile(
    r"\bCustos?\s*:|\bCusto\s+\d+|\bN[ií]vel\s*\d+\s*:|\bUso Autom[aá]tico\b|"
    r"\bPontos? de Poder\b|\bPontos? de F[eé]\b|\bPoder B[aá]sico\b|\bPoderes? compr[aá]veis\b|"
    r"\bCaminhos?\s*:|\bPMs?\b|\bReiatsu\b",
    re.IGNORECASE,
)
RAW_MAGIC_SIGNAL_RE = re.compile(
    r"\bC[ií]rculos?\b|\bEntender\s*-|\bCriar\s*-|\bControlar\s*-|\bFocus\b|"
    r"\bPontos? de Magia\b|\bPMs?\b|\bAlcance\s*:|\bDura[cç][aã]o\s*:|\bEfeito\s*:|"
    r"\bCaminhos?\s*:|\bMagia\s*:|\bEscola\s*:",
    re.IGNORECASE,
)
RAW_MAGIC_STRUCTURE_RE = re.compile(
    r"\bCustos?\s*:|\bEntender\s*-|\bCriar\s*-|\bControlar\s*-|"
    r"\bAlcance\s*:|\bDura[cç][aã]o\s*:|\bEfeito\s*:|\bCaminhos?\s*:|\bEscola\s*:",
    re.IGNORECASE,
)
STAT_BLOCK_RE = re.compile(
    r"\bCON\s+\d+|\bFR\s+\d+|\bDEX\s+\d+|\bAGI\s+\d+|\bWILL\s+\d+|\bPER\s+\d+|"
    r"\bCAR\s+\d+|\bPVs?\b|\bIP\s*:?\s*\d+|\b#?Ataques?\b|\bdano\s+\d+d",
    re.IGNORECASE,
)

BAD_NAMES = {
    "agradecimentos",
    "a arabia",
    "a historia",
    "alguns",
    "alem",
    "aprimoramentos",
    "atributos",
    "avancado",
    "bardo",
    "bibliografia",
    "bocas",
    "caminho",
    "caminhos",
    "capitulo",
    "campanhas possiveis",
    "car",
    "captare",
    "classes",
    "conforme",
    "confere",
    "conquistador",
    "consegue",
    "conclusao",
    "crimes",
    "daemon",
    "daemon medieval",
    "death",
    "deve",
    "descricao",
    "efeito",
    "eles",
    "energia mistica",
    "estatiticas classicas",
    "estatisticas classicas",
    "este",
    "estes",
    "existencia",
    "evolucao",
    "grande",
    "grande lista",
    "grimorio",
    "historia",
    "indice",
    "introducao",
    "kit",
    "kits",
    "magia",
    "magias",
    "muitos",
    "nivel",
    "nao",
    "narrador",
    "necessario",
    "necessario o",
    "nota",
    "novas regras",
    "o combate",
    "poder",
    "poderes",
    "poderes animais",
    "poderes arcadianos",
    "poderes de classe",
    "poderes demoniacos",
    "poderes misticos",
    "poderes mentais",
    "prefacio",
    "primarios",
    "pvs",
    "permite",
    "retarda",
    "ritual",
    "rituais",
    "saliva",
    "situacoes especiais",
    "sumario",
    "super poderes",
    "tal",
    "tambem",
    "usado",
    "will",
}

POWER_TERMS = {
    "animalidade",
    "cabalistico",
    "cabalisticos",
    "fe",
    "kidou",
    "mental",
    "mentais",
    "milagre",
    "poder",
    "poderes",
    "psionico",
    "psiquismo",
    "reiatsu",
    "superpoder",
    "superpoderes",
}
MAGIC_TERMS = {
    "arcano",
    "circulo",
    "circulos",
    "caminho",
    "caminhos",
    "feitico",
    "feiticos",
    "focus",
    "grimorio",
    "magia",
    "magias",
    "mago",
    "magos",
}
RITUAL_TERMS = {"ritual", "rituais", "invocacao", "invocacoes"}


def normalize_key(value: str) -> str:
    return slugify(value).replace("-", " ")


def has_any_term(text: str, terms: set[str]) -> bool:
    tokens = set(text.split())
    return bool(tokens & terms)


def normalized_signal(text: str, patterns: list[str]) -> bool:
    return any(pattern in text for pattern in patterns)


def lock_source_names(path_name: str) -> set[tuple[str, str]]:
    lock = read_json(INDEX_DIR / path_name, {"records": []})
    return {
        (record["source"], record["nameKey"])
        for record in lock.get("records", [])
        if record.get("source") and record.get("nameKey")
    }


def body_text(entity: dict[str, Any]) -> str:
    entries = entity.get("entries") or []
    return "\n".join(entry for entry in entries if isinstance(entry, str))


def content_key(entity: dict[str, Any]) -> tuple[str, str]:
    body = re.sub(r"\s+", " ", body_text(entity)).strip().lower()
    digest = hashlib.sha1(body.encode("utf-8", errors="ignore")).hexdigest()
    return (slugify(str(entity.get("name") or "")), digest)


def has_power_signal(entity: dict[str, Any], body: str, normalized: str) -> bool:
    context = str(entity.get("powerMagicContext") or "")
    head = body[:900]
    normalized_head = normalize_key(head)
    if RAW_POWER_SIGNAL_RE.search(head):
        return True
    return (
        "power-source" in context
        and has_any_term(normalized_head, POWER_TERMS)
        and normalized_signal(
            normalized_head,
            [
                "custo",
                "custos",
                "nivel",
                "pontos de poder",
                "pontos de fe",
                "uso automatico",
                "reiatsu",
                "pms",
            ],
        )
    )


def has_magic_signal(entity: dict[str, Any], body: str, normalized: str) -> bool:
    context = str(entity.get("powerMagicContext") or "")
    name = normalize_key(str(entity.get("name") or ""))
    head = body[:900]
    normalized_head = normalize_key(head)
    if RAW_MAGIC_STRUCTURE_RE.search(head):
        return True
    return (
        "magic-source" in context
        and has_any_term(f"{name} {normalized_head}", MAGIC_TERMS)
        and normalized_signal(
            f"{name} {normalized_head}",
            [
                "circulo",
                "circulos",
                "entender",
                "criar",
                "controlar",
                "focus",
                "pontos de magia",
                "alcance",
                "duracao",
                "efeito",
                "pms",
            ],
        )
    )


def looks_like_stat_block(body: str) -> bool:
    head = body[:900]
    return len(STAT_BLOCK_RE.findall(head)) >= 5


def looks_like_kit_or_aprimoramento(name_key: str, body: str) -> bool:
    normalized = normalize_key(body[:1200])
    if "aprimoramento" in name_key.split() or "aprimoramentos" in name_key.split():
        return True
    return (
        "pericias" in normalized
        and "aprimoramentos" in normalized
        and ("pontos heroicos" in normalized or "pts de pericia" in normalized or "pts aprimoramento" in normalized)
    )


def canonicalized_entity(entity: dict[str, Any]) -> dict[str, Any]:
    name_key = normalize_key(str(entity.get("name") or ""))
    body = body_text(entity)
    magic_name_prefixes = ("caminhos ", "entender ", "criar ", "controlar ", "criar controlar ", "entender controlar ")
    if entity.get("subtype") == "poder" and name_key.startswith(magic_name_prefixes) and RAW_MAGIC_STRUCTURE_RE.search(body[:900]):
        source = entity.get("source")
        name = str(entity.get("name") or "")
        payload = {
            **entity,
            "id": f"magia-{source}-{slugify(name)}",
            "subtype": "magia",
        }
        payload["tags"] = sorted(set([tag for tag in payload.get("tags", []) if tag != "poder"] + ["magia"]))
        return payload
    return entity


def certification_failure(
    entity: dict[str, Any],
    locked_names: dict[str, set[tuple[str, str]]],
) -> str | None:
    name = str(entity.get("name") or "").strip()
    name_key = normalize_key(name)
    source_name = (entity.get("source"), slugify(name))
    body = body_text(entity)
    combined = f"{name}\n{body}"
    normalized = normalize_key(combined)
    context = str(entity.get("powerMagicContext") or "")
    subtype = entity.get("subtype")

    for lock_name, names in locked_names.items():
        if source_name in names:
            return f"locked_as_{lock_name}"
    if entity.get("category") != "power_magic":
        return "category_is_not_power_magic"
    if subtype == "poder" and "aprimoramento" in normalize_key(str(entity.get("source") or "")):
        return "source_is_aprimoramento"
    if subtype not in {"poder", "magia"}:
        return "subtype_is_not_poder_or_magia"
    if subtype == "poder" and not str(entity.get("id") or "").startswith("poder-"):
        return "id_is_not_poder"
    if subtype == "magia" and not str(entity.get("id") or "").startswith("magia-"):
        return "id_is_not_magia"
    if not CONTEXT_RE.search(context):
        return "no_explicit_power_magic_context"
    if not name or name_key in BAD_NAMES:
        return "name_is_section_or_empty"
    if name_key.startswith("apenas para ") or name_key.startswith("escolha "):
        return "name_is_section_or_empty"
    letters = [char for char in name if char.isalpha()]
    if len(name.split()) > 1 and letters and sum(1 for char in letters if char.isupper()) / len(letters) > 0.85:
        return "name_looks_like_section_heading"
    if any(char in name for char in [".", ",", ";", "?", "!", "="]):
        return "name_has_sentence_punctuation"
    if ":" in name and not normalize_key(name).startswith("caminhos "):
        return "name_has_sentence_punctuation"
    if name.startswith("(") or re.match(r"^\d", name):
        return "name_starts_with_broken_marker"
    if len(body) < 45:
        return "entry_too_short"
    if looks_like_stat_block(body):
        return "looks_like_stat_block"
    if looks_like_kit_or_aprimoramento(name_key, body):
        return "looks_like_kit_or_aprimoramento"

    name_terms = set(name_key.split())
    if name_terms & RITUAL_TERMS:
        return "looks_like_ritual"

    if subtype == "poder":
        if not has_any_term(normalized, POWER_TERMS) and "power-source" not in context:
            return "no_power_term"
        if not has_power_signal(entity, body, normalized):
            return "no_mechanical_power_signal"
        return None

    if subtype == "magia":
        if not has_any_term(normalized, MAGIC_TERMS) and "magic-source" not in context:
            return "no_magic_term"
        if has_any_term(normalized, RITUAL_TERMS) and not has_magic_signal(entity, body, normalized):
            return "looks_like_ritual"
        if not has_magic_signal(entity, body, normalized):
            return "no_mechanical_magic_signal"
        return None

    return None


def certified_payload(entity: dict[str, Any]) -> dict[str, Any]:
    certified_area = "poderes" if entity["subtype"] == "poder" else "magias"
    lock_prefix = "poder-lock" if entity["subtype"] == "poder" else "magia-lock"
    certification_id = f"{lock_prefix}:{entity['source']}:{slugify(entity['name'])}"
    payload = {
        **entity,
        "category": "power_magic",
        "certificationStatus": "certified",
        "certifiedAs": entity["subtype"],
        "certifiedArea": certified_area,
        "lockedArea": certified_area,
        "certificationId": certification_id,
        "certificationMethod": "power-magic-explicit-context-mechanical-pass-1",
    }
    payload["tags"] = sorted(set([*payload.get("tags", []), entity["subtype"], certified_area, "certificado"]))
    return payload


def lock_records(certified: list[dict[str, Any]], subtype: str) -> list[dict[str, Any]]:
    return [
        {
            "id": entity["id"],
            "source": entity["source"],
            "name": entity["name"],
            "nameKey": slugify(entity["name"]),
            "category": "power_magic",
            "subtype": entity["subtype"],
            "lockedArea": entity["lockedArea"],
            "certificationId": entity["certificationId"],
        }
        for entity in certified
        if entity["subtype"] == subtype
    ]


def main() -> None:
    DATA_DIR.joinpath("work").mkdir(parents=True, exist_ok=True)
    entities = read_json(ENTITIES_PATH, [])
    if not isinstance(entities, list):
        raise SystemExit("power_magic_granular.json is not a list.")

    locked_names = {
        "aprimoramento": lock_source_names("aprimoramentos-certified-lock.json"),
        "kit": lock_source_names("kits-certified-lock.json"),
        "class": lock_source_names("classes-certified-lock.json"),
        "raca": lock_source_names("racas-certified-lock.json"),
        "linhagem": lock_source_names("linhagens-certified-lock.json"),
    }

    certified: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_source_names: set[tuple[str, str]] = set()
    seen_content_keys: set[tuple[str, str]] = set()

    for raw_entity in entities:
        entity = canonicalized_entity(raw_entity)
        failure = certification_failure(entity, locked_names)
        source_name = (entity.get("source"), slugify(str(entity.get("name") or "")))
        duplicate_content_key = content_key(entity)
        if entity.get("id") in seen_ids or source_name in seen_source_names:
            failure = "duplicate_certification_key"
        elif duplicate_content_key in seen_content_keys:
            failure = "duplicate_certification_content"
        if failure:
            rejected.append({**entity, "certificationStatus": "rejected", "rejectionReason": failure})
            continue
        payload = certified_payload(entity)
        certified.append(payload)
        seen_ids.add(payload["id"])
        seen_source_names.add((payload["source"], slugify(payload["name"])))
        seen_content_keys.add(duplicate_content_key)

    write_json(ENTITIES_PATH, certified)
    write_json(REJECTED_PATH, rejected)

    power_records = lock_records(certified, "poder")
    magic_records = lock_records(certified, "magia")
    powers_lock = {
        "version": 1,
        "area": "poderes",
        "policy": {
            "certified_items_are_locked_to_area": True,
            "certified_items_must_not_be_duplicated_in_other_categories": True,
            "uncertified_power_claims_do_not_enter_poderes": True,
            "certified_aprimoramentos_kits_classes_racas_and_linhagens_are_not_reclassified_as_poderes": True,
        },
        "certifiedCount": len(power_records),
        "rejectedCount": len(rejected),
        "records": power_records,
    }
    magics_lock = {
        "version": 1,
        "area": "magias",
        "policy": {
            "certified_items_are_locked_to_area": True,
            "certified_items_must_not_be_duplicated_in_other_categories": True,
            "uncertified_magic_claims_do_not_enter_magias": True,
            "certified_aprimoramentos_kits_classes_racas_and_linhagens_are_not_reclassified_as_magias": True,
            "rituais_are_kept_in_rituais": True,
        },
        "certifiedCount": len(magic_records),
        "rejectedCount": len(rejected),
        "records": magic_records,
    }
    write_json(POWERS_LOCK_PATH, powers_lock)
    write_json(MAGICS_LOCK_PATH, magics_lock)

    counts = Counter(entity["source"] for entity in certified)
    kinds = Counter(entity["subtype"] for entity in certified)
    rejection_counts = Counter(entity["rejectionReason"] for entity in rejected)
    lines = [
        "# Poderes e magias certification",
        "",
        "Varredura das fontes prontas com travas separadas para poderes e magias.",
        "",
        f"- Certified items: {len(certified)}",
        f"- Certified poderes: {kinds.get('poder', 0)}",
        f"- Certified magias: {kinds.get('magia', 0)}",
        f"- Rejected candidates: {len(rejected)}",
        "",
        "## Policy",
        "",
        "- A certified poder is locked to `poderes`.",
        "- A certified magia is locked to `magias`.",
        "- Certified poderes/magias cannot be duplicated in another category.",
        "- Items already locked as `aprimoramentos`, `kits`, `classes`, `racas` or `linhagens` are rejected here.",
        "- Ritual-looking records stay out of `magias` unless they expose clear magic mechanics.",
        "",
        "## Certified by source",
        "",
        "| Source | Certified |",
        "| --- | ---: |",
    ]
    for source, count in counts.most_common():
        lines.append(f"| `{source}` | {count} |")
    lines.extend(["", "## Rejection reasons", "", "| Reason | Count |", "| --- | ---: |"])
    for reason, count in rejection_counts.most_common():
        lines.append(f"| `{reason}` | {count} |")
    if rejected:
        lines.extend(["", "## Rejected sample", ""])
        for entity in rejected[:120]:
            lines.append(f"- `{entity.get('source')}` / `{entity.get('name')}`: {entity.get('rejectionReason')}")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Certified {len(certified)} poderes/magias; rejected {len(rejected)} candidates.")


if __name__ == "__main__":
    main()
