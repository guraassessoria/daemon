from __future__ import annotations

import argparse
import re

from common import INDEX_DIR, ROOT, TEXT_DIR, read_json, write_json


SOURCES_PATH = INDEX_DIR / "sources.json"
REPORT_PATH = INDEX_DIR / "docx-segmentation-report.json"
DEFAULT_IDS = [
    "battlemage",
    "cimeria",
    "corondor",
    "jutsu-e-um-termo-japones-para-tecnica",
    "kits-orientais",
    "principais-deuses-da-mitologia-n-u00d3rdica",
    "samurai-shodown",
    "samurai-shodown-v-move-list",
    "vantagens",
]


def normalize_existing_text(text: str) -> str:
    if "--- page " not in text:
        return text.strip()

    chunks = []
    for part in re.split(r"--- page \d+ ---", text):
        stripped = part.strip()
        if stripped:
            chunks.append(stripped)
    return "\n\n".join(chunks).strip()


def split_paragraphs(text: str) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n+", text) if part.strip()]
    if len(paragraphs) > 1:
        return paragraphs

    # Some converted documents lost paragraph breaks. Add conservative breaks
    # before common heading-like tokens without changing the text itself.
    fallback = re.sub(r"(?<=[.!?])\s+(?=[A-ZÁÀÃÂÉÊÍÓÔÕÚÇ][^.!?]{0,70}:)", "\n\n", text)
    return [part.strip() for part in fallback.split("\n\n") if part.strip()]


def is_heading(paragraph: str) -> bool:
    clean = " ".join(paragraph.split())
    if not clean or len(clean) > 90:
        return False
    if clean.endswith(":"):
        return True
    words = clean.split()
    if len(words) <= 7 and sum(char.isalpha() for char in clean) >= 4:
        uppercase = sum(1 for char in clean if char.isupper())
        letters = sum(1 for char in clean if char.isalpha())
        return letters > 0 and uppercase / letters > 0.6
    return False


def segment_text(text: str, target_chars: int, max_chars: int, min_heading_chars: int) -> list[str]:
    pages: list[str] = []
    current: list[str] = []
    current_chars = 0

    for paragraph in split_paragraphs(text):
        paragraph_len = len(paragraph)
        should_break_for_heading = (
            current
            and current_chars >= min_heading_chars
            and is_heading(paragraph)
        )
        should_break_for_size = current and current_chars + paragraph_len > target_chars

        if should_break_for_heading or should_break_for_size:
            pages.append("\n\n".join(current).strip())
            current = []
            current_chars = 0

        if paragraph_len > max_chars:
            sentences = re.split(r"(?<=[.!?])\s+", paragraph)
            for sentence in sentences:
                if current and current_chars + len(sentence) > target_chars:
                    pages.append("\n\n".join(current).strip())
                    current = []
                    current_chars = 0
                current.append(sentence)
                current_chars += len(sentence) + 2
            continue

        current.append(paragraph)
        current_chars += paragraph_len + 2

    if current:
        pages.append("\n\n".join(current).strip())
    return pages


def wrap_long_paragraphs(text: str, max_line_chars: int) -> str:
    wrapped = []
    for paragraph in text.split("\n\n"):
        if len(paragraph) <= max_line_chars:
            wrapped.append(paragraph)
            continue
        lines = []
        current = ""
        for sentence in re.split(r"(?<=[.!?])\s+", paragraph):
            if current and len(current) + len(sentence) + 1 > max_line_chars:
                lines.append(current.strip())
                current = ""
            current = f"{current} {sentence}".strip()
        if current:
            lines.append(current.strip())
        wrapped.append("\n".join(lines))
    return "\n\n".join(wrapped)


def with_page_markers(pages: list[str], max_line_chars: int) -> str:
    return "\n\n".join(
        f"--- page {index} ---\n{wrap_long_paragraphs(page.strip(), max_line_chars)}"
        for index, page in enumerate(pages, start=1)
    ).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", default=DEFAULT_IDS)
    parser.add_argument("--target-chars", type=int, default=3500)
    parser.add_argument("--max-chars", type=int, default=5200)
    parser.add_argument("--max-line-chars", type=int, default=650)
    parser.add_argument("--min-heading-chars", type=int, default=1200)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    index = read_json(SOURCES_PATH, {"sources": []})
    by_id = {source["id"]: source for source in index.get("sources", [])}
    report = {"version": 1, "sources": []}

    for source_id in args.ids:
        source = by_id.get(source_id)
        text_path = TEXT_DIR / f"{source_id}.txt"
        if not source or not text_path.exists():
            report["sources"].append({"id": source_id, "status": "missing"})
            continue

        before = text_path.read_text(encoding="utf-8", errors="ignore")
        clean_text = normalize_existing_text(before)
        pages = segment_text(clean_text, args.target_chars, args.max_chars, args.min_heading_chars)
        after = with_page_markers(pages, args.max_line_chars)

        row = {
            "id": source_id,
            "status": "dry_run" if args.dry_run else "written",
            "charsBefore": len(clean_text),
            "charsAfter": len(after),
            "pagesBefore": before.count("--- page ") or 1,
            "pagesAfter": len(pages),
            "avgCharsPerPage": round(len(clean_text) / max(1, len(pages)), 2),
        }
        report["sources"].append(row)

        if not args.dry_run:
            text_path.write_text(after, encoding="utf-8")
            source["pageCount"] = len(pages)
            source["textStatus"] = "ok"

        print(
            f"{source_id}: {row['pagesBefore']} -> {row['pagesAfter']} pages "
            f"avg={row['avgCharsPerPage']}"
        )

    if not args.dry_run:
        write_json(SOURCES_PATH, index)
    write_json(REPORT_PATH, report)
    print(f"Docx segmentation report written to {REPORT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
