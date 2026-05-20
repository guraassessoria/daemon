from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


ENTITY_FILES = [
    DATA_DIR / "entities" / "core_rule.json",
    DATA_DIR / "entities" / "combat.json",
    DATA_DIR / "entities" / "attribute_skill.json",
]
LOCK_PATH = INDEX_DIR / "regras-base-certified-lock.json"
REJECTED_PATH = DATA_DIR / "work" / "regras-base-certification-rejected.json"
REPORT_PATH = ROOT / "docs" / "reports" / "certification" / "regras-base-certification.md"

VALID_CATEGORIES = {"core_rule", "attribute_skill", "combat"}
MECHANICAL_RE = re.compile(
    r"\b(?:regra|regras|sistema|teste|testes|atributo|atributos|per[ií]cia|per[ií]cias|"
    r"especializa[cç][aã]o|combate|dano|ferimentos|pontos?|modificadores?|penalidade|"
    r"b[oô]nus|dificuldade|resolu[cç][aã]o|cria[cç][aã]o de personagem|narrador|mestre)\b",
    re.IGNORECASE,
)
BAD_NAMES = {
    "agradecimentos",
    "atributos",
    "capitulo",
    "combate",
    "creditos",
    "indice",
    "introducao",
    "pericias",
    "regras",
    "sumario",
}


def body_text(entity: dict[str, Any]) -> str:
    entries = entity.get("entries") or []
    return "\n".join(entry for entry in entries if isinstance(entry, str)).strip()


def certification_failure(entity: dict[str, Any]) -> str | None:
    name = str(entity.get("name") or "").strip()
    name_key = slugify(name).replace("-", " ")
    body = body_text(entity)
    category = entity.get("category")

    if category not in VALID_CATEGORIES:
        return "category_is_not_regras_base"
    if not str(entity.get("id") or ""):
        return "missing_id"
    if not entity.get("source"):
        return "missing_source"
    if not name or name_key in BAD_NAMES:
        return "name_is_section_or_empty"
    if any(char in name for char in [";", "?", "!"]):
        return "name_has_sentence_punctuation"
    if len(body) < 45:
        return "entry_too_short"
    if not MECHANICAL_RE.search(f"{name} {body} {' '.join(entity.get('tags', []) or [])}"):
        return "no_rule_mechanical_signal"
    return None


def certified_payload(entity: dict[str, Any]) -> dict[str, Any]:
    certification_id = f"regras-base-lock:{entity['source']}:{slugify(entity['name'])}"
    payload = {
        **entity,
        "certificationStatus": "certified",
        "certifiedAs": "regra_base",
        "certifiedArea": "regras_base",
        "lockedArea": "regras_base",
        "certificationId": certification_id,
        "certificationMethod": "regras-base-mechanical-pass-1",
    }
    payload["tags"] = sorted(set([*payload.get("tags", []), "regras-base", "certificado"]))
    return payload


def read_entities(path: Path) -> list[dict[str, Any]]:
    payload = read_json(path, [])
    if not isinstance(payload, list):
        raise SystemExit(f"{path.name} is not a list.")
    return [item for item in payload if isinstance(item, dict)]


def write_entities(path: Path, entities: list[dict[str, Any]]) -> None:
    if path.exists() or entities:
        write_json(path, entities)


def main() -> None:
    DATA_DIR.joinpath("work").mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    certified_by_file: dict[Path, list[dict[str, Any]]] = {path: [] for path in ENTITY_FILES}
    rejected: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_source_names: set[tuple[str, str]] = set()

    for path in ENTITY_FILES:
        for entity in read_entities(path):
            failure = certification_failure(entity)
            source_name = (entity.get("source"), slugify(str(entity.get("name") or "")))
            if entity.get("id") in seen_ids or source_name in seen_source_names:
                failure = "duplicate_certification_key"
            if failure:
                rejected.append({**entity, "entityFile": path.name, "certificationStatus": "rejected", "rejectionReason": failure})
                continue
            payload = certified_payload(entity)
            certified_by_file[path].append(payload)
            seen_ids.add(payload["id"])
            seen_source_names.add((payload["source"], slugify(payload["name"])))

    for path, entities in certified_by_file.items():
        write_entities(path, entities)

    certified = [entity for entities in certified_by_file.values() for entity in entities]
    lock = {
        "version": 1,
        "area": "regras_base",
        "policy": {
            "certified_items_are_locked_to_area": True,
            "certified_items_must_not_be_duplicated_in_other_categories": True,
            "uncertified_regras_base_claims_do_not_enter_regras_base": True,
        },
        "records": [
            {
                "id": entity["id"],
                "source": entity["source"],
                "name": entity["name"],
                "nameKey": slugify(entity["name"]),
                "category": entity["category"],
                "lockedArea": "regras_base",
                "certificationId": entity["certificationId"],
            }
            for entity in certified
        ],
    }
    write_json(LOCK_PATH, lock)
    write_json(REJECTED_PATH, rejected)

    rejected_counts = Counter(item["rejectionReason"] for item in rejected)
    report = [
        "# Certificacao de Regras Base",
        "",
        f"- Certificados: {len(certified)}",
        f"- Rejeitados: {len(rejected)}",
        "",
        "## Politica",
        "",
        "- Somente registros com categoria `core_rule`, `attribute_skill` ou `combat` entram em `Regras Base` como entidade certificada.",
        "- Registros certificados ficam travados em `regras_base` e nao devem ser publicados em outra area.",
        "- Reivindicacoes de regra base sem certificacao sao enviadas para quarentena operacional.",
        "",
        "## Rejeicoes",
        "",
    ]
    if rejected_counts:
        report.extend(f"- {reason}: {count}" for reason, count in sorted(rejected_counts.items()))
    else:
        report.append("- Nenhuma rejeicao.")
    report.extend(["", "## Registros certificados", ""])
    report.extend(f"- {entity['name']} ({entity['source']}, {entity['category']})" for entity in certified)
    REPORT_PATH.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"certified {len(certified)} regras_base records; rejected {len(rejected)}")


if __name__ == "__main__":
    main()
