from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import extract_text  # noqa: E402
from common import read_json, write_json  # noqa: E402


def test_extract_text_skips_existing_file_without_force(monkeypatch, tmp_path: Path) -> None:
    books_dir = tmp_path / "Livros"
    text_dir = tmp_path / "data" / "text"
    index_dir = tmp_path / "data" / "index"
    books_dir.mkdir(parents=True)
    text_dir.mkdir(parents=True)
    index_dir.mkdir(parents=True)
    (text_dir / "book.txt").write_text("existing", encoding="utf-8")
    (books_dir / "book.docx").write_text("unused", encoding="utf-8")

    write_json(
        index_dir / "sources.json",
        {
            "sources": [
                {
                    "id": "book",
                    "path": "Livros/book.docx",
                    "extension": ".docx",
                }
            ]
        },
    )

    def fail_extract(_path: Path) -> tuple[str, int | None]:
        raise AssertionError("extract_docx should not be called")

    monkeypatch.setattr(extract_text, "BOOKS_DIR", books_dir)
    monkeypatch.setattr(extract_text, "TEXT_DIR", text_dir)
    monkeypatch.setattr(extract_text, "INDEX_DIR", index_dir)
    monkeypatch.setattr(extract_text, "extract_docx", fail_extract)
    monkeypatch.setattr(sys, "argv", ["extract_text.py"])

    extract_text.main()

    source = read_json(index_dir / "sources.json", {"sources": []})["sources"][0]
    assert source["textStatus"] == "ok"


def test_extract_text_force_reextracts_existing_file(monkeypatch, tmp_path: Path) -> None:
    books_dir = tmp_path / "Livros"
    text_dir = tmp_path / "data" / "text"
    index_dir = tmp_path / "data" / "index"
    books_dir.mkdir(parents=True)
    text_dir.mkdir(parents=True)
    index_dir.mkdir(parents=True)
    (text_dir / "book.txt").write_text("existing", encoding="utf-8")
    (books_dir / "book.docx").write_text("unused", encoding="utf-8")

    write_json(
        index_dir / "sources.json",
        {
            "sources": [
                {
                    "id": "book",
                    "path": "Livros/book.docx",
                    "extension": ".docx",
                }
            ]
        },
    )

    monkeypatch.setattr(extract_text, "BOOKS_DIR", books_dir)
    monkeypatch.setattr(extract_text, "TEXT_DIR", text_dir)
    monkeypatch.setattr(extract_text, "INDEX_DIR", index_dir)
    monkeypatch.setattr(extract_text, "extract_docx", lambda _path: ("new text", None))
    monkeypatch.setattr(sys, "argv", ["extract_text.py", "--force"])

    extract_text.main()

    assert (text_dir / "book.txt").read_text(encoding="utf-8") == "new text"
