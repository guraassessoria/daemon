from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


TEXT_DIR = DATA_DIR / "text"
BOOKS_DATA_DIR = DATA_DIR / "books"
ENTITIES_DIR = DATA_DIR / "entities"
REPORTS_DIR = ROOT / "docs"

PAGE_RE = re.compile(r"^--- page (\d+) ---$")

POWER_SOURCE_RE = re.compile(r"poder|poderes|superpoder|animalidade|fadas?|psi[oô]nic|mentais|cabalistic", re.IGNORECASE)
MAGIC_SOURCE_RE = re.compile(r"magia|magias|grim[oó]rio|caminhos?|kidou|kidous|energia-mistica|energia mistica", re.IGNORECASE)
POWER_SIGNAL_RE = re.compile(
    r"\bCusto\s*:|\bCusto\s+\d+|\bN[ií]vel\s*\d+\s*:|\bUso Autom[aá]tico\b|"
    r"\bPontos? de Poder\b|\bCaminhos?\s*:|\bPMs?\b|\bReiatsu\b",
    re.IGNORECASE,
)
MAGIC_SIGNAL_RE = re.compile(
    r"\bC[ií]rculo\b|\bEntender\s*-|\bCriar\s*-|\bControlar\s*-|\bFocus\b|"
    r"\bCaminhos?\b|\bPMs?\b|\bPontos? de Magia\b|\bAlcance\s*:|\bDura[cç][aã]o\s*:|"
    r"\bEfeito\s*:|\bMagia\b",
    re.IGNORECASE,
)
RITUAL_SIGNAL_RE = re.compile(r"\britual\b|\brituais\b", re.IGNORECASE)
SENTENCE_END_RE = re.compile(r"[.;!?]$")

INLINE_POWER_RE = re.compile(r"^\((?P<cost>\d+)\)\s*(?P<name>[^:]{3,70}):\s*(?P<body>.*)$")

SECTION_HEADINGS = {
    "agradecimentos",
    "bibliografia",
    "capitulo",
    "capitulo i",
    "capitulo ii",
    "capitulo iii",
    "capitulo quatro",
    "capitulo tres",
    "conclusao",
    "dedicatoria",
    "indice",
    "introducao",
    "novas regras",
    "pagina inicial",
    "prefacio",
    "sumario",
}

BAD_NAMES = {
    "daemon",
    "magia",
    "magias",
    "poder",
    "poderes",
    "poderes animais",
    "poderes arcadianos",
    "poderes misticos",
    "poderes mentais",
    "super poderes",
}


@dataclass
class Line:
    page: int
    text: str


def fix_mojibake(text: str) -> str:
    if "Ã" not in text and "Â" not in text:
        return text
    try:
        fixed = text.encode("latin1", errors="ignore").decode("utf-8", errors="ignore")
    except UnicodeError:
        return text
    original_score = text.count("Ã") + text.count("Â")
    fixed_score = fixed.count("Ã") + fixed.count("Â")
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


def normalize_text(value: str) -> str:
    return slugify(value).replace("-", " ")


def expand_pages(pages: list[Any]) -> set[int]:
    expanded: set[int] = set()
    for page in pages:
        if isinstance(page, int):
            expanded.add(page)
        elif isinstance(page, list) and len(page) == 2 and all(isinstance(item, int) for item in page):
            expanded.update(range(page[0], page[1] + 1))
    return expanded


def source_part_is_candidate(part: dict[str, Any], source_title: str) -> bool:
    text = " ".join([part.get("id", ""), part.get("name", ""), part.get("summary", ""), source_title])
    category = part.get("category")
    return category == "power_magic" or bool(POWER_SOURCE_RE.search(text) or MAGIC_SOURCE_RE.search(text))


def source_context(source_id: str, source_title: str) -> set[str]:
    haystack = f"{source_id} {source_title}".replace("-", " ")
    context: set[str] = set()
    if POWER_SOURCE_RE.search(haystack):
        context.add("power-source")
    if MAGIC_SOURCE_RE.search(haystack):
        context.add("magic-source")
    return context


def is_probable_heading(line: str, following: list[str]) -> bool:
    clean = re.sub(r"\s+", " ", line).strip(" *")
    normalized = normalize_text(clean)
    if not clean or normalized in SECTION_HEADINGS or normalized in BAD_NAMES:
        return False
    if len(clean) < 3 or len(clean) > 80:
        return False
    if clean.isdigit() or re.fullmatch(r"[-–—0-9IVXLCDM ]+", clean):
        return False
    if clean.count(",") > 1 or clean.count(".") > 1:
        return False
    if SENTENCE_END_RE.search(clean):
        return False
    words = clean.split()
    if len(words) > 9:
        return False
    letters = [char for char in clean if char.isalpha()]
    if not letters:
        return False
    uppercase_ratio = sum(1 for char in letters if char.isupper()) / len(letters)
    title_words = sum(1 for word in words if word[:1].isupper())
    looks_like_title = uppercase_ratio >= 0.55 or title_words >= max(1, len(words) - 1)
    if not looks_like_title:
        return False
    lookahead = " ".join(following[:18])
    return bool(POWER_SIGNAL_RE.search(lookahead) or MAGIC_SIGNAL_RE.search(lookahead))


def subtype_for(source_id: str, source_title: str, name: str, body: str, context: str) -> str | None:
    source_haystack = f"{source_id} {source_title}".replace("-", " ")
    combined = f"{name} {body}"
    if "power-source" in context and not MAGIC_SOURCE_RE.search(source_haystack):
        return "poder"
    if "magic-source" in context and not POWER_SOURCE_RE.search(source_haystack):
        return "magia"
    power_hits = len(POWER_SIGNAL_RE.findall(combined))
    magic_hits = len(MAGIC_SIGNAL_RE.findall(combined))
    if re.search(r"\bN[ií]vel\s*\d+\s*:", body, re.IGNORECASE) and re.search(r"\bPontos? de Poder\b|\bCusto\b", body, re.IGNORECASE):
        return "poder"
    if re.search(r"\bCaminhos?\s*:", body, re.IGNORECASE) and "poderes-mentais" in source_id:
        return "poder"
    if re.search(r"\bC[ií]rculo\b|\bEntender\s*-|\bCriar\s*-|\bControlar\s*-|\bFocus\b", body, re.IGNORECASE):
        return "magia"
    if magic_hits > power_hits:
        return "magia"
    if power_hits:
        return "poder"
    return None


def tag_from_text(name: str, body: str, subtype: str) -> list[str]:
    normalized = normalize_text(f"{name} {body}")
    tags = [subtype, "auto-extraido"]
    for tag, keywords in {
        "fada": ["fada", "fadas", "arcad"],
        "animalidade": ["fera", "feras", "animal"],
        "mental": ["mental", "mente", "psion", "telepat", "telecines"],
        "angelico": ["anjo", "anjos", "paradisia"],
        "demonico": ["demonio", "demonios", "inferno"],
        "caminho": ["caminho", "caminhos", "circulo"],
        "kidou": ["kidou", "reiatsu", "hadou", "bakudou"],
    }.items():
        if any(keyword in normalized for keyword in keywords):
            tags.append(tag)
    return sorted(set(tags))


def build_entity(
    source_id: str,
    source_title: str,
    name: str,
    chunk: list[Line],
    context: str,
    method: str,
) -> dict[str, Any] | None:
    if len(chunk) < 2:
        return None
    clean_name = re.sub(r"\s+", " ", name).strip(" *")
    name_key = slugify(clean_name)
    if not name_key or name_key in BAD_NAMES or len(name_key) <= 2:
        return None
    body = "\n".join(line.text for line in chunk[1:]).strip()
    if len(body) < 35:
        return None
    subtype = subtype_for(source_id, source_title, clean_name, body, context)
    if not subtype:
        return None
    if subtype == "magia" and RITUAL_SIGNAL_RE.search(f"{clean_name} {body}") and not MAGIC_SIGNAL_RE.search(body):
        return None
    pages = sorted({line.page for line in chunk if line.page})
    entity_id = f"{subtype}-{source_id}-{name_key}"
    return {
        "id": entity_id,
        "name": clean_name,
        "category": "power_magic",
        "subtype": subtype,
        "source": source_id,
        "sourceTitle": source_title,
        "page": pages[0] if pages else None,
        "pages": pages,
        "entries": [body],
        "tags": tag_from_text(clean_name, body, subtype),
        "confidence": 0.82 if subtype == "poder" else 0.78,
        "extractionMethod": method,
        "powerMagicContext": context,
    }


def extract_from_lines(source_id: str, source_title: str, lines: list[Line], context: str) -> list[dict[str, Any]]:
    headings: list[int] = []
    texts = [line.text for line in lines]
    for index, line in enumerate(lines):
        if is_probable_heading(line.text, texts[index + 1:index + 20]):
            headings.append(index)

    entities: list[dict[str, Any]] = []
    seen: set[str] = set()
    for pos, start in enumerate(headings):
        end = headings[pos + 1] if pos + 1 < len(headings) else len(lines)
        chunk = lines[start:end]
        name_key = slugify(chunk[0].text)
        if name_key in seen:
            continue
        entity = build_entity(source_id, source_title, chunk[0].text, chunk, context, "auto-power-magic-heading-pass-1")
        if entity:
            entities.append(entity)
            seen.add(name_key)
    return entities


def extract_inline_cabalistic(source_id: str, source_title: str, lines: list[Line], context: str) -> list[dict[str, Any]]:
    if source_id != "poderes-cabalisticos":
        return []
    starts: list[tuple[str, int]] = []
    for index, line in enumerate(lines):
        match = INLINE_POWER_RE.match(line.text)
        if match:
            starts.append((match.group("name").strip(), index))
    entities: list[dict[str, Any]] = []
    for pos, (name, start) in enumerate(starts):
        end = starts[pos + 1][1] if pos + 1 < len(starts) else len(lines)
        first = lines[start]
        match = INLINE_POWER_RE.match(first.text)
        if not match:
            continue
        chunk = [Line(first.page, name), Line(first.page, f"Custo: {match.group('cost')} ponto(s). {match.group('body').strip()}"), *lines[start + 1:end]]
        entity = build_entity(source_id, source_title, name, chunk, context, "auto-inline-cabalistic-power-pass-1")
        if entity:
            entity["confidence"] = 0.86
            entities.append(entity)
    return entities


def add_legacy_manual_entities(ready_sources: set[str], source_lookup: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    manual_entities = read_json(ENTITIES_DIR / "power_magic.json", [])
    if not isinstance(manual_entities, list):
        return []
    entities: list[dict[str, Any]] = []
    for entity in manual_entities:
        source_id = entity.get("source")
        if source_id not in ready_sources:
            continue
        name = str(entity.get("name") or "").strip()
        body = "\n".join(entry for entry in entity.get("entries", []) if isinstance(entry, str)).strip()
        if not name or len(body) < 35:
            continue
        source_title = source_lookup.get(source_id, {}).get("title", source_id)
        context = "manual-power-magic"
        subtype = subtype_for(source_id, source_title, name, body, context) or ("magia" if "magia" in normalize_text(f"{name} {body}") else "poder")
        payload = {
            **entity,
            "id": f"{subtype}-{source_id}-{slugify(name)}",
            "category": "power_magic",
            "subtype": subtype,
            "sourceTitle": source_title,
            "pages": [entity["page"]] if isinstance(entity.get("page"), int) else entity.get("pages", []),
            "tags": sorted(set([*entity.get("tags", []), subtype, "manual"])),
            "extractionMethod": "manual-power-magic-pass-1",
            "powerMagicContext": context,
        }
        entities.append(payload)
    return entities


def main() -> None:
    area_summary = read_json(INDEX_DIR / "area-summary.json", {})
    ready_sources = set(area_summary.get("readySources", []))
    source_lookup = {source["id"]: source for source in read_json(INDEX_DIR / "sources.json", {"sources": []}).get("sources", [])}

    candidates_by_source: dict[str, set[int]] = {}
    source_titles: dict[str, str] = {}
    candidate_contexts: dict[str, set[str]] = {}

    for source_id in sorted(ready_sources):
        text_path = TEXT_DIR / f"{source_id}.txt"
        if not text_path.exists():
            continue
        source_title = source_lookup.get(source_id, {}).get("title", source_id)
        source_titles[source_id] = source_title
        source_ctx = source_context(source_id, source_title)
        if source_ctx:
            lines = split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore"))
            pages = {line.page for line in lines if line.page}
            if pages:
                candidates_by_source.setdefault(source_id, set()).update(pages)
                candidate_contexts.setdefault(source_id, set()).update(source_ctx)

        book_path = BOOKS_DATA_DIR / f"{source_id}.json"
        if not book_path.exists():
            continue
        book = read_json(book_path, {})
        book_title = book.get("title") or source_title
        source_titles[source_id] = book_title
        for part in book.get("parts", []):
            if not source_part_is_candidate(part, book_title):
                continue
            pages = expand_pages(part.get("pages", []))
            if not pages:
                continue
            candidates_by_source.setdefault(source_id, set()).update(pages)
            if part.get("category") == "power_magic":
                candidate_contexts.setdefault(source_id, set()).add("power-magic-book-part")
            if POWER_SOURCE_RE.search(" ".join([part.get("name", ""), part.get("summary", "")])):
                candidate_contexts.setdefault(source_id, set()).add("power-term")
            if MAGIC_SOURCE_RE.search(" ".join([part.get("name", ""), part.get("summary", "")])):
                candidate_contexts.setdefault(source_id, set()).add("magic-term")

    all_entities: list[dict[str, Any]] = []
    per_source: list[dict[str, Any]] = []
    for source_id in sorted(candidates_by_source):
        text_path = TEXT_DIR / f"{source_id}.txt"
        if not text_path.exists():
            continue
        title = source_titles.get(source_id, source_id)
        lines = split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore"))
        selected = [line for line in lines if line.page in candidates_by_source[source_id]]
        context = ",".join(sorted(candidate_contexts.get(source_id, {"unknown"})))
        entities = extract_from_lines(source_id, title, selected, context)
        entities.extend(extract_inline_cabalistic(source_id, title, selected, context))
        all_entities.extend(entities)
        per_source.append(
            {
                "source": source_id,
                "candidatePages": sorted(candidates_by_source[source_id]),
                "context": context,
                "extractedCount": len(entities),
            }
        )

    manual_entities = add_legacy_manual_entities(ready_sources, source_lookup)
    all_entities.extend(manual_entities)
    if manual_entities:
        per_source.append({"source": "_manual_power_magic", "candidatePages": [], "context": "manual-power-magic", "extractedCount": len(manual_entities)})

    unique_entities: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, str, str]] = set()
    for entity in sorted(all_entities, key=lambda item: (item.get("source") or "", item.get("page") or 0, item.get("name") or "")):
        key = (entity.get("subtype"), entity.get("source"), slugify(str(entity.get("name") or "")))
        if key in seen_keys:
            continue
        seen_keys.add(key)
        unique_entities.append(entity)

    write_json(ENTITIES_DIR / "power_magic_granular.json", unique_entities)
    report = {
        "version": 1,
        "candidateSourceCount": len(candidates_by_source),
        "rawExtractedCount": len(all_entities),
        "extractedCount": len(unique_entities),
        "sources": per_source,
    }
    write_json(INDEX_DIR / "granular-poderes-magias-report.json", report)

    lines = [
        "# Poderes e magias granular pass 001",
        "",
        "Varredura das fontes prontas para separar poderes e magias em registros certificados.",
        "",
        f"- Candidate sources: {len(candidates_by_source)}",
        f"- Raw extracted candidates: {len(all_entities)}",
        f"- Unique extracted candidates: {len(unique_entities)}",
        "",
        "## By source",
        "",
        "| Source | Candidates | Context | Pages |",
        "| --- | ---: | --- | --- |",
    ]
    for item in per_source:
        pages = item.get("candidatePages", [])
        page_text = f"{pages[0]}-{pages[-1]} ({len(pages)} pages)" if len(pages) > 12 else ", ".join(str(page) for page in pages)
        lines.append(f"| `{item['source']}` | {item['extractedCount']} | {item['context']} | {page_text} |")
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "granular-poderes-magias-pass-001.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Extracted {len(unique_entities)} raw poderes/magias candidates from {len(candidates_by_source)} sources.")


if __name__ == "__main__":
    main()
