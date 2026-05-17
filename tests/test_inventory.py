from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from inventory import preserved_metadata  # noqa: E402


def test_preserved_metadata_keeps_extraction_fields_when_source_is_unchanged() -> None:
    previous = {
        "book": {
            "id": "book",
            "path": "Livros/book.pdf",
            "sha256": "abc",
            "categoryHints": ["core_rule"],
            "textStatus": "ok",
            "pageCount": 10,
        }
    }

    assert preserved_metadata("book", "Book", "Livros/book.pdf", "abc", previous, {}) == {
        "textStatus": "ok",
        "pageCount": 10,
        "categoryHints": ["core_rule"],
    }


def test_preserved_metadata_resets_when_hash_changes() -> None:
    previous = {
        "book": {
            "id": "book",
            "path": "Livros/book.pdf",
            "sha256": "old",
            "categoryHints": ["core_rule"],
            "textStatus": "ok",
            "pageCount": 10,
        }
    }

    metadata = preserved_metadata("book", "Book", "Livros/book.pdf", "new", previous, {})

    assert metadata["textStatus"] == "pending"
    assert "pageCount" not in metadata
