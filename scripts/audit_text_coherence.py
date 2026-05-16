from __future__ import annotations

import argparse
import re
from collections import Counter
from statistics import mean

from common import INDEX_DIR, ROOT, TEXT_DIR, read_json, write_json
from text_quality_report import split_pages


SOURCES_PATH = INDEX_DIR / "sources.json"
DUPLICATES_PATH = INDEX_DIR / "duplicates.json"
REPORT_JSON = INDEX_DIR / "text-coherence-report.json"
REPORT_MD = ROOT / "docs" / "text-coherence-report.md"

MOJIBAKE_MARKERS = ["Ã", "Â", "�", "\ufffd", "Ð", "ð", "þ", "ý"]
COMMON_PT = {
    "a", "ao", "aos", "as", "com", "como", "da", "das", "de", "do", "dos",
    "e", "em", "entre", "mais", "mas", "na", "nas", "no", "nos", "o", "os",
    "ou", "para", "por", "que", "se", "sem", "sua", "suas", "seu", "seus",
    "um", "uma", "personagem", "personagens", "sistema", "daemon", "mestre",
    "jogador", "jogadores", "teste", "pontos", "poder", "magia", "dano",
}


def duplicate_map() -> dict[str, str]:
    payload = read_json(DUPLICATES_PATH, {"duplicates": []})
    return {row["duplicate"]: row["canonical"] for row in payload.get("duplicates", [])}


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", text)


def page_marker_count(text: str) -> int:
    return len(re.findall(r"--- page \d+ ---", text))


def weird_count(text: str) -> int:
    marker_hits = sum(text.count(marker) for marker in MOJIBAKE_MARKERS)
    control_hits = sum(1 for char in text if ord(char) < 32 and char not in "\n\r\t")
    return marker_hits + control_hits


def symbol_ratio(text: str) -> float:
    stripped = text.strip()
    if not stripped:
        return 1.0
    allowed = ".,;:!?()[]{}<>/%+-ºª'\"“”‘’•·–—_#@&*=|\\/"
    symbols = sum(1 for char in stripped if not char.isalnum() and not char.isspace() and char not in allowed)
    return symbols / max(1, len(stripped))


def vowel_ratio(text_words: list[str]) -> float:
    letters = "".join(char for word in text_words for char in word if char.isalpha())
    if not letters:
        return 0
    vowels = sum(1 for char in letters.casefold() if char in "aeiouáàãâéêíóôõúü")
    return vowels / len(letters)


def common_word_ratio(text_words: list[str]) -> float:
    alpha = [word.casefold() for word in text_words if any(char.isalpha() for char in word)]
    if not alpha:
        return 0
    return sum(1 for word in alpha if word in COMMON_PT) / len(alpha)


def long_word_ratio(text_words: list[str]) -> float:
    alpha = [word for word in text_words if any(char.isalpha() for char in word)]
    if not alpha:
        return 0
    return sum(1 for word in alpha if len(word) > 28) / len(alpha)


def repeated_fragment_ratio(text: str) -> float:
    normalized = re.sub(r"\s+", " ", text.casefold())
    fragments = [
        normalized[index : index + 120]
        for index in range(0, max(0, len(normalized) - 120), 120)
    ]
    if len(fragments) < 20:
        return 0
    counts = Counter(fragments)
    repeated = sum(count for count in counts.values() if count >= 3)
    return repeated / len(fragments)


def line_anomalies(text: str) -> tuple[float, int]:
    lines = [line.strip() for line in text.splitlines() if line.strip() and not line.startswith("--- page ")]
    if not lines:
        return 1.0, 0
    very_long = sum(1 for line in lines if len(line) > 700)
    return very_long / len(lines), very_long


def sample_problem(text: str) -> str:
    candidates = []
    for line in text.splitlines():
        clean = " ".join(line.split())
        if not clean or clean.startswith("--- page "):
            continue
        score = weird_count(clean) * 3 + symbol_ratio(clean) * 100 + (10 if len(clean) > 700 else 0)
        if len(words(clean)) >= 3:
            candidates.append((score, clean[:260]))
    if not candidates:
        return ""
    return max(candidates, key=lambda item: item[0])[1]


def classify(metrics: dict) -> tuple[str, list[str]]:
    flags: list[str] = []

    if metrics["duplicate"]:
        return "duplicate", ["duplicate_source"]
    if metrics["missingText"]:
        return "critical", ["missing_text"]
    if metrics["emptyPageRatio"] >= 0.35:
        flags.append("many_empty_or_tiny_pages")
    if metrics["avgCharsPerPage"] < 150 and metrics["pages"] > 1:
        flags.append("very_low_text_density")
    if metrics["weirdRatio"] > 0.02:
        flags.append("encoding_noise")
    if metrics["symbolRatio"] > 0.03:
        flags.append("symbol_noise")
    if metrics["vowelRatio"] < 0.25 and metrics["wordCount"] > 100:
        flags.append("low_vowel_ratio")
    if metrics["commonWordRatio"] < 0.025 and metrics["wordCount"] > 250:
        flags.append("low_common_word_ratio")
    if metrics["longWordRatio"] > 0.015:
        flags.append("many_very_long_words")
    if metrics["longLineRatio"] > 0.2:
        flags.append("layout_or_linebreak_problem")
    if metrics["repeatedFragmentRatio"] > 0.08:
        flags.append("repeated_fragment_problem")

    severe = {
        "many_empty_or_tiny_pages",
        "very_low_text_density",
        "encoding_noise",
        "low_vowel_ratio",
        "repeated_fragment_problem",
    }
    if any(flag in severe for flag in flags):
        return "critical", flags
    if flags:
        return "review", flags
    return "ok", []


def audit_source(source: dict, duplicates: dict[str, str]) -> dict:
    source_id = source["id"]
    text_path = TEXT_DIR / f"{source_id}.txt"
    duplicate = source_id in duplicates
    if not text_path.exists():
        status, flags = classify({"duplicate": duplicate, "missingText": True})
        return {
            "id": source_id,
            "title": source["title"],
            "status": status,
            "flags": flags,
            "duplicate": duplicate,
            "canonical": duplicates.get(source_id),
            "missingText": True,
        }

    text = text_path.read_text(encoding="utf-8", errors="ignore")
    pages_map = split_pages(text)
    markers = page_marker_count(text)
    page_count = int(source.get("pageCount") or markers or max(pages_map.keys(), default=1))
    if not pages_map and text.strip():
        pages_map = {1: text.strip()}

    page_lengths = [len(pages_map.get(page, "").strip()) for page in range(1, page_count + 1)]
    empty_pages = sum(1 for size in page_lengths if size < 25)
    text_words = words(text)
    total = len(text.strip())
    weird = weird_count(text)
    long_line_ratio, long_line_count = line_anomalies(text)
    metrics = {
        "duplicate": duplicate,
        "missingText": False,
        "pages": page_count,
        "pageMarkers": markers,
        "totalChars": total,
        "wordCount": len(text_words),
        "avgCharsPerPage": round(mean(page_lengths), 2) if page_lengths else 0,
        "emptyPages": empty_pages,
        "emptyPageRatio": round(empty_pages / max(1, page_count), 4),
        "weirdChars": weird,
        "weirdRatio": round(weird / max(1, total), 6),
        "symbolRatio": round(symbol_ratio(text), 6),
        "vowelRatio": round(vowel_ratio(text_words), 6),
        "commonWordRatio": round(common_word_ratio(text_words), 6),
        "longWordRatio": round(long_word_ratio(text_words), 6),
        "longLineRatio": round(long_line_ratio, 6),
        "longLineCount": long_line_count,
        "repeatedFragmentRatio": round(repeated_fragment_ratio(text), 6),
    }
    status, flags = classify(metrics)
    return {
        "id": source_id,
        "title": source["title"],
        "extension": source.get("extension"),
        "status": status,
        "flags": flags,
        "canonical": duplicates.get(source_id),
        **metrics,
        "sample": sample_problem(text) if status in {"critical", "review"} else "",
    }


def write_markdown(report: dict) -> None:
    lines = [
        "# Text Coherence Report",
        "",
        "Automated audit of extracted text coherence. Duplicates are tracked separately and not counted as failures.",
        "",
        "## Summary",
        "",
    ]
    for key, value in report["summary"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Critical", ""])

    for row in report["sources"]:
        if row["status"] != "critical":
            continue
        lines.append(f"### {row['id']}")
        lines.append(f"- title: {row['title']}")
        lines.append(f"- flags: {', '.join(row.get('flags', []))}")
        lines.append(f"- chars/pages: {row.get('totalChars')} / {row.get('pages')}")
        lines.append(f"- weird ratio: {row.get('weirdRatio')} | empty pages: {row.get('emptyPages')}")
        if row.get("sample"):
            lines.append(f"- sample: `{row['sample']}`")
        lines.append("")

    lines.extend(["## Review", ""])
    for row in report["sources"]:
        if row["status"] != "review":
            continue
        lines.append(f"- {row['id']}: {', '.join(row.get('flags', []))}")

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-duplicates", action="store_true")
    args = parser.parse_args()

    index = read_json(SOURCES_PATH, {"sources": []})
    duplicates = duplicate_map()
    rows = []
    summary = {"ok": 0, "review": 0, "critical": 0, "duplicate": 0}

    for source in index.get("sources", []):
        row = audit_source(source, duplicates)
        if row["status"] == "duplicate" and not args.include_duplicates:
            rows.append(row)
            summary["duplicate"] += 1
            continue
        summary[row["status"]] = summary.get(row["status"], 0) + 1
        rows.append(row)

    order = {"critical": 0, "review": 1, "ok": 2, "duplicate": 3}
    rows.sort(key=lambda row: (order.get(row["status"], 9), row["id"]))
    report = {"version": 1, "summary": summary, "sources": rows}
    write_json(REPORT_JSON, report)
    write_markdown(report)

    print(f"Text coherence report written to {REPORT_JSON.relative_to(ROOT)}")
    print(f"Markdown report written to {REPORT_MD.relative_to(ROOT)}")
    print(summary)
    for row in rows[:40]:
        if row["status"] in {"critical", "review"}:
            print(f"{row['status']:8} {row['id']} flags={','.join(row.get('flags', []))}")


if __name__ == "__main__":
    main()
