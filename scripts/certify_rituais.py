from __future__ import annotations

import hashlib
import re
from collections import Counter
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json
from granular_validation import certification_quality_failure


ENTITIES_PATH = DATA_DIR / "entities" / "ritual_spell_granular.json"
LOCK_PATH = INDEX_DIR / "rituais-certified-lock.json"
REJECTED_PATH = DATA_DIR / "work" / "rituais-certification-rejected.json"
REPORT_PATH = ROOT / "docs" / "reports" / "certification" / "rituais-certification.md"

CONTEXT_RE = re.compile(r"ritual-book-part|ritual-term|dedicated-ritual-source|manual-ritual-spell", re.IGNORECASE)
RITUAL_METHOD_RE = re.compile(
    r"\b(?:Entender|Criar|Controlar)(?:\s*/\s*(?:Entender|Criar|Controlar))*\b.*\b\d{1,2}\b|"
    r"\bCustos?\s*:|\bTempo de Conjura[cç][aã]o\s*:|\bMateriais?\s*:|\bApenas por Ritual\b|"
    r"\bC[ií]rculo de invoca[cç][aã]o\b",
    re.IGNORECASE,
)
RITUAL_STRONG_RE = re.compile(
    r"\bTempo de Conjura[cç][aã]o\s*:|\bMateriais?\s*:|\bApenas por Ritual\b|\britual\b|\brituais\b",
    re.IGNORECASE,
)
KITLIKE_RE = re.compile(
    r"\bCustos?\s*:.*\bPontos? de Per[ií]cia\b|\bPer[ií]cias?\s*:.*\bAprimoramentos?\s*:|"
    r"\bpts?\.? de Aprimoramento\b.*\bpts?\.? de Per[ií]cia\b",
    re.IGNORECASE | re.DOTALL,
)
STAT_BLOCK_RE = re.compile(
    r"\bCON\s*\[?\d|\bFR\s*\[?\d|\bDEX\s*\[?\d|\bAGI\s*\[?\d|\bWILL\s*\[?\d|\bPER\s*\[?\d|"
    r"\bCAR\s*\[?\d|\bPVs?\b|\bIP\s*:?\s*\d|#?Ataques?",
    re.IGNORECASE,
)

BAD_NAMES = {
    "agradecimentos",
    "apenas por ritual",
    "atributos",
    "bibliografia",
    "car",
    "classes",
    "consagracao",
    "custo",
    "custo nenhum",
    "daemon",
    "esses",
    "efeitos magicos",
    "exemplos",
    "focus",
    "grimorio",
    "indice",
    "introducao",
    "lista de novos efeitos",
    "magia",
    "magia negra",
    "magias",
    "materiais nenhum",
    "novas magias e rituais",
    "pagina inicial",
    "prefacio",
    "ritual",
    "rituais",
    "rituais necromanticos",
    "sanidade",
    "sumario",
    "transformacao elemental",
    "tempo de conjuracao imediato",
}


def normalize_key(value: str) -> str:
    return slugify(value).replace("-", " ")


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


def looks_like_stat_block(body: str) -> bool:
    head = body[:700]
    has_explicit_ritual_setup = bool(
        re.search(r"\bTempo de Conjura[cç][aã]o\s*:", head, flags=re.IGNORECASE)
        and re.search(r"\bMateriais?\s*:", head, flags=re.IGNORECASE)
    )
    return len(STAT_BLOCK_RE.findall(body[:1000])) >= 5 and not has_explicit_ritual_setup


def has_ritual_signal(body: str) -> bool:
    head = body[:700]
    if not RITUAL_METHOD_RE.search(head):
        return False
    if re.search(r"\britual\b|\brituais\b|\bApenas por Ritual\b", head, flags=re.IGNORECASE):
        return True
    if re.search(r"\bTempo de Conjura[cç][aã]o\s*:", head, flags=re.IGNORECASE) and re.search(r"\bMateriais?\s*:", head, flags=re.IGNORECASE):
        return True
    return False


def certification_failure(entity: dict[str, Any], locked_names: dict[str, set[tuple[str, str]]]) -> str | None:
    name = str(entity.get("name") or "").strip()
    name_key = normalize_key(name)
    source_name = (entity.get("source"), slugify(name))
    body = body_text(entity)
    context = str(entity.get("ritualContext") or "")

    for lock_name, names in locked_names.items():
        if source_name in names:
            return f"locked_as_{lock_name}"
    if entity.get("category") != "ritual_spell":
        return "category_is_not_ritual_spell"
    if entity.get("subtype") != "ritual":
        return "subtype_is_not_ritual"
    if not str(entity.get("id") or "").startswith("ritual-"):
        return "id_is_not_ritual"
    if not CONTEXT_RE.search(context):
        return "no_explicit_ritual_context"
    if not name or name_key in BAD_NAMES:
        return "name_is_section_or_empty"
    if name_key.startswith(("daemon ", "alcance ", "duracao ")):
        return "name_is_mechanical_field"
    if name_key.startswith(("custo ", "tempo de conjuracao", "materiais ", "duracao ")):
        return "name_is_mechanical_field"
    if any(char in name for char in [";", "?", "!", "="]):
        return "name_has_sentence_punctuation"
    if len(body) < 45:
        return "entry_too_short"
    if quality_failure := certification_quality_failure(entity):
        return quality_failure
    if "manual-ritual-spell" not in context and len(body) < 100:
        return "ritual_entry_too_short"
    if re.search(r"\bTempo de Aprendizado\s*:", body[:700], flags=re.IGNORECASE):
        return "looks_like_kit_or_class"
    if KITLIKE_RE.search(body):
        return "looks_like_kit_or_class"
    if looks_like_stat_block(body):
        return "looks_like_stat_block"
    if "manual-ritual-spell" in context:
        return None
    if not has_ritual_signal(body):
        return "no_mechanical_ritual_signal"
    return None


def certified_payload(entity: dict[str, Any]) -> dict[str, Any]:
    certification_id = f"ritual-lock:{entity['source']}:{slugify(entity['name'])}"
    payload = {
        **entity,
        "category": "ritual_spell",
        "subtype": "ritual",
        "certificationStatus": "certified",
        "certifiedAs": "ritual",
        "certifiedArea": "rituais",
        "lockedArea": "rituais",
        "certificationId": certification_id,
        "certificationMethod": "ritual-explicit-context-mechanical-pass-1",
    }
    payload["tags"] = sorted(set([*payload.get("tags", []), "ritual", "certificado"]))
    return payload


def main() -> None:
    DATA_DIR.joinpath("work").mkdir(parents=True, exist_ok=True)
    entities = read_json(ENTITIES_PATH, [])
    if not isinstance(entities, list):
        raise SystemExit("ritual_spell_granular.json is not a list.")

    locked_names = {
        "regras_base": lock_source_names("regras-base-certified-lock.json"),
        "aprimoramento": lock_source_names("aprimoramentos-certified-lock.json"),
        "kit": lock_source_names("kits-certified-lock.json"),
        "class": lock_source_names("classes-certified-lock.json"),
        "raca": lock_source_names("racas-certified-lock.json"),
        "linhagem": lock_source_names("linhagens-certified-lock.json"),
        "poder": lock_source_names("poderes-certified-lock.json"),
        "magia": lock_source_names("magias-certified-lock.json"),
    }

    certified: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_source_names: set[tuple[str, str]] = set()
    seen_content_keys: set[tuple[str, str]] = set()

    for entity in entities:
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

    lock_records = [
        {
            "id": entity["id"],
            "source": entity["source"],
            "name": entity["name"],
            "nameKey": slugify(entity["name"]),
            "category": "ritual_spell",
            "subtype": "ritual",
            "lockedArea": "rituais",
            "certificationId": entity["certificationId"],
        }
        for entity in certified
    ]
    lock = {
        "version": 1,
        "area": "rituais",
        "policy": {
            "certified_items_are_locked_to_area": True,
            "certified_items_must_not_be_duplicated_in_other_categories": True,
            "uncertified_ritual_claims_do_not_enter_rituais": True,
            "certified_regras_base_items_are_not_reclassified_as_rituais": True,
            "certified_poderes_and_magias_are_not_reclassified_as_rituais": True,
            "certified_aprimoramentos_kits_classes_racas_and_linhagens_are_not_reclassified_as_rituais": True,
        },
        "certifiedCount": len(certified),
        "rejectedCount": len(rejected),
        "records": lock_records,
    }
    write_json(LOCK_PATH, lock)

    counts = Counter(entity["source"] for entity in certified)
    rejection_counts = Counter(entity["rejectionReason"] for entity in rejected)
    lines = [
        "# Rituais certification",
        "",
        "Varredura das fontes prontas com trava de certificacao para rituais.",
        "",
        f"- Certified rituais: {len(certified)}",
        f"- Rejected candidates: {len(rejected)}",
        "",
        "## Policy",
        "",
        "- A certified ritual is locked to `rituais`.",
        "- A certified ritual cannot be duplicated in another category.",
        "- Items already locked as `regras_base`, `aprimoramentos`, `kits`, `classes`, `racas`, `linhagens`, `poderes` or `magias` are rejected here.",
        "- Kit/class stat blocks and generic ritual sections are rejected.",
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
    print(f"Certified {len(certified)} rituais; rejected {len(rejected)} candidates.")


if __name__ == "__main__":
    main()
