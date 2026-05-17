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

RACE_KEYWORD_RE = re.compile(
    r"\bra[cçÃ§]as?\b|\blinhagens?\b|\besp[éeÃ©]cies?\b|\bpovos?\b|"
    r"\belfos?\b|\ban[õoÃµ]es?\b|\bvampiros?\b|\blobisomens?\b|\bfadas?\b|"
    r"\byoukais?\b|\bgaki\b|\bghou?ls?\b|\bdrag[õoÃµ]es?\b|\bimortais?\b",
    re.IGNORECASE,
)
MECHANICAL_RACE_RE = re.compile(
    r"\bCusto\s*:|\bIdade Inicial\s*:|\bAtributos\s*:|\bVantagens\s*:|\bDesvantagens\s*:",
    re.IGNORECASE,
)
KITLIKE_RE = re.compile(
    r"\bPer[iíÃ­]cias?\s*:.*\bAprimoramentos?\s*:.*\bPontos (?:Her[oóÃ³]icos|de F[eéÃ©]|de Magia)\b",
    re.IGNORECASE | re.DOTALL,
)
SENTENCE_END_RE = re.compile(r"[.;:!?]$")

COST_RE = re.compile(r"\bCusto\s*:\s*(?P<cost>.*?)(?=\bIdade Inicial\s*:|\bAtributos\s*:|\bVantagens\s*:|\bDesvantagens\s*:|$)", re.IGNORECASE | re.DOTALL)
AGE_RE = re.compile(r"\bIdade Inicial\s*:\s*(?P<age>.*?)(?=\bAtributos\s*:|\bVantagens\s*:|\bDesvantagens\s*:|$)", re.IGNORECASE | re.DOTALL)
ATTRIBUTES_RE = re.compile(r"\bAtributos\s*:\s*(?P<attributes>.*?)(?=\bVantagens\s*:|\bDesvantagens\s*:|$)", re.IGNORECASE | re.DOTALL)
ADVANTAGES_RE = re.compile(r"\bVantagens\s*:\s*(?P<advantages>.*?)(?=\bDesvantagens\s*:|$)", re.IGNORECASE | re.DOTALL)
DISADVANTAGES_RE = re.compile(r"\bDesvantagens\s*:\s*(?P<disadvantages>.*?)(?=\n[A-ZÁÉÍÓÚÃÕÇ][^\n]{2,60}\n|$)", re.IGNORECASE | re.DOTALL)
FRAQUEZAS_RE = re.compile(r"\bFraquezas?\s*:\s*(?P<weaknesses>.*?)(?=\n[A-ZÁÉÍÓÚÃÕÇ][^\n]{2,60}\n|$)", re.IGNORECASE | re.DOTALL)

SOURCE_KEYWORDS = (
    "raca",
    "racas",
    "raças",
    "linhagem",
    "linhagens",
    "vampiro",
    "vampiros",
    "lobisomem",
    "lobisomens",
    "fada",
    "fadas",
    "youkai",
    "youkais",
    "gaki",
    "elf",
    "anoes",
    "anões",
    "dragoes",
    "dragões",
    "imortal",
    "animalidade",
)

SECTION_HEADINGS = {
    "agradecimentos",
    "aprimoramentos",
    "aprimoramentos especificos",
    "aprimoramentos específicos",
    "atributos",
    "aventuras",
    "bibliografia",
    "campanha",
    "caracteristicas",
    "características",
    "conclusao",
    "conclusão",
    "consideracoes",
    "considerações",
    "creditos",
    "créditos",
    "desvantagens",
    "especial",
    "fraqueza",
    "fraquezas",
    "historia",
    "história",
    "idade inicial",
    "indice",
    "índice",
    "introducao",
    "introdução",
    "modo de vida",
    "organizacao",
    "organização",
    "os aventureiros",
    "poderes",
    "poderes animais",
    "poderes exclusivos",
    "poderes naturais",
    "pontos de fe",
    "pontos de fé",
    "pontos heroicos",
    "pontos heróicos",
    "relacao com outros povos",
    "relação com outros povos",
    "religiao",
    "religião",
    "sociedade",
    "vantagens",
}

BAD_NAMES = {
    "3d t",
    "a origem",
    "ano",
    "anos",
    "ark a nun",
    "custo",
    "daemon",
    "humano",
    "humanos",
    "lobisomem a maldicao",
    "lobisomem a maldição",
    "pagina inicial",
    "racas",
    "raças",
    "sistema",
    "trevas",
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


def normalize_text(value: str) -> str:
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


def source_is_dedicated(source_id: str, source_title: str) -> bool:
    haystack = normalize_text(f"{source_id} {source_title}")
    return any(normalize_text(keyword) in haystack for keyword in SOURCE_KEYWORDS)


def source_part_is_candidate(part: dict[str, Any], source_title: str) -> bool:
    text = " ".join(
        [
            part.get("id", ""),
            part.get("name", ""),
            part.get("summary", ""),
            source_title,
        ]
    )
    return part.get("category") == "race_lineage" or bool(RACE_KEYWORD_RE.search(text))


def is_probable_heading(line: str, following: list[str], allow_narrative: bool) -> bool:
    clean = re.sub(r"\s+", " ", line).strip(" *")
    normalized = normalize_text(clean)
    if not clean or normalized in BAD_NAMES or normalized in SECTION_HEADINGS:
        return False
    if len(clean) < 3 or len(clean) > 70:
        return False
    if clean.isdigit() or re.fullmatch(r"[-–—0-9 ]+", clean):
        return False
    if any(char in clean for char in [";", ":", "?", "!"]):
        return False
    if SENTENCE_END_RE.search(clean):
        return False
    words = clean.split()
    if len(words) > 7:
        return False
    letters = [char for char in clean if char.isalpha()]
    if not letters:
        return False
    uppercase_ratio = sum(1 for char in letters if char.isupper()) / len(letters)
    title_words = sum(1 for word in words if word[:1].isupper())
    if uppercase_ratio < 0.55 and title_words < max(1, len(words) - 1):
        return False
    lookahead = " ".join(following[:28])
    mechanical_hits = len(MECHANICAL_RACE_RE.findall(lookahead))
    if mechanical_hits >= 3:
        return True
    if not allow_narrative:
        return False
    narrative_hits = 0
    normalized_lookahead = normalize_text(lookahead)
    for keyword in [
        "origem e historia",
        "origem e historia",
        "caracteristicas",
        "raca",
        "racas",
        "linhagem",
        "descendente",
        "descendentes",
        "hibrido",
        "hibridos",
        "sangue de",
        "vampiro",
        "vampiros",
        "lobisomem",
        "lobisomens",
        "fada",
        "fadas",
        "youkai",
        "imortal",
        "imortais",
    ]:
        if keyword in normalized_lookahead:
            narrative_hits += 1
    return narrative_hits >= 2 and len(lookahead) > 120


def field_text(regex: re.Pattern[str], body: str, group: str) -> str | None:
    match = regex.search(body)
    if not match:
        return None
    value = re.sub(r"\s+", " ", match.group(group)).strip(" .;-")
    return value or None


def tag_from_text(name: str, body: str, subtype: str) -> list[str]:
    normalized = normalize_text(f"{name} {body}")
    tags = ["auto-extraido", subtype]
    for tag, keywords in {
        "vampiro": ["vampiro", "vampiros", "ghul", "ghoul", "kiang shi", "rakshasa"],
        "lobisomem": ["lobisomem", "lobisomens", "licantrop"],
        "fada": ["fada", "fadas", "arcadia", "arcadiano"],
        "dragao": ["dragao", "dragoes", "draconico"],
        "arton": ["arton", "reinado", "tormenta"],
        "youkai": ["youkai", "kyuukai", "ningenkai", "makai"],
        "imortal": ["imortal", "centelha"],
        "metamorfo": ["metamorfo", "metamorfose", "forma animal"],
    }.items():
        if any(keyword in normalized for keyword in keywords):
            tags.append(tag)
    return sorted(set(tags))


def race_kind(body: str, context: str) -> str:
    mechanical_hits = len(MECHANICAL_RACE_RE.findall(body))
    normalized = normalize_text(f"{context} {body}")
    if mechanical_hits >= 3 and "idade inicial" in normalized:
        return "raca"
    if "linhagem" in normalized or "sangue de" in normalized:
        return "linhagem"
    return "raca"


def build_entity(source_id: str, source_title: str, name: str, chunk: list[Line], context: str, method: str) -> dict[str, Any] | None:
    if len(chunk) < 2:
        return None
    clean_name = re.sub(r"\s+", " ", name).strip(" *")
    name_key = slugify(clean_name)
    if not name_key or name_key in BAD_NAMES or len(name_key) <= 2:
        return None
    body = "\n".join(line.text for line in chunk[1:]).strip()
    if len(body) < 45:
        return None
    kind = race_kind(body, context)
    mechanical_hits = len(MECHANICAL_RACE_RE.findall(body))
    if mechanical_hits < 3 and not RACE_KEYWORD_RE.search(f"{clean_name} {body}"):
        return None
    if kind == "raca" and mechanical_hits < 3 and "race_lineage" not in context:
        return None
    pages = sorted({line.page for line in chunk if line.page})
    entity: dict[str, Any] = {
        "id": f"raca-{source_id}-{name_key}",
        "name": clean_name,
        "category": "race_lineage",
        "subtype": kind,
        "source": source_id,
        "sourceTitle": source_title,
        "page": pages[0] if pages else None,
        "pages": pages,
        "entries": [body],
        "tags": tag_from_text(clean_name, body, kind),
        "confidence": 0.84 if mechanical_hits >= 3 else 0.76,
        "extractionMethod": method,
        "raceContext": context,
    }
    for field_name, regex, group in [
        ("costText", COST_RE, "cost"),
        ("initialAgeText", AGE_RE, "age"),
        ("attributesText", ATTRIBUTES_RE, "attributes"),
        ("advantagesText", ADVANTAGES_RE, "advantages"),
        ("disadvantagesText", DISADVANTAGES_RE, "disadvantages"),
        ("weaknessesText", FRAQUEZAS_RE, "weaknesses"),
    ]:
        value = field_text(regex, body, group)
        if value:
            entity[field_name] = value
    if KITLIKE_RE.search(body) and mechanical_hits < 3:
        entity["possibleKitOrClass"] = True
    return entity


def lines_for_pages(lines: list[Line], start: int, end: int) -> list[Line]:
    return [line for line in lines if start <= line.page <= end]


def find_named_heading_indices(lines: list[Line], aliases: dict[str, str]) -> list[tuple[str, int]]:
    matches: list[tuple[str, int]] = []
    last_key: str | None = None
    last_index = -10
    for index, line in enumerate(lines):
        key = slugify(line.text)
        if key not in aliases:
            continue
        if key == last_key and index <= last_index + 3:
            continue
        matches.append((aliases[key], index))
        last_key = key
        last_index = index
    return matches


def build_source_specific_entity(
    source_id: str,
    source_title: str,
    name: str,
    chunk: list[Line],
    confidence: float = 0.82,
) -> dict[str, Any] | None:
    if len(chunk) < 2:
        return None
    body = "\n".join(line.text for line in chunk[1:]).strip()
    if len(body) < 80:
        return None
    pages = sorted({line.page for line in chunk if line.page})
    name_key = slugify(name)
    entity: dict[str, Any] = {
        "id": f"raca-{source_id}-{name_key}",
        "name": name,
        "category": "race_lineage",
        "subtype": "linhagem",
        "source": source_id,
        "sourceTitle": source_title,
        "page": pages[0] if pages else None,
        "pages": pages,
        "entries": [body],
        "tags": tag_from_text(name, body, "linhagem"),
        "confidence": confidence,
        "extractionMethod": "source-specific-race-lineage-pass-1",
        "raceContext": "source-specific-race-lineage",
    }
    weakness = field_text(FRAQUEZAS_RE, body, "weaknesses")
    if weakness:
        entity["weaknessesText"] = weakness
    return entity


def extract_named_lineages(
    source_id: str,
    source_lookup: dict[str, dict[str, Any]],
    names: list[str],
    start_page: int,
    end_page: int,
    confidence: float = 0.82,
    aliases: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    text_path = TEXT_DIR / f"{source_id}.txt"
    if not text_path.exists():
        return []
    source_title = source_lookup.get(source_id, {}).get("title", source_id)
    lines = lines_for_pages(split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore")), start_page, end_page)
    alias_map = {slugify(name): name for name in names}
    if aliases:
        alias_map.update({slugify(key): value for key, value in aliases.items()})
    headings = find_named_heading_indices(lines, alias_map)
    entities: list[dict[str, Any]] = []
    for pos, (name, start) in enumerate(headings):
        end = headings[pos + 1][1] if pos + 1 < len(headings) else len(lines)
        entity = build_source_specific_entity(source_id, source_title, name, lines[start:end], confidence)
        if entity:
            entities.append(entity)
    return entities


def build_pages_entity(
    source_id: str,
    source_lookup: dict[str, dict[str, Any]],
    name: str,
    start_page: int,
    end_page: int,
    confidence: float = 0.82,
) -> dict[str, Any] | None:
    text_path = TEXT_DIR / f"{source_id}.txt"
    if not text_path.exists():
        return None
    source_title = source_lookup.get(source_id, {}).get("title", source_id)
    lines = lines_for_pages(split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore")), start_page, end_page)
    if not lines:
        return None
    return build_source_specific_entity(source_id, source_title, name, [Line(start_page, name), *lines], confidence)


def source_specific_entities(ready_sources: set[str], source_lookup: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    entities: list[dict[str, Any]] = []
    page_entities = [
        ("alianca-daemon-01", "Ghuls", 18, 28, 0.88),
        ("animalidade", "Feras", 2, 4, 0.86),
        ("gaki", "Gaki", 4, 6, 0.88),
    ]
    for source_id, name, start, end, confidence in page_entities:
        if source_id not in ready_sources:
            continue
        entity = build_pages_entity(source_id, source_lookup, name, start, end, confidence)
        if entity:
            entities.append(entity)

    named_specs = [
        (
            "animalidade",
            [
                "Nagas",
                "Herats",
                "Licantropos",
                "Minotauros",
                "Pantros",
                "Bastet",
                "Defensores do Ragnarok",
                "Garras de Sharikan",
                "Rocs",
                "Croatan",
                "Filhos de Aracne",
            ],
            10,
            13,
            0.82,
            None,
        ),
        (
            "imortal-a-centelha",
            ["Bogatyr", "Chaneque", "Hsien", "Makrobiói", "Neperari", "Sidhichean", "Unwaba-Tulo", "Urlug", "Yamabushi"],
            8,
            30,
            0.82,
            None,
        ),
        (
            "imortal-a-centelha-2",
            ["BOGATYR", "CHANEQUE", "HSIEN", "MAKROBIOI", "SIDHICHEAN", "UNWABA", "URLUG", "YAMABUSHI"],
            6,
            20,
            0.8,
            {"BOGATYR": "Bogatyr", "CHANEQUE": "Chaneque", "HSIEN": "Hsien", "MAKROBIOI": "Makrobiói", "SIDHICHEAN": "Sidhichean", "UNWABA": "Unwaba-Tulo", "URLUG": "Urlug", "YAMABUSHI": "Yamabushi"},
        ),
        (
            "youkai-kyuukai",
            [
                "Watashimori",
                "Shuudouin",
                "Youma",
                "Kagegokai",
                "Shiryou/Mononoke",
                "Akuma",
                "Shouten Kishi",
                "Bouji Tenma",
                "Kazoekirenai",
                "Abareuma",
                "Kuei",
                "Oni",
                "Ponaturi",
                "Kyuuketsuki",
                "Kiang-Shi",
                "Kappa",
                "Gaki",
                "Rakshasa",
                "Heruka",
                "Teyirang",
                "Lagsuyar e Pontianak",
                "Pennangalan",
                "Obake",
                "Yuurei",
                "Ikiryo/Tsukumo",
                "Tatsu",
                "Kouseitan",
                "Hinote",
                "Bikou",
                "Mizu",
                "Kokuei",
                "Chi",
                "Kaze",
                "Dendou",
                "Amanohara",
                "Kei",
                "Chu-ih-yu",
                "Hou-chi",
                "Hisendo",
                "Chi-Mei",
                "Tigbanua",
                "Baoxien",
                "Kyonshe",
                "Shishio",
                "Guerreiro de Terracota",
                "Hengeyokai",
                "Kitsune",
                "Tanuki",
                "Tengu",
                "Reflictys",
                "Wang-wa",
                "Shinma",
                "Vanara",
                "Peri",
                "Kobakama",
                "Shih",
                "Daiphir",
                "Siang",
                "Arahitogami",
                "Hanyu",
                "Lung-Ti Chuan Ren",
                "Kotan-Nukur",
                "Hsien",
                "Yamabushi",
            ],
            7,
            19,
            0.8,
            None,
        ),
    ]
    for source_id, names, start, end, confidence, aliases in named_specs:
        if source_id == "imortal-a-centelha-2" and "imortal-a-centelha" in ready_sources:
            continue
        if source_id not in ready_sources:
            continue
        entities.extend(extract_named_lineages(source_id, source_lookup, names, start, end, confidence, aliases))
    return entities


def extract_from_lines(source_id: str, source_title: str, lines: list[Line], context: str) -> list[dict[str, Any]]:
    headings: list[int] = []
    texts = [line.text for line in lines]
    allow_narrative = "race_lineage" in context or "dedicated-source" in context
    for index, line in enumerate(lines):
        if is_probable_heading(line.text, texts[index + 1:index + 30], allow_narrative):
            headings.append(index)

    entities: list[dict[str, Any]] = []
    seen_names: set[str] = set()
    for pos, start in enumerate(headings):
        end = headings[pos + 1] if pos + 1 < len(headings) else len(lines)
        chunk = lines[start:end]
        name = chunk[0].text
        name_key = slugify(name)
        if name_key in seen_names:
            continue
        entity = build_entity(source_id, source_title, name, chunk, context, "auto-race-heading-pass-1")
        if entity:
            entities.append(entity)
            seen_names.add(name_key)
    return entities


def add_legacy_manual_entities(ready_sources: set[str], source_lookup: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    manual_path = ENTITIES_DIR / "race_lineage.json"
    manual_entities = read_json(manual_path, [])
    if not isinstance(manual_entities, list):
        return []
    entities: list[dict[str, Any]] = []
    for entity in manual_entities:
        source_id = entity.get("source")
        if source_id not in ready_sources:
            continue
        name = str(entity.get("name") or "").strip()
        if not name:
            continue
        body = "\n".join(entry for entry in entity.get("entries", []) if isinstance(entry, str)).strip()
        if len(body) < 45:
            continue
        kind = "linhagem" if "linhagem" in normalize_text(f"{name} {body}") else "raca"
        source_title = source_lookup.get(source_id, {}).get("title", source_id)
        payload = {
            **entity,
            "id": f"raca-{source_id}-{slugify(name)}",
            "category": "race_lineage",
            "subtype": kind,
            "sourceTitle": source_title,
            "pages": [entity["page"]] if isinstance(entity.get("page"), int) else entity.get("pages", []),
            "tags": sorted(set([*entity.get("tags", []), kind, "manual"])),
            "extractionMethod": "manual-race-lineage-pass-1",
            "raceContext": "manual-race-lineage",
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
        lines = split_lines_by_page(text_path.read_text(encoding="utf-8", errors="ignore"))
        if source_is_dedicated(source_id, source_title):
            pages = {line.page for line in lines if line.page}
            if pages:
                candidates_by_source.setdefault(source_id, set()).update(pages)
                candidate_contexts.setdefault(source_id, set()).add("dedicated-source")

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
            if part.get("category") == "race_lineage":
                candidate_contexts.setdefault(source_id, set()).add("race_lineage-book-part")
            else:
                candidate_contexts.setdefault(source_id, set()).add("text-race-term")

    all_entities: list[dict[str, Any]] = []
    per_source: list[dict[str, Any]] = []
    explicit_entities = source_specific_entities(ready_sources, source_lookup)
    all_entities.extend(explicit_entities)
    if explicit_entities:
        per_source.append(
            {
                "source": "_source_specific_race_lineage",
                "candidatePages": [],
                "context": "source-specific-race-lineage",
                "extractedCount": len(explicit_entities),
            }
        )
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

    manual_entities = add_legacy_manual_entities(ready_sources, source_lookup)
    all_entities.extend(manual_entities)
    if manual_entities:
        per_source.append(
            {
                "source": "_manual_race_lineage",
                "candidatePages": [],
                "context": "manual-race-lineage",
                "extractedCount": len(manual_entities),
            }
        )

    unique_entities: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, str]] = set()
    def entity_priority(entity: dict[str, Any]) -> tuple[int, str, int, str]:
        context = str(entity.get("raceContext") or "")
        if "source-specific-race-lineage" in context:
            priority = 0
        elif "manual-race-lineage" in context:
            priority = 1
        else:
            priority = 2
        return (priority, str(entity.get("source") or ""), int(entity.get("page") or 0), str(entity.get("name") or ""))

    for entity in sorted(all_entities, key=entity_priority):
        key = (entity.get("source"), slugify(str(entity.get("name") or "")))
        if key in seen_keys:
            continue
        seen_keys.add(key)
        unique_entities.append(entity)

    write_json(ENTITIES_DIR / "race_lineage_granular.json", sorted(unique_entities, key=lambda item: (item.get("source") or "", item.get("page") or 0, item.get("name") or "")))
    report = {
        "version": 1,
        "candidateSourceCount": len(candidates_by_source),
        "rawExtractedCount": len(all_entities),
        "extractedCount": len(unique_entities),
        "sources": per_source,
    }
    write_json(INDEX_DIR / "granular-racas-report.json", report)

    lines = [
        "# Racas e linhagens granular pass 001",
        "",
        "Varredura das fontes prontas para extrair registros menores de racas e linhagens.",
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
        if len(pages) > 12:
            page_text = f"{pages[0]}-{pages[-1]} ({len(pages)} pages)"
        else:
            page_text = ", ".join(str(page) for page in pages)
        lines.append(f"| `{item['source']}` | {item['extractedCount']} | {item['context']} | {page_text} |")
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "granular-racas-pass-001.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Extracted {len(unique_entities)} raw race/lineage candidates from {len(candidates_by_source)} sources.")


if __name__ == "__main__":
    main()
