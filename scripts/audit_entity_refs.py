from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, read_json, write_json


REPORT_JSON = INDEX_DIR / "entity-ref-integrity.json"
REPORT_MD = ROOT / "docs" / "reports" / "entity-ref-integrity.md"


def entity_records(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key in ("entities", "items", "records"):
            records = payload.get(key)
            if isinstance(records, list):
                return [item for item in records if isinstance(item, dict)]
    return []


def collect_entity_ids() -> dict[str, list[str]]:
    by_id: dict[str, list[str]] = defaultdict(list)
    for path in sorted((DATA_DIR / "entities").glob("*.json")):
        for index, entity in enumerate(entity_records(read_json(path, []))):
            entity_id = entity.get("id")
            if entity_id:
                by_id[str(entity_id)].append(f"{path.relative_to(ROOT)}#{index}")
    return by_id


def collect_refs(paths: list[Path]) -> list[dict[str, Any]]:
    refs: list[dict[str, Any]] = []

    def walk(value: Any, path: Path, context: str) -> None:
        if isinstance(value, dict):
            entity_refs = value.get("entityRefs")
            if isinstance(entity_refs, list):
                seen: set[str] = set()
                for ref in entity_refs:
                    ref_id = str(ref)
                    refs.append(
                        {
                            "ref": ref_id,
                            "file": str(path.relative_to(ROOT)),
                            "context": context,
                            "duplicatedInSameBlock": ref_id in seen,
                            "ownerId": value.get("id"),
                            "ownerName": value.get("name") or value.get("title"),
                        }
                    )
                    seen.add(ref_id)
            for key, child in value.items():
                walk(child, path, f"{context}/{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, path, f"{context}[{index}]")

    for path in paths:
        walk(read_json(path, {}), path, "")
    return refs


def build_report() -> dict[str, Any]:
    entity_id_locations = collect_entity_ids()
    duplicate_ids = {
        entity_id: locations
        for entity_id, locations in sorted(entity_id_locations.items())
        if len(locations) > 1
    }
    published_paths = sorted((DATA_DIR / "areas").glob("*.json"))
    book_paths = sorted((DATA_DIR / "books").glob("*.json"))
    published_refs = collect_refs(published_paths)
    book_refs = collect_refs(book_paths)
    valid_ids = set(entity_id_locations)
    broken_published = [row for row in published_refs if row["ref"] not in valid_ids]
    broken_books = [row for row in book_refs if row["ref"] not in valid_ids]
    duplicate_ref_blocks = [row for row in [*published_refs, *book_refs] if row["duplicatedInSameBlock"]]
    payload = {
        "version": 1,
        "summary": {
            "entityIdCount": len(entity_id_locations),
            "duplicateGlobalIdCount": len(duplicate_ids),
            "publishedRefCount": len(published_refs),
            "brokenPublishedRefCount": len(broken_published),
            "bookRefCount": len(book_refs),
            "brokenBookRefCount": len(broken_books),
            "duplicateRefInSameBlockCount": len(duplicate_ref_blocks),
        },
        "duplicateGlobalIds": duplicate_ids,
        "brokenPublishedRefs": broken_published,
        "brokenBookRefsTop": [
            {"ref": ref, "count": count}
            for ref, count in Counter(row["ref"] for row in broken_books).most_common(200)
        ],
        "duplicateRefsInSameBlock": duplicate_ref_blocks[:300],
    }
    return payload


def write_markdown(payload: dict[str, Any]) -> None:
    summary = payload["summary"]
    lines = [
        "# Auditoria de referências cruzadas",
        "",
        "Este relatório separa o que está publicado nas áreas do site do que ainda existe como referência bruta nos livros processados.",
        "",
        "## Resumo",
        "",
        f"- IDs de entidade: {summary['entityIdCount']}",
        f"- IDs globais duplicados: {summary['duplicateGlobalIdCount']}",
        f"- Referências publicadas: {summary['publishedRefCount']}",
        f"- Referências publicadas quebradas: {summary['brokenPublishedRefCount']}",
        f"- Referências brutas nos livros: {summary['bookRefCount']}",
        f"- Referências brutas quebradas nos livros: {summary['brokenBookRefCount']}",
        f"- Referências duplicadas no mesmo bloco: {summary['duplicateRefInSameBlockCount']}",
        "",
        "## IDs globais duplicados",
        "",
    ]
    if not payload["duplicateGlobalIds"]:
        lines.append("Nenhum.")
    else:
        for entity_id, locations in payload["duplicateGlobalIds"].items():
            lines.append(f"- `{entity_id}`: {', '.join(locations)}")
    lines.extend(["", "## Referências publicadas quebradas", ""])
    if not payload["brokenPublishedRefs"]:
        lines.append("Nenhuma.")
    else:
        for row in payload["brokenPublishedRefs"][:100]:
            lines.append(f"- `{row['ref']}` em `{row['file']}` / `{row.get('ownerId')}`")
    lines.extend(["", "## Principais referências brutas quebradas nos livros", ""])
    if not payload["brokenBookRefsTop"]:
        lines.append("Nenhuma.")
    else:
        for row in payload["brokenBookRefsTop"][:60]:
            lines.append(f"- `{row['ref']}`: {row['count']} ocorrência(s)")
    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    payload = build_report()
    write_json(REPORT_JSON, payload)
    write_markdown(payload)
    print("Entity reference integrity report written.")
    print(payload["summary"])


if __name__ == "__main__":
    main()
