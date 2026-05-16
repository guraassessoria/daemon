from __future__ import annotations

import re
from collections import Counter
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


ENTITIES_PATH = DATA_DIR / "entities" / "class_granular.json"
LOCK_PATH = INDEX_DIR / "classes-certified-lock.json"
REJECTED_PATH = DATA_DIR / "work" / "classes-certification-rejected.json"
REPORT_PATH = ROOT / "docs" / "classes-certification.md"

MECHANICAL_RE = re.compile(
    r"\bCusto\s*:|\bPer[ií]cias?\s*:|\bAprimoramentos?\s*:|\bAtributos Principais\s*:|"
    r"\bPer[ií]cias Obrigat[oó]rias\s*:|\bPer[ií]cias Sugeridas\s*:|"
    r"\bPoderes? de Classe\b|\bPoderes compr[aá]veis\b|\bB[oô]nus de Treino\s*:|"
    r"\bRequer\s*:|\bRequisitos?\s*:|\bN[ií]vel da classe\b",
    re.IGNORECASE,
)
CLASS_CONTEXT_RE = re.compile(r"manual-extractor|text-class-term|book-part|cargo-section", re.IGNORECASE)

BAD_NAMES = {
    "3d t",
    "aprimoramento",
    "aprimoramentos",
    "atributos",
    "caminho",
    "caminhos",
    "classe",
    "classes",
    "daemon",
    "daemon medieval",
    "kits",
    "kits de personagem",
    "novos kits",
    "pericia",
    "pericias",
    "perícia",
    "perícias",
    "poderes",
    "poderes de classe",
    "regras",
}


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


def certification_failure(
    entity: dict[str, Any],
    kit_names: set[tuple[str, str]],
    aprimoramento_names: set[tuple[str, str]],
) -> str | None:
    name = str(entity.get("name") or "").strip()
    name_key = slugify(name)
    source_name = (entity.get("source"), name_key)
    body = body_text(entity)
    context = str(entity.get("classContext") or "")
    class_kind = str(entity.get("classKind") or "")

    if source_name in kit_names:
        return "locked_as_kit"
    if source_name in aprimoramento_names:
        return "locked_as_aprimoramento"
    if entity.get("category") != "character_class":
        return "category_is_not_character_class"
    if entity.get("subtype") != "class":
        return "subtype_is_not_class"
    if not str(entity.get("id") or "").startswith("classe-"):
        return "id_is_not_class"
    if not CLASS_CONTEXT_RE.search(context):
        return "no_explicit_class_context"
    if not name or name_key.replace("-", " ") in BAD_NAMES or name_key.startswith("kit-") or name_key.startswith("kits-"):
        return "name_is_section_or_empty"
    if any(char in name for char in [".", ",", ";", ":"]):
        return "name_has_sentence_punctuation"
    if len(body) < 45:
        return "entry_too_short"

    if class_kind == "cargo":
        if entity.get("source") != "abismo-infinito-quick-start" or "cargo-section" not in context:
            return "cargo_without_source_section"
        return None

    if len(body) < 80:
        return "mechanical_class_entry_too_short"
    if not MECHANICAL_RE.search(body):
        return "no_mechanical_class_signal"
    return None


def certified_payload(entity: dict[str, Any]) -> dict[str, Any]:
    certification_id = f"class-lock:{entity['source']}:{slugify(entity['name'])}"
    payload = {
        **entity,
        "category": "character_class",
        "subtype": "class",
        "certificationStatus": "certified",
        "certifiedAs": "class",
        "certifiedArea": "classes",
        "lockedArea": "classes",
        "certificationId": certification_id,
        "certificationMethod": "class-explicit-context-mechanical-pass-1",
    }
    payload["tags"] = sorted(set([*payload.get("tags", []), "classe", "certificado"]))
    return payload


def main() -> None:
    DATA_DIR.joinpath("work").mkdir(parents=True, exist_ok=True)
    entities = read_json(ENTITIES_PATH, [])
    if not isinstance(entities, list):
        raise SystemExit("class_granular.json is not a list.")

    kit_names = lock_source_names("kits-certified-lock.json")
    aprimoramento_names = lock_source_names("aprimoramentos-certified-lock.json")

    certified: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_source_names: set[tuple[str, str]] = set()

    for entity in entities:
        failure = certification_failure(entity, kit_names, aprimoramento_names)
        source_name = (entity.get("source"), slugify(str(entity.get("name") or "")))
        if entity.get("id") in seen_ids or source_name in seen_source_names:
            failure = "duplicate_certification_key"
        if failure:
            rejected.append({**entity, "certificationStatus": "rejected", "rejectionReason": failure})
            continue
        payload = certified_payload(entity)
        certified.append(payload)
        seen_ids.add(payload["id"])
        seen_source_names.add((payload["source"], slugify(payload["name"])))

    write_json(ENTITIES_PATH, certified)
    write_json(REJECTED_PATH, rejected)

    lock_records = [
        {
            "id": entity["id"],
            "source": entity["source"],
            "name": entity["name"],
            "nameKey": slugify(entity["name"]),
            "category": "character_class",
            "subtype": "class",
            "lockedArea": "classes",
            "certificationId": entity["certificationId"],
        }
        for entity in certified
    ]
    lock = {
        "version": 1,
        "area": "classes",
        "policy": {
            "certified_items_are_locked_to_area": True,
            "certified_items_must_not_be_duplicated_in_other_categories": True,
            "uncertified_class_claims_do_not_enter_classes": True,
            "certified_kits_and_aprimoramentos_are_not_reclassified_as_classes": True,
        },
        "certifiedCount": len(certified),
        "rejectedCount": len(rejected),
        "records": lock_records,
    }
    write_json(LOCK_PATH, lock)

    counts = Counter(entity["source"] for entity in certified)
    rejection_counts = Counter(entity["rejectionReason"] for entity in rejected)
    lines = [
        "# Classes certification",
        "",
        "Varredura das 190 fontes com trava de certificacao para classes, profissoes, arquetipos e cargos.",
        "",
        f"- Certified classes: {len(certified)}",
        f"- Rejected candidates: {len(rejected)}",
        "",
        "## Policy",
        "",
        "- A certified class is locked to `classes`.",
        "- A certified class cannot be duplicated in another category.",
        "- Items already locked as `kits` or `aprimoramentos` are rejected for classes.",
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
        for entity in rejected[:80]:
            lines.append(f"- `{entity.get('source')}` / `{entity.get('name')}`: {entity.get('rejectionReason')}")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Certified {len(certified)} classes; rejected {len(rejected)} candidates.")


if __name__ == "__main__":
    main()
