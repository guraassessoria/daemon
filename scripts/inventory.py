from __future__ import annotations

from typing import Any

from common import BOOKS_DIR, INDEX_DIR, ensure_dirs, infer_category_hints, read_json, sha256_file, slugify, write_json


SUPPORTED_EXTENSIONS = {".pdf", ".docx"}
PRESERVED_FIELDS = ("textStatus", "pageCount", "textError", "categoryHints")


def previous_sources() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    payload = read_json(INDEX_DIR / "sources.json", {"sources": []})
    by_id: dict[str, dict[str, Any]] = {}
    by_sha: dict[str, dict[str, Any]] = {}
    for source in payload.get("sources", []):
        if not isinstance(source, dict):
            continue
        source_id = source.get("id")
        sha256 = source.get("sha256")
        if isinstance(source_id, str):
            by_id[source_id] = source
        if isinstance(sha256, str):
            by_sha[sha256] = source
    return by_id, by_sha


def preserved_metadata(
    source_id: str,
    title: str,
    path: str,
    sha256: str,
    previous_by_id: dict[str, dict[str, Any]],
    previous_by_sha: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    previous = previous_by_id.get(source_id) or previous_by_sha.get(sha256)
    if not previous:
        return {"categoryHints": infer_category_hints(title), "textStatus": "pending"}
    if previous.get("sha256") != sha256 or previous.get("path") != path:
        return {"categoryHints": infer_category_hints(title), "textStatus": "pending"}
    return {field: previous[field] for field in PRESERVED_FIELDS if field in previous}


def main() -> None:
    ensure_dirs()
    sources = []
    seen_ids: set[str] = set()
    previous_by_id, previous_by_sha = previous_sources()

    for path in sorted(BOOKS_DIR.iterdir(), key=lambda item: item.name.casefold()):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        base_id = slugify(path.stem)
        source_id = base_id
        counter = 2
        while source_id in seen_ids:
            source_id = f"{base_id}-{counter}"
            counter += 1
        seen_ids.add(source_id)

        relative_path = path.relative_to(BOOKS_DIR.parent).as_posix()
        sha256 = sha256_file(path)
        metadata = preserved_metadata(source_id, path.stem, relative_path, sha256, previous_by_id, previous_by_sha)
        source = {
            "id": source_id,
            "title": path.stem,
            "path": relative_path,
            "extension": path.suffix.lower(),
            "sizeBytes": path.stat().st_size,
            "sha256": sha256,
            "categoryHints": metadata.get("categoryHints", infer_category_hints(path.stem)),
            "textStatus": metadata.get("textStatus", "pending"),
        }
        for field in ("pageCount", "textError"):
            if field in metadata:
                source[field] = metadata[field]
        sources.append(source)

    write_json(
        INDEX_DIR / "sources.json",
        {
            "version": 1,
            "count": len(sources),
            "sources": sources,
        },
    )
    print(f"Indexed {len(sources)} sources.")


if __name__ == "__main__":
    main()
