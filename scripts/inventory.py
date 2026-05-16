from __future__ import annotations

from common import BOOKS_DIR, INDEX_DIR, ensure_dirs, infer_category_hints, sha256_file, slugify, write_json


SUPPORTED_EXTENSIONS = {".pdf", ".docx"}


def main() -> None:
    ensure_dirs()
    sources = []
    seen_ids: set[str] = set()

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

        sources.append(
            {
                "id": source_id,
                "title": path.stem,
                "path": path.relative_to(BOOKS_DIR.parent).as_posix(),
                "extension": path.suffix.lower(),
                "sizeBytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "categoryHints": infer_category_hints(path.stem),
                "textStatus": "pending",
            }
        )

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
