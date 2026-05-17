from __future__ import annotations

from pathlib import Path
from statistics import mean

from audit_cleanup_pages import cleanup_source_ids
from audit_good_pages import classify_page, sample
from common import INDEX_DIR, TEXT_DIR, read_json, write_json
from text_quality_report import split_pages


REPORT_JSON = INDEX_DIR / "usable-sources-page-coherence-after-easy-cleanup.json"
REPORT_MD = Path("docs") / "reports" / "manual-review" / "usable-sources-page-coherence-after-easy-cleanup.md"


def load_sources() -> dict[str, dict]:
    payload = read_json(INDEX_DIR / "sources.json", {"sources": []})
    return {row["id"]: row for row in payload["sources"]}


def main() -> None:
    sources = load_sources()
    ids = cleanup_source_ids()
    results = []
    summary = {
        "usableSources": len(ids),
        "sourcesPassed": 0,
        "sourcesWithNotesOnly": 0,
        "sourcesWithReviewPages": 0,
        "totalPagesChecked": 0,
        "okPages": 0,
        "notePages": 0,
        "reviewPages": 0,
        "missingTextFiles": 0,
    }

    for source_id in ids:
        source = sources.get(source_id, {"id": source_id, "title": source_id, "pageCount": None})
        path = TEXT_DIR / f"{source_id}.txt"
        if not path.exists():
            summary["missingTextFiles"] += 1
            results.append({"id": source_id, "title": source["title"], "status": "missing_text_file"})
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        pages = split_pages(text)
        page_count = int(source.get("pageCount") or max(pages.keys(), default=1))
        page_results = []
        source_status = "ok"

        for page in range(1, page_count + 1):
            page_text = pages.get(page, "")
            status, flags, metrics = classify_page(page_text)
            summary["totalPagesChecked"] += 1
            summary[f"{status}Pages"] += 1
            if status == "review":
                source_status = "review"
            elif status == "note" and source_status == "ok":
                source_status = "notes_only"
            page_results.append({
                "page": page,
                "status": status,
                "flags": flags,
                **metrics,
                "sample": sample(page_text) if status != "ok" else "",
            })

        if source_status == "review":
            summary["sourcesWithReviewPages"] += 1
        elif source_status == "notes_only":
            summary["sourcesWithNotesOnly"] += 1
        else:
            summary["sourcesPassed"] += 1

        results.append({
            "id": source_id,
            "title": source["title"],
            "pages": page_count,
            "status": source_status,
            "reviewPageCount": sum(1 for row in page_results if row["status"] == "review"),
            "notePageCount": sum(1 for row in page_results if row["status"] == "note"),
            "avgCharsPerPage": round(mean([row["chars"] for row in page_results]), 2) if page_results else 0,
            "pageResults": page_results,
        })

    write_json(REPORT_JSON, {"version": 1, "summary": summary, "sources": results})
    write_markdown(summary, results)
    print(f"Usable page coherence JSON written to {REPORT_JSON}")
    print(f"Markdown report written to {REPORT_MD}")
    print(summary)
    for row in results:
        if row.get("status") == "review":
            pages = [str(page["page"]) for page in row["pageResults"] if page["status"] == "review"][:30]
            print(f"review {row['id']} pages={','.join(pages)}")


def write_markdown(summary: dict, results: list[dict]) -> None:
    lines = [
        "# Usable Sources Page Coherence After Easy Cleanup",
        "",
        "Page-by-page coherence audit after applying easy cleanup fixes to usable/verification sources.",
        "",
        "## Summary",
        "",
        f"- Usable/verification sources checked: {summary['usableSources']}",
        f"- Pages checked: {summary['totalPagesChecked']}",
        f"- Sources passed with all pages ok: {summary['sourcesPassed']}",
        f"- Sources with only note-level pages: {summary['sourcesWithNotesOnly']}",
        f"- Sources with review-level pages: {summary['sourcesWithReviewPages']}",
        f"- Ok pages: {summary['okPages']}",
        f"- Note pages: {summary['notePages']}",
        f"- Review pages: {summary['reviewPages']}",
        "",
        "Note-level pages are usually covers, blank pages, table/stat blocks, page-number remnants, or mechanically repetitive RPG data. Review-level pages are the remaining pages that need manual correction, source comparison, or OCR/re-extraction.",
        "",
        "## Sources With Review-Level Pages",
        "",
    ]

    review_sources = [row for row in results if row.get("status") == "review"]
    if not review_sources:
        lines.append("None.")
        lines.append("")
    for row in review_sources:
        review_pages = [page for page in row["pageResults"] if page["status"] == "review"]
        pages = ", ".join(str(page["page"]) for page in review_pages[:60])
        if len(review_pages) > 60:
            pages += f", ... (+{len(review_pages) - 60})"
        flags = sorted({flag for page in review_pages for flag in page["flags"]})
        lines += [
            f"### `{row['id']}`",
            "",
            f"- Title: {row['title']}",
            f"- Review pages: {len(review_pages)} / {row['pages']}",
            f"- Pages: {pages}",
            f"- Flags: {', '.join(flags)}",
            "",
        ]
        for page in review_pages[:8]:
            lines.append(f"  - p. {page['page']}: `{', '.join(page['flags'])}` - {page['sample']}")
        lines.append("")

    note_sources = [row for row in results if row.get("status") == "notes_only"]
    lines += ["## Sources With Only Note-Level Pages", ""]
    if not note_sources:
        lines.append("None.")
        lines.append("")
    for row in note_sources:
        note_pages = [page for page in row["pageResults"] if page["status"] == "note"]
        pages = ", ".join(str(page["page"]) for page in note_pages[:45])
        if len(note_pages) > 45:
            pages += f", ... (+{len(note_pages) - 45})"
        lines.append(f"- `{row['id']}`: {len(note_pages)} note page(s): {pages}")
    lines.append("")

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
