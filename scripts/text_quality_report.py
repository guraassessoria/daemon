from __future__ import annotations

import re
from statistics import mean

from common import INDEX_DIR, TEXT_DIR, read_json, write_json


SOURCES_PATH = INDEX_DIR / "sources.json"
REPORT_PATH = INDEX_DIR / "text-quality.json"
DUPLICATES_PATH = INDEX_DIR / "duplicates.json"


MOJIBAKE_MARKERS = ["Ã", "Â", "â€", "�", "\ufffd"]


def split_pages(text: str) -> dict[int, str]:
    pages: dict[int, str] = {}
    matches = list(re.finditer(r"--- page (\d+) ---", text))
    if not matches:
        stripped = text.strip()
        return {1: stripped} if stripped else {}

    for index, match in enumerate(matches):
        page = int(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        pages[page] = text[start:end].strip()
    return pages


def count_weird_chars(text: str) -> int:
    marker_hits = sum(text.count(marker) for marker in MOJIBAKE_MARKERS)
    control_hits = sum(1 for char in text if ord(char) < 32 and char not in "\n\r\t")
    replacement_hits = text.count("\ufffd")
    return marker_hits + control_hits + replacement_hits


def classify(source: dict, pages: dict[int, str], text: str) -> tuple[str, list[str]]:
    page_count = int(source.get("pageCount") or max(pages.keys(), default=1))
    empty_pages = sum(1 for page in range(1, page_count + 1) if len(pages.get(page, "").strip()) < 20)
    char_counts = [len(pages.get(page, "")) for page in range(1, page_count + 1)]
    avg_chars = mean(char_counts) if char_counts else 0
    total_chars = len(text.strip())
    weird_chars = count_weird_chars(text)
    weird_ratio = weird_chars / max(1, total_chars)

    flags: list[str] = []
    if page_count > 1 and empty_pages / page_count >= 0.5:
        flags.append("many_empty_pages")
    if avg_chars < 120 and page_count > 1:
        flags.append("low_text_density")
    if total_chars < 100 and page_count > 1:
        flags.append("almost_no_text")
    if weird_ratio > 0.01:
        flags.append("encoding_or_ocr_noise")
    if any(len(pages.get(page, "")) > 20000 for page in pages):
        flags.append("layout_extraction_blob")

    if "almost_no_text" in flags or ("many_empty_pages" in flags and "low_text_density" in flags):
        return "needs_ocr", flags
    if flags:
        return "review", flags
    return "ok", flags


def main() -> None:
    index = read_json(SOURCES_PATH, {"sources": []})
    duplicates_payload = read_json(DUPLICATES_PATH, {"duplicates": []})
    duplicates = {row["duplicate"]: row["canonical"] for row in duplicates_payload.get("duplicates", [])}
    reports = []
    summary = {"ok": 0, "review": 0, "needs_ocr": 0, "missing_text_file": 0, "duplicate": 0}

    for source in index["sources"]:
        if source["id"] in duplicates:
            summary["duplicate"] += 1
            reports.append(
                {
                    "id": source["id"],
                    "title": source["title"],
                    "extension": source.get("extension"),
                    "pages": source.get("pageCount"),
                    "status": "duplicate",
                    "flags": ["duplicate_source"],
                    "canonical": duplicates[source["id"]],
                }
            )
            continue

        text_path = TEXT_DIR / f"{source['id']}.txt"
        if not text_path.exists():
            summary["missing_text_file"] += 1
            reports.append(
                {
                    "id": source["id"],
                    "title": source["title"],
                    "status": "missing_text_file",
                    "flags": ["missing_text_file"],
                }
            )
            continue

        text = text_path.read_text(encoding="utf-8", errors="ignore")
        pages = split_pages(text)
        page_count = int(source.get("pageCount") or max(pages.keys(), default=1))
        char_counts = [len(pages.get(page, "")) for page in range(1, page_count + 1)]
        empty_pages = sum(1 for count in char_counts if count < 20)
        total_chars = len(text.strip())
        weird_chars = count_weird_chars(text)
        status, flags = classify(source, pages, text)
        summary[status] += 1

        reports.append(
            {
                "id": source["id"],
                "title": source["title"],
                "extension": source.get("extension"),
                "pages": page_count,
                "status": status,
                "flags": flags,
                "totalChars": total_chars,
                "avgCharsPerPage": round(mean(char_counts), 2) if char_counts else 0,
                "emptyPages": empty_pages,
                "emptyPageRatio": round(empty_pages / max(1, page_count), 4),
                "weirdChars": weird_chars,
                "weirdCharRatio": round(weird_chars / max(1, total_chars), 6),
            }
        )

    reports.sort(key=lambda item: ({"needs_ocr": 0, "review": 1, "ok": 2, "duplicate": 3, "missing_text_file": 4}.get(item["status"], 9), item["id"]))
    write_json(REPORT_PATH, {"version": 1, "summary": summary, "sources": reports})

    print("Text quality report written to data/index/text-quality.json")
    print(summary)
    for row in reports[:30]:
        if row["status"] != "ok":
            print(f"{row['status']:9} {row['id']} pages={row.get('pages')} avg={row.get('avgCharsPerPage')} empty={row.get('emptyPages')} flags={','.join(row.get('flags', []))}")


if __name__ == "__main__":
    main()
