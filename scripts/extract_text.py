from __future__ import annotations

import argparse
import traceback
import zipfile
from pathlib import Path
from xml.etree import ElementTree

from common import BOOKS_DIR, INDEX_DIR, TEXT_DIR, ensure_dirs, read_json, write_json


def extract_pdf(path: Path) -> tuple[str, int | None]:
    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError("PyMuPDF nao instalado. Rode: python -m pip install -r requirements.txt") from exc

    chunks: list[str] = []
    with fitz.open(path) as document:
        for index, page in enumerate(document, start=1):
            text = page.get_text("text")
            chunks.append(f"\n\n--- page {index} ---\n{text}")
        return "".join(chunks).strip(), document.page_count


def extract_docx(path: Path) -> tuple[str, int | None]:
    paragraphs: list[str] = []
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(path) as archive:
        with archive.open("word/document.xml") as file:
            root = ElementTree.parse(file).getroot()

    for paragraph in root.findall(".//w:p", namespace):
        parts = [node.text or "" for node in paragraph.findall(".//w:t", namespace)]
        text = "".join(parts).strip()
        if text:
            paragraphs.append(text)
    return "\n\n".join(paragraphs), None


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from indexed PDF/DOCX sources.")
    parser.add_argument("--force", action="store_true", help="Re-extract text even when data/text already exists.")
    parser.add_argument("--ids", nargs="*", help="Optional source ids to extract.")
    args = parser.parse_args()

    ensure_dirs()
    index_path = INDEX_DIR / "sources.json"
    index = read_json(index_path, {"sources": []})
    extracted = 0
    skipped = 0
    failed = 0
    wanted = set(args.ids or [])

    for source in index["sources"]:
        if wanted and source["id"] not in wanted:
            continue
        source_path = BOOKS_DIR.parent / source["path"]
        output_path = TEXT_DIR / f"{source['id']}.txt"
        if output_path.exists() and output_path.stat().st_size and not args.force:
            source["textStatus"] = "ok"
            skipped += 1
            continue

        try:
            if source["extension"] == ".pdf":
                text, page_count = extract_pdf(source_path)
            elif source["extension"] == ".docx":
                text, page_count = extract_docx(source_path)
            else:
                continue

            output_path.write_text(text, encoding="utf-8", errors="replace")
            source["textStatus"] = "ok" if text else "partial"
            source["pageCount"] = page_count
            extracted += 1
        except Exception as exc:
            source["textStatus"] = "failed"
            source["textError"] = str(exc)
            source["textTrace"] = traceback.format_exc(limit=3)
            failed += 1

    write_json(index_path, index)
    print(f"Extracted {extracted} sources; skipped {skipped}; failed {failed}.")


if __name__ == "__main__":
    main()
