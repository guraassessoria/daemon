from __future__ import annotations

import sys
from pathlib import Path

from common import ROOT, read_json


BOOKS_META_DIR = ROOT / "data" / "books"


def expand_pages(pages: list[int | list[int]]) -> set[int]:
    expanded: set[int] = set()
    for item in pages:
        if isinstance(item, int):
            expanded.add(item)
        elif isinstance(item, list) and len(item) == 2:
            start, end = item
            expanded.update(range(start, end + 1))
    return expanded


def check_book(path: Path) -> tuple[bool, str]:
    payload = read_json(path, {})
    page_count = payload.get("pages")
    parts = payload.get("parts", [])
    if not page_count:
        return False, f"{path.name}: missing page count"

    covered: set[int] = set()
    for part in parts:
        covered.update(expand_pages(part.get("pages", [])))

    expected = set(range(1, page_count + 1))
    missing = sorted(expected - covered)
    outside = sorted(covered - expected)
    if missing or outside:
        return False, f"{path.name}: missing={missing or '-'} outside={outside or '-'}"
    return True, f"{path.name}: full coverage ({page_count} pages)"


def main() -> None:
    targets = [BOOKS_META_DIR / arg for arg in sys.argv[1:]]
    if not targets:
        targets = sorted(BOOKS_META_DIR.glob("*.json"))

    failed = False
    for target in targets:
        ok, message = check_book(target)
        print(message)
        failed = failed or not ok

    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
