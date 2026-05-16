from __future__ import annotations

from collections import Counter

from common import INDEX_DIR, TEXT_DIR, infer_category_hints, read_json, write_json


def main() -> None:
    index_path = INDEX_DIR / "sources.json"
    index = read_json(index_path, {"sources": []})
    category_counts: Counter[str] = Counter()

    for source in index["sources"]:
        text_path = TEXT_DIR / f"{source['id']}.txt"
        basis = source["title"]
        if text_path.exists():
            sample = text_path.read_text(encoding="utf-8", errors="ignore")[:20000]
            basis = f"{basis}\n{sample}"

        hints = infer_category_hints(basis)
        source["categoryHints"] = hints
        for hint in hints:
            category_counts[hint] += 1

    write_json(index_path, index)
    write_json(
        INDEX_DIR / "category-summary.json",
        {
            "version": 1,
            "counts": dict(category_counts.most_common()),
        },
    )
    print("Updated category hints.")


if __name__ == "__main__":
    main()
