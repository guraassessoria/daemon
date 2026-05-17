from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


BOOKS_DATA_DIR = DATA_DIR / "books"
WORK_DIR = DATA_DIR / "work"
DOCS_DIR = ROOT / "docs" / "reports" / "audits"

AREAS = {
    "aprimoramentos": {
        "label": "Aprimoramentos",
        "lock": "aprimoramentos-certified-lock.json",
        "rejected": "aprimoramentos-certification-rejected.json",
        "entity_file": "character_option_granular.json",
        "categories": {"character_option"},
        "keywords": ("aprimoramento", "aprimoramentos", "vantagem", "desvantagem", "talento"),
        "strong": re.compile(r"\b\d+\s+pontos?\b|\b-\d+\s+pontos?\b|\bCusto\s*:", re.IGNORECASE),
    },
    "kits": {
        "label": "Kits",
        "lock": "kits-certified-lock.json",
        "rejected": "kits-certification-rejected.json",
        "entity_file": "kit_class_granular.json",
        "categories": {"kit_class"},
        "keywords": ("kit", "kits"),
        "strong": re.compile(r"\bCustos?\s*:|\bPer[ií]cias?\s*:|\bAprimoramentos?\s*:|\bPontos Her[oó]icos\b", re.IGNORECASE),
    },
    "classes": {
        "label": "Classes",
        "lock": "classes-certified-lock.json",
        "rejected": "classes-certification-rejected.json",
        "entity_file": "class_granular.json",
        "categories": {"character_class"},
        "keywords": ("classe", "classes", "profissao", "profissoes", "ocupacao", "arquetipo", "caminho"),
        "strong": re.compile(r"\bCustos?\s*:|\bPer[ií]cias?\s*:|\bAprimoramentos?\s*:|\bAtributos Principais\s*:", re.IGNORECASE),
    },
    "racas": {
        "label": "Racas",
        "lock": "racas-certified-lock.json",
        "rejected": "racas-certification-rejected.json",
        "entity_file": "race_lineage_granular.json",
        "categories": {"race_lineage"},
        "keywords": ("raca", "racas", "especie", "especies", "elfo", "anao", "orc"),
        "strong": re.compile(r"\bCusto\s*:|\bIdade Inicial\s*:|\bAtributos\s*:|\bVantagens\s*:|\bDesvantagens\s*:", re.IGNORECASE),
    },
    "linhagens": {
        "label": "Linhagens",
        "lock": "linhagens-certified-lock.json",
        "rejected": "racas-certification-rejected.json",
        "entity_file": "race_lineage_granular.json",
        "categories": {"race_lineage"},
        "keywords": ("linhagem", "linhagens", "vampiro", "youkai", "imortal", "fera", "lobisomem"),
        "strong": re.compile(r"\blinhagens?\b|\bvampiros?\b|\byoukais?\b|\bimortais?\b|\bferas?\b|\blobisomens?\b", re.IGNORECASE),
    },
    "poderes": {
        "label": "Poderes",
        "lock": "poderes-certified-lock.json",
        "rejected": "poderes-magias-certification-rejected.json",
        "entity_file": "power_magic_granular.json",
        "categories": {"power_magic"},
        "keywords": ("poder", "poderes", "superpoder", "psiquismo", "milagre", "reiatsu"),
        "strong": re.compile(r"\bCustos?\s*:|\bN[ií]vel\s*\d+\s*:|\bPontos? de Poder\b|\bPontos? de F[eé]\b", re.IGNORECASE),
    },
    "magias": {
        "label": "Magias",
        "lock": "magias-certified-lock.json",
        "rejected": "poderes-magias-certification-rejected.json",
        "entity_file": "power_magic_granular.json",
        "categories": {"power_magic"},
        "keywords": ("magia", "magias", "caminho", "caminhos", "focus", "feitico"),
        "strong": re.compile(r"\bC[ií]rculos?\b|\bEntender\s*-|\bCriar\s*-|\bControlar\s*-|\bFocus\b|\bDura[cç][aã]o\s*:|\bEfeito\s*:", re.IGNORECASE),
    },
}

EXCLUDE_REASONS = {
    "duplicate_certification_key",
    "duplicate_certification_content",
    "entry_too_short",
    "lineage_entry_too_short",
    "name_has_sentence_punctuation",
    "name_is_broken_sentence",
    "name_is_section_or_empty",
    "name_looks_like_section_heading",
    "name_starts_with_broken_marker",
    "source_is_aprimoramento",
    "subtype_is_not_poder_or_magia",
    "subtype_is_not_raca_or_linhagem",
}


def normalize(value: str) -> str:
    return slugify(value).replace("-", " ")


def body_text(entity: dict[str, Any]) -> str:
    return "\n".join(entry for entry in entity.get("entries", []) if isinstance(entry, str))


def ready_source_ids() -> list[str]:
    summary = read_json(INDEX_DIR / "area-summary.json", {"readySources": []})
    return sorted(summary.get("readySources", []))


def lock_records(area: str) -> list[dict[str, Any]]:
    return read_json(INDEX_DIR / AREAS[area]["lock"], {"records": []}).get("records", [])


def certified_source_counts() -> dict[str, Counter[str]]:
    counts: dict[str, Counter[str]] = {}
    for area in AREAS:
        counts[area] = Counter(record.get("source") for record in lock_records(area) if record.get("source"))
    return counts


def rejected_candidates(area: str) -> list[dict[str, Any]]:
    config = AREAS[area]
    rejected = read_json(WORK_DIR / config["rejected"], [])
    if not isinstance(rejected, list):
        return []
    result: list[dict[str, Any]] = []
    for entity in rejected:
        if area in {"poderes", "magias"} and entity.get("subtype") != ("poder" if area == "poderes" else "magia"):
            continue
        if area == "racas" and entity.get("subtype") != "raca":
            continue
        if area == "linhagens" and entity.get("subtype") != "linhagem":
            continue
        reason = entity.get("rejectionReason")
        if not reason or reason in EXCLUDE_REASONS or str(reason).startswith("locked_as_"):
            continue
        body = body_text(entity)
        strong = bool(config["strong"].search(body[:1800]))
        if not strong and reason.startswith("no_mechanical_"):
            continue
        result.append(
            {
                "id": entity.get("id"),
                "name": entity.get("name"),
                "source": entity.get("source"),
                "page": entity.get("page"),
                "rejectionReason": reason,
                "strongSignal": strong,
                "excerpt": re.sub(r"\s+", " ", body).strip()[:240],
            }
        )
    return result


def quarantine_candidates(area: str) -> list[dict[str, Any]]:
    path = WORK_DIR / f"{area}-quarantine.json"
    data = read_json(path, [])
    if not isinstance(data, list):
        return []
    return data


def book_part_gap_candidates(area: str, source_counts: dict[str, Counter[str]]) -> list[dict[str, Any]]:
    config = AREAS[area]
    ready_sources = set(ready_source_ids())
    candidates: list[dict[str, Any]] = []
    for source_id in ready_sources:
        path = BOOKS_DATA_DIR / f"{source_id}.json"
        if not path.exists():
            continue
        book = read_json(path, {})
        for part in book.get("parts", []):
            haystack = normalize(" ".join([part.get("name", ""), part.get("summary", ""), part.get("id", "")]))
            category_hit = part.get("category") in config["categories"]
            keyword_hits = [keyword for keyword in config["keywords"] if normalize(keyword) in haystack]
            strong = bool(config["strong"].search(" ".join([part.get("name", ""), part.get("summary", "")])[:1800]))
            if not category_hit and not keyword_hits:
                continue
            if source_counts[area].get(source_id, 0) and not strong:
                continue
            if not strong and len(keyword_hits) < 2 and not category_hit:
                continue
            candidates.append(
                {
                    "source": source_id,
                    "partId": part.get("id"),
                    "name": part.get("name"),
                    "category": part.get("category"),
                    "pages": part.get("pages", []),
                    "sourceCertifiedCount": source_counts[area].get(source_id, 0),
                    "keywordHits": keyword_hits[:8],
                    "strongSignal": strong,
                    "summary": re.sub(r"\s+", " ", part.get("summary", "")).strip()[:260],
                }
            )
    return candidates


def published_cross_area_hits() -> dict[str, list[dict[str, Any]]]:
    area_by_id: dict[str, str] = {}
    for area in AREAS:
        for record in lock_records(area):
            if record.get("id"):
                area_by_id[record["id"]] = area

    hits: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in (DATA_DIR / "areas").glob("*.json"):
        payload = read_json(path, {})
        area_id = path.stem
        for entity in payload.get("entities", []):
            entity_id = entity.get("id")
            locked_area = area_by_id.get(entity_id)
            if locked_area and locked_area != area_id:
                hits[locked_area].append(
                    {
                        "id": entity_id,
                        "name": entity.get("name"),
                        "publishedArea": area_id,
                        "lockedArea": locked_area,
                    }
                )
    return dict(hits)


def main() -> None:
    source_counts = certified_source_counts()
    cross_area_hits = published_cross_area_hits()
    report: dict[str, Any] = {
        "version": 1,
        "areas": {},
        "crossAreaHits": cross_area_hits,
    }

    for area, config in AREAS.items():
        rejected = rejected_candidates(area)
        quarantine = quarantine_candidates(area)
        source_parts = book_part_gap_candidates(area, source_counts)
        lock = read_json(INDEX_DIR / config["lock"], {"records": []})
        report["areas"][area] = {
            "label": config["label"],
            "certifiedCount": lock.get("certifiedCount", len(lock.get("records", []))),
            "quarantineCount": len(quarantine),
            "duplicateCount": len(read_json(WORK_DIR / f"{area}-duplicate-blocks.json", [])),
            "rejectedReviewCount": len(rejected),
            "sourcePartReviewCount": len(source_parts),
            "quarantine": quarantine[:80],
            "rejectedReview": sorted(rejected, key=lambda item: (not item["strongSignal"], item.get("source") or "", item.get("name") or ""))[:120],
            "sourcePartReview": sorted(
                source_parts,
                key=lambda item: (item["sourceCertifiedCount"] > 0, not item["strongSignal"], item.get("source") or "", item.get("name") or ""),
            )[:120],
        }

    write_json(INDEX_DIR / "certified-category-gap-audit.json", report)

    lines = [
        "# Certified category gap audit",
        "",
        "Pente fino das areas ja certificadas antes de seguir para novas categorias.",
        "",
        "Areas auditadas: `aprimoramentos`, `kits`, `classes`, `racas`, `linhagens`, `poderes` e `magias`.",
        "",
        "## Resumo",
        "",
        "| Area | Certificados | Quarentena | Rejeitados para revisar | Partes de livro para revisar |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for area, payload in report["areas"].items():
        lines.append(
            f"| {payload['label']} (`{area}`) | {payload['certifiedCount']} | {payload['quarantineCount']} | "
            f"{payload['rejectedReviewCount']} | {payload['sourcePartReviewCount']} |"
        )
    lines.extend(["", "## Publicacao cruzada", ""])
    if cross_area_hits:
        for area, hits in cross_area_hits.items():
            lines.append(f"- `{area}`: {len(hits)} item(ns) publicados fora da area travada.")
    else:
        lines.append("- Nenhum item certificado foi encontrado publicado em area diferente da trava.")

    for area, payload in report["areas"].items():
        lines.extend(["", f"## {payload['label']}", ""])
        if payload["quarantine"]:
            lines.append("### Quarentena")
            for item in payload["quarantine"][:25]:
                lines.append(f"- `{item.get('source')}` / `{item.get('name')}`: {item.get('reason')}")
            lines.append("")
        if payload["rejectedReview"]:
            lines.append("### Rejeitados com sinal para revisao")
            for item in payload["rejectedReview"][:30]:
                marker = "forte" if item["strongSignal"] else "medio"
                lines.append(f"- `{item.get('source')}` / `{item.get('name')}` ({marker}): {item.get('rejectionReason')}")
            lines.append("")
        if payload["sourcePartReview"]:
            lines.append("### Partes de livro candidatas")
            for item in payload["sourcePartReview"][:30]:
                coverage = item["sourceCertifiedCount"]
                lines.append(
                    f"- `{item.get('source')}` / `{item.get('name')}`: categoria `{item.get('category')}`, "
                    f"certificados na fonte={coverage}, sinais={', '.join(item.get('keywordHits') or []) or '-'}"
                )
            lines.append("")
        if not payload["quarantine"] and not payload["rejectedReview"] and not payload["sourcePartReview"]:
            lines.append("- Nenhuma lacuna forte encontrada nesta passada.")

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "certified-category-gap-audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Certified category gap audit written.")


if __name__ == "__main__":
    main()
