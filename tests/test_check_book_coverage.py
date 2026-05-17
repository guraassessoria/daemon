from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_book_coverage import check_book, expand_pages  # noqa: E402


def test_expand_pages_accepts_single_pages_and_ranges() -> None:
    assert expand_pages([1, [3, 5]]) == {1, 3, 4, 5}


def test_check_book_reports_full_coverage(tmp_path: Path) -> None:
    path = tmp_path / "book.json"
    path.write_text(
        json.dumps({"pages": 3, "parts": [{"pages": [1, [2, 3]]}]}),
        encoding="utf-8",
    )

    ok, message = check_book(path)

    assert ok is True
    assert "full coverage" in message


def test_check_book_reports_missing_pages(tmp_path: Path) -> None:
    path = tmp_path / "book.json"
    path.write_text(
        json.dumps({"pages": 3, "parts": [{"pages": [1]}]}),
        encoding="utf-8",
    )

    ok, message = check_book(path)

    assert ok is False
    assert "missing=[2, 3]" in message
