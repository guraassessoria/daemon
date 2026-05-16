from __future__ import annotations

import re
from collections import Counter
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


ENTITIES_PATH = DATA_DIR / "entities" / "character_option_granular.json"
LOCK_PATH = INDEX_DIR / "aprimoramentos-certified-lock.json"
REJECTED_PATH = DATA_DIR / "work" / "aprimoramentos-certification-rejected.json"
REPORT_PATH = ROOT / "docs" / "aprimoramentos-certification.md"

MECHANICAL_RE = re.compile(
    r"\b-?\d+\s*(?:a\s*\d+\s*)?pontos?\b|\bvari[aá]vel\b|para cada ponto|"
    r"pontos? de aprimoramento|custo|restri[cç][aã]o|pr[eé]-?requisito",
    re.IGNORECASE,
)

BAD_NAMES = {
    "aprimoramentos",
    "aprimoramentos positivos",
    "aprimoramentos negativos",
    "aprimoramentos regionais",
    "desenvolvimento",
    "agradecimentos",
    "introducao",
    "introdução",
    "vantagens",
    "desvantagens",
    "talentos",
}


def published_sources() -> set[str]:
    report = read_json(INDEX_DIR / "granular-aprimoramentos-report.json", {})
    return {item["source"] for item in report.get("sources", []) if item.get("source")}


def certification_failure(entity: dict[str, Any], allowed_sources: set[str]) -> str | None:
    name = str(entity.get("name") or "").strip()
    body = "\n".join(entry for entry in entity.get("entries", []) if isinstance(entry, str))
    if entity.get("source") not in allowed_sources:
        return "source_not_in_publishable_aprimoramento_set"
    if entity.get("category") != "character_option":
        return "category_is_not_character_option"
    if entity.get("subtype") != "aprimoramento":
        return "subtype_is_not_aprimoramento"
    if not str(entity.get("id") or "").startswith("aprimoramento-"):
        return "id_is_not_aprimoramento"
    if not name or slugify(name) in BAD_NAMES:
        return "name_is_section_or_empty"
    if len(body) < 30:
        return "entry_too_short"
    if not MECHANICAL_RE.search(body):
        return "no_mechanical_aprimoramento_signal"
    return None


def certified_payload(entity: dict[str, Any]) -> dict[str, Any]:
    certification_id = f"aprimoramento-lock:{entity['source']}:{slugify(entity['name'])}"
    payload = {
        **entity,
        "category": "character_option",
        "subtype": "aprimoramento",
        "certificationStatus": "certified",
        "certifiedAs": "aprimoramento",
        "certifiedArea": "aprimoramentos",
        "lockedArea": "aprimoramentos",
        "certificationId": certification_id,
        "certificationMethod": "aprimoramento-source-mechanical-pass-1",
    }
    payload["tags"] = sorted(set([*payload.get("tags", []), "aprimoramento", "certificado"]))
    return payload


def main() -> None:
    DATA_DIR.joinpath("work").mkdir(parents=True, exist_ok=True)
    entities = read_json(ENTITIES_PATH, [])
    if not isinstance(entities, list):
        raise SystemExit("character_option_granular.json is not a list.")

    allowed_sources = published_sources()
    certified: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_source_names: set[tuple[str, str]] = set()

    for entity in entities:
        failure = certification_failure(entity, allowed_sources)
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
            "category": "character_option",
            "subtype": "aprimoramento",
            "lockedArea": "aprimoramentos",
            "certificationId": entity["certificationId"],
        }
        for entity in certified
    ]
    lock = {
        "version": 1,
        "area": "aprimoramentos",
        "policy": {
            "certified_items_are_locked_to_area": True,
            "certified_items_must_not_be_duplicated_in_other_categories": True,
            "uncertified_character_options_do_not_enter_aprimoramentos": True,
        },
        "certifiedCount": len(certified),
        "rejectedCount": len(rejected),
        "records": lock_records,
    }
    write_json(LOCK_PATH, lock)

    counts = Counter(entity["source"] for entity in certified)
    lines = [
        "# Aprimoramentos certification",
        "",
        "Reinicio da area de aprimoramentos com trava de certificacao.",
        "",
        f"- Certified aprimoramentos: {len(certified)}",
        f"- Rejected candidates: {len(rejected)}",
        "",
        "## Policy",
        "",
        "- A certified aprimoramento is locked to `aprimoramentos`.",
        "- A certified aprimoramento cannot be duplicated in another category.",
        "- Generic/manual character option summaries are not allowed in `aprimoramentos`.",
        "",
        "## Certified by source",
        "",
        "| Source | Certified |",
        "| --- | ---: |",
    ]
    for source, count in counts.most_common():
        lines.append(f"| `{source}` | {count} |")
    if rejected:
        lines.extend(["", "## Rejected", ""])
        for entity in rejected[:80]:
            lines.append(f"- `{entity.get('source')}` / `{entity.get('name')}`: {entity.get('rejectionReason')}")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Certified {len(certified)} aprimoramentos; rejected {len(rejected)} candidates.")


if __name__ == "__main__":
    main()
