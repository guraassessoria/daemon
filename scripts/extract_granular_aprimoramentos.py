from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


TEXT_DIR = DATA_DIR / "text"
BOOKS_DATA_DIR = DATA_DIR / "books"
ENTITIES_DIR = DATA_DIR / "entities"
REPORTS_DIR = ROOT / "docs" / "reports" / "granular"

COST_RE = re.compile(
    r"\b(?:-?\d+\s*(?:a\s*\d+\s*)?pontos?|vari[aá]vel|restri[cç][aã]o|apenas para|pr[eé]-?requisito)",
    re.IGNORECASE,
)
PAGE_RE = re.compile(r"^--- page (\d+) ---$")
SENTENCE_END_RE = re.compile(r"[.;:!?]$")

SECTION_HEADINGS = {
    "aprimoramentos",
    "aprimoramentos positivos",
    "aprimoramentos negativos",
    "aprimoramentos conceituais",
    "aprimoramentos fisicos",
    "aprimoramentos físicos",
    "novos aprimoramentos",
    "vantagens",
    "desvantagens",
    "talentos",
    "introducao",
    "introdução",
    "desenvolvimento",
    "agradecimentos",
}

BAD_HEADING_NAMES = {
    "aliados",
    "mago",
    "mortos",
    "ponto",
    "pontos",
    "secreta",
    "tornar se",
    "uma",
    "ultimas consideracoes",
    "últimas considerações",
}

AUTO_PUBLISH_SOURCES = {
    "aprimoramentos-1",
    "aprimoramentos-2",
    "aprimoramentos-3",
    "aprimoramentos-4",
    "aprimoramentostormenta",
    "talentos",
}


@dataclass
class Line:
    page: int
    text: str


def fix_mojibake(text: str) -> str:
    if "Ã" not in text and "â" not in text:
        return text
    try:
        fixed = text.encode("latin1", errors="ignore").decode("utf-8", errors="ignore")
    except UnicodeError:
        return text
    original_score = text.count("Ã") + text.count("â")
    fixed_score = fixed.count("Ã") + fixed.count("â")
    return fixed if fixed_score < original_score else text


def split_lines_by_page(text: str) -> list[Line]:
    lines: list[Line] = []
    current_page = 0
    for raw_line in text.splitlines():
        marker = PAGE_RE.match(raw_line.strip())
        if marker:
            current_page = int(marker.group(1))
            continue
        line = fix_mojibake(raw_line).strip()
        if line:
            lines.append(Line(current_page, line))
    return lines


def expand_pages(pages: list[Any]) -> set[int]:
    expanded: set[int] = set()
    for page in pages:
        if isinstance(page, int):
            expanded.add(page)
        elif isinstance(page, list) and len(page) == 2 and all(isinstance(item, int) for item in page):
            expanded.update(range(page[0], page[1] + 1))
    return expanded


def normalize_text(value: str) -> str:
    return slugify(value).replace("-", " ")


def is_probable_heading(line: str, following: list[str]) -> bool:
    clean = re.sub(r"\s+", " ", line).strip()
    normalized = normalize_text(clean)
    if normalized in SECTION_HEADINGS:
        return False
    if len(clean) < 3 or len(clean) > 70:
        return False
    if clean.isdigit() or COST_RE.search(clean):
        return False
    if SENTENCE_END_RE.search(clean):
        return False
    words = clean.split()
    if len(words) > 8:
        return False
    letters = [char for char in clean if char.isalpha()]
    if not letters:
        return False
    uppercase_ratio = sum(1 for char in letters if char.isupper()) / len(letters)
    title_words = sum(1 for word in words if word[:1].isupper())
    looks_like_title = uppercase_ratio >= 0.68 or title_words >= max(1, len(words) - 1)
    if not looks_like_title:
        return False
    lookahead = " ".join(following[:12])
    return bool(COST_RE.search(lookahead))


def source_part_is_candidate(part: dict[str, Any]) -> bool:
    text = normalize_text(" ".join([
        part.get("id", ""),
        part.get("name", ""),
        part.get("summary", ""),
        part.get("sourceTitle", ""),
    ]))
    keywords = [
        "aprimoramento",
        "aprimoramentos",
        "talento",
        "talentos",
        "vantagem",
        "vantagens",
        "desvantagem",
        "fraqueza",
        "fraquezas",
    ]
    return any(keyword in text for keyword in keywords)


def is_publishable_part(source_id: str, part: dict[str, Any]) -> bool:
    source_slug = normalize_text(source_id)
    source_title = normalize_text(part.get("sourceTitle", ""))
    return any(
        keyword in f"{source_slug} {source_title}"
        for keyword in ["aprimoramento", "aprimoramentos", "talento", "talentos"]
    )


def extract_costs(text: str) -> list[str]:
    costs = re.findall(r"\b-?\d+\s*(?:a\s*\d+\s*)?pontos?\b|\bvari[aá]vel\b", text, flags=re.IGNORECASE)
    normalized_costs: set[str] = set()
    for cost in costs:
        normalized = re.sub(r"\s+", " ", fix_mojibake(cost)).strip().lower()
        numbers = [int(number) for number in re.findall(r"-?\d+", normalized)]
        if numbers and any(abs(number) > 20 for number in numbers):
            continue
        normalized_costs.add(normalized)
    return sorted(normalized_costs)


def tag_from_name_and_text(name: str, text: str) -> list[str]:
    normalized = normalize_text(f"{name} {text}")
    tags = ["aprimoramento", "auto-extraido"]
    for tag, keywords in {
        "combate": ["combate", "ataque", "defesa", "dano", "arma", "iniciativa"],
        "magia": ["magia", "ritual", "mana", "focus", "mago", "feitico"],
        "social": ["carisma", "labia", "lideranca", "seducao", "etiqueta"],
        "pericia": ["pericia", "pericias", "teste", "testes"],
        "sobrenatural": ["demonio", "anjo", "espirito", "vampiro", "sobrenatural"],
        "fisico": ["forca", "constituicao", "destreza", "agilidade", "pvs"],
    }.items():
        if any(keyword in normalized for keyword in keywords):
            tags.append(tag)
    return sorted(set(tags))


def extract_from_lines(source_id: str, source_title: str, lines: list[Line]) -> list[dict[str, Any]]:
    headings: list[int] = []
    texts = [line.text for line in lines]
    for index, line in enumerate(lines):
        if is_probable_heading(line.text, texts[index + 1:index + 13]):
            headings.append(index)

    entities: list[dict[str, Any]] = []
    seen_names: set[str] = set()
    for current, start in enumerate(headings):
        end = headings[current + 1] if current + 1 < len(headings) else len(lines)
        chunk_lines = lines[start:end]
        if len(chunk_lines) < 2:
            continue
        name = re.sub(r"\s+", " ", chunk_lines[0].text).strip(" *")
        name_key = slugify(name)
        normalized_name = normalize_text(name)
        if normalized_name in BAD_HEADING_NAMES:
            continue
        if len(name_key) <= 3:
            continue
        if name_key in seen_names:
            continue
        body = "\n".join(line.text for line in chunk_lines[1:]).strip()
        if len(body) < 45 or not COST_RE.search(body):
            continue
        pages = sorted({line.page for line in chunk_lines if line.page})
        entity_id = f"aprimoramento-{source_id}-{name_key}"
        entities.append(
            {
                "id": entity_id,
                "name": name,
                "category": "character_option",
                "subtype": "aprimoramento",
                "source": source_id,
                "sourceTitle": source_title,
                "page": pages[0] if pages else None,
                "pages": pages,
                "costs": extract_costs(body),
                "entries": [body],
                "tags": tag_from_name_and_text(name, body),
                "confidence": 0.74,
                "extractionMethod": "auto-aprimoramento-pass-1",
            }
        )
        seen_names.add(name_key)
    return entities


def main() -> None:
    ready_sources = set(read_json(INDEX_DIR / "area-summary.json", {}).get("readySources", []))
    source_lookup = {source["id"]: source for source in read_json(INDEX_DIR / "sources.json", {"sources": []}).get("sources", [])}
    publishable_by_source: dict[str, set[int]] = {}
    review_by_source: dict[str, set[int]] = {}
    source_titles: dict[str, str] = {}

    for source_id in sorted(AUTO_PUBLISH_SOURCES & ready_sources):
        text_path = TEXT_DIR / f"{source_id}.txt"
        if not text_path.exists():
            continue
        lines = split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore"))
        pages = {line.page for line in lines if line.page}
        if pages:
            publishable_by_source[source_id] = pages
            source_titles[source_id] = source_lookup.get(source_id, {}).get("title", source_id)

    for source_id in sorted(ready_sources - set(publishable_by_source)):
        book_path = BOOKS_DATA_DIR / f"{source_id}.json"
        if not book_path.exists():
            continue
        book = read_json(book_path, {})
        for part in book.get("parts", []):
            if not source_part_is_candidate(part):
                continue
            pages = expand_pages(part.get("pages", []))
            if not pages:
                continue
            target = publishable_by_source if is_publishable_part(source_id, {**part, "sourceTitle": book.get("title", "")}) else review_by_source
            target.setdefault(source_id, set()).update(pages)
            source_titles[source_id] = book.get("title") or source_lookup.get(source_id, {}).get("title", source_id)

    all_entities: list[dict[str, Any]] = []
    per_source: list[dict[str, Any]] = []
    review_entities: list[dict[str, Any]] = []
    review_per_source: list[dict[str, Any]] = []

    for source_id in sorted(publishable_by_source):
        text_path = TEXT_DIR / f"{source_id}.txt"
        if not text_path.exists():
            continue
        lines = split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore"))
        pages = publishable_by_source[source_id]
        selected = [line for line in lines if line.page in pages]
        entities = extract_from_lines(source_id, source_titles.get(source_id, source_id), selected)
        all_entities.extend(entities)
        per_source.append(
            {
                "source": source_id,
                "candidatePages": sorted(pages),
                "extractedCount": len(entities),
            }
        )

    for source_id in sorted(review_by_source):
        text_path = TEXT_DIR / f"{source_id}.txt"
        if not text_path.exists():
            continue
        lines = split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore"))
        pages = review_by_source[source_id]
        selected = [line for line in lines if line.page in pages]
        entities = extract_from_lines(source_id, source_titles.get(source_id, source_id), selected)
        review_entities.extend(entities)
        review_per_source.append(
            {
                "source": source_id,
                "candidatePages": sorted(pages),
                "extractedCount": len(entities),
            }
        )

    write_json(ENTITIES_DIR / "character_option_granular.json", all_entities)
    write_json(DATA_DIR / "work" / "granular-aprimoramentos-review.json", review_entities)
    report = {
        "version": 1,
        "subtype": "aprimoramento",
        "publishableSourceCount": len(publishable_by_source),
        "publishedExtractedCount": len(all_entities),
        "reviewSourceCount": len(review_by_source),
        "reviewExtractedCount": len(review_entities),
        "sources": per_source,
        "reviewSources": review_per_source,
    }
    write_json(INDEX_DIR / "granular-aprimoramentos-report.json", report)

    lines = [
        "# Granular aprimoramentos pass 001",
        "",
        f"- Publishable candidate sources: {report['publishableSourceCount']}",
        f"- Published extracted aprimoramentos: {report['publishedExtractedCount']}",
        f"- Review candidate sources: {report['reviewSourceCount']}",
        f"- Review extracted candidates: {report['reviewExtractedCount']}",
        "",
        "## By source",
        "",
        "| Source | Candidate pages | Extracted |",
        "| --- | ---: | ---: |",
    ]
    for item in per_source:
        lines.append(f"| `{item['source']}` | {len(item['candidatePages'])} | {item['extractedCount']} |")
    lines.extend(
        [
            "",
            "## Needs review before publishing",
            "",
            "| Source | Candidate pages | Extracted candidates |",
            "| --- | ---: | ---: |",
        ]
    )
    for item in review_per_source:
        lines.append(f"| `{item['source']}` | {len(item['candidatePages'])} | {item['extractedCount']} |")
    lines.append("")
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "granular-aprimoramentos-pass-001.md").write_text("\n".join(lines), encoding="utf-8")

    print(
        f"Published {len(all_entities)} granular aprimoramentos from {len(publishable_by_source)} sources. "
        f"Queued {len(review_entities)} candidates from {len(review_by_source)} sources for review."
    )


if __name__ == "__main__":
    main()
