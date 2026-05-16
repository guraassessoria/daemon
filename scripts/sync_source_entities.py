from __future__ import annotations

import argparse
from pathlib import Path

from common import ROOT, read_json, write_json


SOURCES_PATH = ROOT / "data" / "index" / "sources.json"
BOOKS_META_DIR = ROOT / "data" / "books"
ENTITIES_PATH = ROOT / "data" / "entities" / "source.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--count", type=int)
    args = parser.parse_args()

    index = read_json(SOURCES_PATH, {"sources": []})
    selected = index["sources"][args.start - 1 :]
    if args.count is not None:
        selected = selected[: args.count]

    existing = {entity["id"]: entity for entity in read_json(ENTITIES_PATH, [])}
    for source in selected:
        book_path = BOOKS_META_DIR / f"{source['id']}.json"
        if not book_path.exists():
            continue
        book = read_json(book_path, {})
        categories = sorted({part.get("category", "source") for part in book.get("parts", [])})
        existing[source["id"]] = {
            "id": source["id"],
            "name": source["title"],
            "category": "source",
            "source": source["id"],
            "page": 1,
            "entries": [
                f"Fonte processada com cobertura total: {book.get('pages', source.get('pageCount'))} paginas, {len(book.get('parts', []))} partes.",
                "Categorias encontradas: " + ", ".join(categories),
            ],
            "tags": categories,
            "confidence": 1,
            "extractionMethod": book.get("status", "unknown"),
        }

    write_json(ENTITIES_PATH, [existing[key] for key in sorted(existing)])
    print(f"synced {len(selected)} source entities")


if __name__ == "__main__":
    main()
