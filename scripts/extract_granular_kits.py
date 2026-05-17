from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


TEXT_DIR = DATA_DIR / "text"
BOOKS_DATA_DIR = DATA_DIR / "books"
ENTITIES_DIR = DATA_DIR / "entities"
REPORTS_DIR = ROOT / "docs" / "reports" / "granular"

PAGE_RE = re.compile(r"^--- page (\d+) ---$")
KIT_TERM_RE = re.compile(r"\bkits?\b|kits?\s+de\s+personagem|novos\s+kits", re.IGNORECASE)
COST_RE = re.compile(r"\bCustos?\s*:|\bCusto em pontos de Aprimoramento\s*:", re.IGNORECASE)
KIT_LABEL_RE = re.compile(r"^Kit\s*:\s*(?P<name>.+?)\s*$", re.IGNORECASE)
KIT_COST_RE = re.compile(
    r"Custo\s*:\s*(?P<cost>.*?)(?=\bPer[iÃ­]cias\s*:|\bPercias\s*:|\bAprimoramentos\s*:|\bPontos\b|$)",
    re.IGNORECASE | re.DOTALL,
)
SKILLS_RE = re.compile(
    r"(?:Per[iÃ­]cias|Percias)\s*:\s*(?P<skills>.*?)(?=\bAprimoramentos\s*:|\bPontos de|\bPoderes\b|$)",
    re.IGNORECASE | re.DOTALL,
)
OPTIONS_RE = re.compile(
    r"Aprimoramentos\s*:\s*(?P<options>.*?)(?=\bPontos de|\bPontos Her[oÃ³]icos|\bPoderes\b|$)",
    re.IGNORECASE | re.DOTALL,
)

KIT_COST_RE = re.compile(
    r"(?:Custos?|Custo em pontos de Aprimoramento)\s*:\s*(?P<cost>.*?)(?=\bPer[iíÃƒÂ­]cias(?:\s+(?:Obrigat[oó]rias|Sugeridas))?\s*:|\bPercias(?:\s+(?:Obrigatorias|Sugeridas))?\s*:|\bAprimoramentos\s*:|\bAtributos Principais\s*:|\bPontos\b|$)",
    re.IGNORECASE | re.DOTALL,
)
SKILLS_RE = re.compile(
    r"(?:Per[iíÃƒÂ­]cias|Percias)(?:\s+(?:Obrigat[oó]rias|Obrigatorias|Sugeridas))?\s*:\s*(?P<skills>.*?)(?=\bAprimoramentos\s*:|\bPontos de|\bPoderes\b|\bB[oô]nus de Treino\b|$)",
    re.IGNORECASE | re.DOTALL,
)

DEDICATED_SOURCE_KEYWORDS = ("kit", "kits")
LABEL_HEADINGS = {
    "arkanun",
    "kits",
    "kits angelicais",
    "kits de personagem",
    "demonios",
    "demônios",
    "demonios foragidos",
    "demônios foragidos",
    "kits demonicos",
    "linguas antigas",
    "línguas antigas",
    "kits demonÃ­acos",
    "kits militares",
    "novos kits",
    "trevas",
}
CONNECTOR_WORDS = {"a", "as", "ao", "aos", "da", "das", "de", "do", "dos", "e", "o", "os"}
BAD_KIT_NAMES = {
    "a terra",
    "alma",
    "anjos",
    "aprimoramento",
    "aprimoramentos",
    "armas",
    "armas brancas",
    "ciencias",
    "ciências",
    "como",
    "conhecimento",
    "costuma",
    "costumam",
    "departamento de policia federal",
    "departamento de polÃ­cia federal",
    "kits demonÃ­acos",
    "kits demonicos",
    "muitas",
    "normalmente",
    "outros",
    "pablo mestre kblo",
    "personagens",
    "personagem",
    "pericia",
    "pericias",
    "perícia",
    "perícias",
    "pode",
    "ponto de magia",
    "ponto heroico",
    "ponto heróico",
    "pontos",
    "pontos de fe",
    "pontos de fé",
    "pontos de magia",
    "pontos heroicos",
    "pontos heróicos",
    "sc etc",
    "secretaria de assuntos estrategicos",
    "secretaria de assuntos estratÃ©gicos",
}


@dataclass
class Line:
    page: int
    text: str


def fix_mojibake(text: str) -> str:
    if "Ãƒ" not in text and "Ã¢" not in text:
        return text
    try:
        fixed = text.encode("latin1", errors="ignore").decode("utf-8", errors="ignore")
    except UnicodeError:
        return text
    original_score = text.count("Ãƒ") + text.count("Ã¢")
    fixed_score = fixed.count("Ãƒ") + fixed.count("Ã¢")
    return fixed if fixed_score < original_score else text


def normalize_for_search(value: str) -> str:
    return slugify(value).replace("-", " ")


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


def is_dedicated_source(source_id: str, title: str) -> bool:
    haystack = normalize_for_search(f"{source_id} {title}")
    return any(keyword in haystack.split() or keyword in haystack for keyword in DEDICATED_SOURCE_KEYWORDS)


def source_part_is_candidate(part: dict[str, Any], source_title: str) -> bool:
    text = " ".join(
        [
            str(part.get("id", "")),
            str(part.get("name", "")),
            str(part.get("summary", "")),
            str(part.get("category", "")),
            source_title,
        ]
    )
    return part.get("category") == "kit_class" or bool(KIT_TERM_RE.search(text))


def kit_pages_from_text(lines: list[Line]) -> set[int]:
    pages: set[int] = set()
    for line in lines:
        if not line.page or not KIT_TERM_RE.search(line.text):
            continue
        pages.add(line.page)
        normalized = normalize_for_search(line.text)
        if normalized in LABEL_HEADINGS or "novos kits" in normalized or "kits de personagem" in normalized:
            pages.update(range(line.page + 1, line.page + 13))
    return pages


def is_probable_heading(line: str, following: list[str]) -> bool:
    clean = re.sub(r"\s+", " ", line).strip(" *")
    normalized = normalize_for_search(clean)
    if normalized in LABEL_HEADINGS:
        return False
    if normalized in BAD_KIT_NAMES:
        return False
    if len(clean) < 3 or len(clean) > 70:
        return False
    if clean.isdigit() or COST_RE.search(clean) or ":" in clean:
        return False
    if any(char in clean for char in [".", ",", ";"]):
        return False
    words = clean.split()
    if len(words) > 7:
        return False
    letters = [char for char in clean if char.isalpha()]
    if not letters:
        return False
    uppercase_ratio = sum(1 for char in letters if char.isupper()) / len(letters)
    content_words = [word for word in words if normalize_for_search(word) not in CONNECTOR_WORDS]
    title_words = sum(1 for word in content_words if word[:1].isupper())
    if uppercase_ratio < 0.55 and title_words < max(1, len(content_words) - 1):
        return False
    lookahead = " ".join(following[:35])
    return bool(COST_RE.search(lookahead))


def clean_inline_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip(" .;\n\t")


def extract_field(pattern: re.Pattern[str], body: str, group: str) -> str | None:
    match = pattern.search(body)
    if not match:
        return None
    value = clean_inline_text(match.group(group))
    return value or None


def extract_cost_numbers(cost: str | None) -> dict[str, Any]:
    if not cost:
        return {}
    payload: dict[str, Any] = {"costText": cost}
    aprimoramento = re.search(r"(\d+)\s*pts?\.?\s*(?:de\s*)?Aprimoramento", cost, flags=re.IGNORECASE)
    pericia = re.search(r"(\d+)\s*pts?\.?\s*de\s*Per[iÃ­]cia", cost, flags=re.IGNORECASE)
    if aprimoramento:
        payload["aprimoramentoCost"] = int(aprimoramento.group(1))
    if pericia:
        payload["periciaCost"] = int(pericia.group(1))
    return payload


def tag_from_text(name: str, body: str) -> list[str]:
    normalized = normalize_for_search(f"{name} {body}")
    tags = ["kit", "auto-extraido"]
    for tag, keywords in {
        "combate": ["arma", "armas", "combate", "ataque", "defesa", "militar", "soldado"],
        "magia": ["magia", "mago", "ritual", "poderes magicos", "mana"],
        "social": ["labia", "etiqueta", "negociacao", "lideranca", "seducao"],
        "investigacao": ["investigacao", "pesquisa", "rastreio", "detetive"],
        "religiao": ["fe", "religiao", "anjo", "demonio", "angelicais"],
    }.items():
        if any(keyword in normalized for keyword in keywords):
            tags.append(tag)
    return sorted(set(tags))


def extract_from_lines(source_id: str, source_title: str, lines: list[Line], kit_context: str) -> list[dict[str, Any]]:
    headings: list[int] = []
    texts = [line.text for line in lines]
    for index, line in enumerate(lines):
        if is_probable_heading(line.text, texts[index + 1:index + 36]):
            headings.append(index)

    entities: list[dict[str, Any]] = []
    seen_names: set[str] = set()

    def add_entity(name: str, chunk: list[Line], body_offset: int, method: str) -> None:
        if len(chunk) <= body_offset:
            return
        name = re.sub(r"\s+", " ", name).strip(" *")
        name_key = slugify(name)
        if normalize_for_search(name) in BAD_KIT_NAMES:
            return
        if len(name_key) <= 3 or name_key in seen_names:
            return
        body = "\n".join(line.text for line in chunk[body_offset:]).strip()
        if not COST_RE.search(body):
            return
        cost = extract_field(KIT_COST_RE, body, "cost")
        skills = extract_field(SKILLS_RE, body, "skills")
        options = extract_field(OPTIONS_RE, body, "options")
        pages = sorted({line.page for line in chunk if line.page})
        entity = {
            "id": f"kit-{source_id}-{name_key}",
            "name": name,
            "category": "kit_class",
            "subtype": "kit",
            "source": source_id,
            "sourceTitle": source_title,
            "page": pages[0] if pages else None,
            "pages": pages,
            "entries": [body],
            "tags": tag_from_text(name, body),
            "confidence": 0.76,
            "extractionMethod": method,
            "kitContext": kit_context,
        }
        entity.update(extract_cost_numbers(cost))
        if skills:
            entity["skillsText"] = skills
        if options:
            entity["aprimoramentosText"] = options
        entities.append(entity)
        seen_names.add(name_key)

    kit_label_starts: list[int] = []
    for index, line in enumerate(lines):
        match = KIT_LABEL_RE.match(line.text)
        if match and normalize_for_search(match.group("name")) not in BAD_KIT_NAMES:
            kit_label_starts.append(index)

    for current, start in enumerate(kit_label_starts):
        end = kit_label_starts[current + 1] if current + 1 < len(kit_label_starts) else len(lines)
        match = KIT_LABEL_RE.match(lines[start].text)
        if not match:
            continue
        add_entity(match.group("name"), lines[start:end], 1, "auto-kit-label-pass-1")

    for current, start in enumerate(headings):
        end = headings[current + 1] if current + 1 < len(headings) else len(lines)
        chunk = lines[start:end]
        if len(chunk) < 3:
            continue
        add_entity(chunk[0].text, chunk, 1, "auto-kit-heading-pass-1")
    return entities


def lines_for_pages(lines: list[Line], start: int, end: int) -> list[Line]:
    return [line for line in lines if start <= line.page <= end]


def find_heading_indices(lines: list[Line], names: list[str]) -> list[tuple[str, int]]:
    normalized_names = {slugify(name): name for name in names}
    matches: list[tuple[str, int]] = []
    for index, line in enumerate(lines):
        key = slugify(line.text)
        if key in normalized_names:
            matches.append((normalized_names[key], index))
    return matches


def build_classlike_kit(source_id: str, source_title: str, name: str, chunk: list[Line], confidence: float) -> dict[str, Any] | None:
    if len(chunk) < 3:
        return None
    body = "\n".join(line.text for line in chunk[1:]).strip()
    if not COST_RE.search(body):
        return None
    cost = extract_field(KIT_COST_RE, body, "cost")
    skills = extract_field(SKILLS_RE, body, "skills")
    options = extract_field(OPTIONS_RE, body, "options")
    pages = sorted({line.page for line in chunk if line.page})
    entity: dict[str, Any] = {
        "id": f"kit-{source_id}-{slugify(name)}",
        "name": name,
        "category": "kit_class",
        "subtype": "kit",
        "source": source_id,
        "sourceTitle": source_title,
        "page": pages[0] if pages else None,
        "pages": pages,
        "entries": [body],
        "tags": tag_from_text(name, body),
        "confidence": confidence,
        "extractionMethod": "auto-kit-classlike-pass-1",
        "kitContext": "classlike-kit,source-specific",
    }
    entity.update(extract_cost_numbers(cost))
    if skills:
        entity["skillsText"] = skills
    if options:
        entity["aprimoramentosText"] = options
    return entity


def extract_gerador_classlike_kits(source_lookup: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    source_id = "gerador-de-criaturas"
    text_path = TEXT_DIR / f"{source_id}.txt"
    if not text_path.exists():
        return []
    source_title = source_lookup.get(source_id, {}).get("title", "Gerador de criaturas")
    lines = lines_for_pages(split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore")), 99, 110)
    names = ["Mestre das Feras", "Caçador", "Convocador", "Imitador", "Mestre da Transformação"]
    headings = find_heading_indices(lines, names)
    entities: list[dict[str, Any]] = []
    for pos, (name, start) in enumerate(headings):
        end = headings[pos + 1][1] if pos + 1 < len(headings) else len(lines)
        entity = build_classlike_kit(source_id, source_title, name, lines[start:end], 0.82)
        if entity:
            entities.append(entity)
    return entities


def extract_demonios_classlike_kits(source_lookup: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    source_id = "demonios-a-divina-comedia"
    text_path = TEXT_DIR / f"{source_id}.txt"
    if not text_path.exists():
        return []
    source_title = source_lookup.get(source_id, {}).get("title", "Demônios - A Divina Comédia")
    lines = lines_for_pages(split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore")), 104, 105)
    names = ["EXORCISTA DE ROMA", "EXORCISTA DE ESPANHOL", "EXORCISTA DE CONSTANTINOPLA"]
    headings = find_heading_indices(lines, names)
    stat_headings: list[tuple[str, int]] = []
    for name, index in headings:
        lookahead = " ".join(line.text for line in lines[index:index + 8])
        if re.search(r"Tempo de aprendizado|Custos?", lookahead, flags=re.IGNORECASE):
            stat_headings.append((name.title().replace(" De ", " de "), index))
    all_heading_indices = [index for _, index in headings]
    entities: list[dict[str, Any]] = []
    for name, start in stat_headings:
        next_indices = [index for index in all_heading_indices if index > start]
        end = next_indices[0] if next_indices else len(lines)
        entity = build_classlike_kit(source_id, source_title, name, lines[start:end], 0.8)
        if entity:
            entities.append(entity)
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
        title = source_lookup.get(source_id, {}).get("title", source_id)
        lines = split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore"))
        source_titles[source_id] = title

        if is_dedicated_source(source_id, title):
            pages = {line.page for line in lines if line.page}
            if pages:
                candidates_by_source.setdefault(source_id, set()).update(pages)
                candidate_contexts.setdefault(source_id, set()).add("source-title")

        text_pages = kit_pages_from_text(lines)
        if text_pages:
            candidates_by_source.setdefault(source_id, set()).update(text_pages)
            candidate_contexts.setdefault(source_id, set()).add("text-kit-term")

        book_path = BOOKS_DATA_DIR / f"{source_id}.json"
        if not book_path.exists():
            continue
        book = read_json(book_path, {})
        book_title = book.get("title") or title
        source_titles[source_id] = book_title
        for part in book.get("parts", []):
            if not source_part_is_candidate(part, book_title):
                continue
            pages = expand_pages(part.get("pages", []))
            if not pages:
                continue
            candidates_by_source.setdefault(source_id, set()).update(pages)
            candidate_contexts.setdefault(source_id, set()).add("book-part")

    all_entities: list[dict[str, Any]] = []
    per_source: list[dict[str, Any]] = []
    for source_id in sorted(candidates_by_source):
        text_path = TEXT_DIR / f"{source_id}.txt"
        if not text_path.exists():
            continue
        title = source_titles.get(source_id, source_id)
        lines = split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore"))
        pages = candidates_by_source[source_id]
        selected = [line for line in lines if line.page in pages]
        context = ",".join(sorted(candidate_contexts.get(source_id, {"unknown"})))
        entities = extract_from_lines(source_id, title, selected, context)
        all_entities.extend(entities)
        per_source.append({"source": source_id, "candidatePages": sorted(pages), "context": context, "extractedCount": len(entities)})

    for source_id, extractor in [
        ("gerador-de-criaturas", extract_gerador_classlike_kits),
        ("demonios-a-divina-comedia", extract_demonios_classlike_kits),
    ]:
        if source_id not in ready_sources:
            continue
        entities = extractor(source_lookup)
        all_entities.extend(entities)
        per_source.append(
            {
                "source": source_id,
                "candidatePages": sorted({page for entity in entities for page in entity.get("pages", [])}),
                "context": "classlike-kit,source-specific",
                "extractedCount": len(entities),
            }
        )

    write_json(ENTITIES_DIR / "kit_class_granular.json", all_entities)
    write_json(DATA_DIR / "work" / "granular-kits-review.json", [])
    report = {
        "version": 1,
        "subtype": "kit",
        "candidateSourceCount": len(candidates_by_source),
        "rawExtractedCount": len(all_entities),
        "sources": per_source,
    }
    write_json(INDEX_DIR / "granular-kits-report.json", report)

    lines = [
        "# Granular kits pass 001",
        "",
        f"- Candidate sources scanned: {report['candidateSourceCount']}",
        f"- Raw extracted kit candidates: {report['rawExtractedCount']}",
        "",
        "## By source",
        "",
        "| Source | Candidate pages | Context | Extracted |",
        "| --- | ---: | --- | ---: |",
    ]
    for item in per_source:
        lines.append(f"| `{item['source']}` | {len(item['candidatePages'])} | {item['context']} | {item['extractedCount']} |")
    lines.append("")
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "granular-kits-pass-001.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Extracted {len(all_entities)} raw kit candidates from {len(candidates_by_source)} sources.")


if __name__ == "__main__":
    main()
