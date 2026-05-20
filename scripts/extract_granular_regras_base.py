from __future__ import annotations

import re
from collections import Counter
from typing import Any

from common import DATA_DIR, ROOT, slugify, read_json, write_json
from build_area_catalog import ready_source_ids
from editorial_classifier import is_probably_ocr_noise, normalize_spaces


BOOKS_DATA_DIR = DATA_DIR / "books"
ENTITIES_PATH = DATA_DIR / "entities" / "regras_base_granular.json"
REPORT_PATH = ROOT / "docs" / "reports" / "granular" / "granular-regras-base-pass-001.md"

VALID_CATEGORIES = {"core_rule", "attribute_skill", "combat"}
BAD_TITLES = {
    "agradecimentos",
    "bibliografia",
    "capitulo",
    "creditos",
    "download",
    "indice",
    "introducao",
    "pagina inicial",
    "prefacio",
    "sumario",
}
MECHANICAL_RE = re.compile(
    r"\b(?:regra|regras|sistema|teste|testes|atributo|atributos|per[ií]cia|per[ií]cias|"
    r"especializa[cç][aã]o|combate|dano|ferimentos|pontos?|modificadores?|penalidade|"
    r"b[oô]nus|dificuldade|resolu[cç][aã]o|cria[cç][aã]o de personagem|iniciativa|"
    r"ataque|defesa|manobra|manobras|experi[eê]ncia|aprendizado|n[ií]vel)\b",
    re.IGNORECASE,
)
SECTION_ALLOW_RE = re.compile(
    r"\b(?:conceitos?\s+b[aá]sicos?|atributos?(?:\s+b[aá]sicos?)?|per[ií]cias?|"
    r"regras?\s+e\s+testes?|testes?|combate|dano|ferimentos|experi[eê]ncia|"
    r"cria[cç][aã]o\s+de\s+personagem|manobras?)\b",
    re.IGNORECASE,
)


def normalize_key(value: str) -> str:
    return slugify(value).replace("-", " ")


def expand_pages(pages: list[Any]) -> list[int]:
    result: set[int] = set()
    for page in pages:
        if isinstance(page, int):
            result.add(page)
        elif isinstance(page, list) and len(page) == 2 and all(isinstance(item, int) for item in page):
            result.update(range(page[0], page[1] + 1))
    return sorted(result)


def source_part_is_candidate(part: dict[str, Any]) -> bool:
    category = part.get("category")
    if category not in VALID_CATEGORIES:
        return False
    name = normalize_spaces(str(part.get("name") or ""))
    summary = normalize_spaces(str(part.get("summary") or ""))
    normalized_name = normalize_key(name)
    text = f"{name} {summary}"
    if not name or normalized_name in BAD_TITLES:
        return False
    if len(summary) < 45:
        return False
    if is_probably_ocr_noise(name, text):
        return False
    return bool(MECHANICAL_RE.search(text) or SECTION_ALLOW_RE.search(name))


def tags_for(category: str, text: str) -> list[str]:
    normalized = normalize_key(text)
    tags = {"regras-base", "auto-extraido", category}
    for tag, words in {
        "atributos": ["atributo", "atributos"],
        "pericias": ["pericia", "pericias", "especializacao", "especializacoes"],
        "combate": ["combate", "ataque", "defesa", "dano", "manobra", "manobras", "ferimentos"],
        "testes": ["teste", "testes", "dificuldade"],
        "experiencia": ["experiencia", "aprendizado", "nivel"],
    }.items():
        if any(word in normalized for word in words):
            tags.add(tag)
    return sorted(tags)


def main() -> None:
    source_ids = set(ready_source_ids())
    records: list[dict[str, Any]] = []
    skipped = Counter()

    for source_id in sorted(source_ids):
        book = read_json(BOOKS_DATA_DIR / f"{source_id}.json", {})
        source_title = str(book.get("title") or source_id)
        for part in book.get("parts", []):
            if not source_part_is_candidate(part):
                skipped[str(part.get("category") or "unknown")] += 1
                continue
            name = normalize_spaces(str(part.get("name") or part.get("id") or "Regra"))
            summary = normalize_spaces(str(part.get("summary") or ""))
            pages = expand_pages(part.get("pages") or [])
            part_id = slugify(str(part.get("id") or name))
            category = str(part.get("category") or "core_rule")
            records.append(
                {
                    "id": f"regra-{source_id}-{part_id}",
                    "name": name,
                    "category": category,
                    "source": source_id,
                    "page": pages[0] if pages else None,
                    "pages": pages,
                    "entries": [summary],
                    "tags": tags_for(category, f"{name} {summary}"),
                    "confidence": 0.82 if category == "core_rule" else 0.8,
                    "extractionMethod": "regras-base-book-part-pass-1",
                    "rulesContext": f"book-part-category:{category}",
                    "sourceTitle": source_title,
                }
            )

    write_json(ENTITIES_PATH, records)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    by_category = Counter(record["category"] for record in records)
    lines = [
        "# Regras Base granular pass 001",
        "",
        f"- Ready sources scanned: {len(source_ids)}",
        f"- Raw regras base candidates: {len(records)}",
        "",
        "## Candidates by category",
        "",
        "| Category | Count |",
        "| --- | ---: |",
    ]
    for category, count in by_category.most_common():
        lines.append(f"| `{category}` | {count} |")
    lines.extend(["", "## Skipped source parts by original category", "", "| Category | Count |", "| --- | ---: |"])
    for category, count in skipped.most_common():
        lines.append(f"| `{category}` | {count} |")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Extracted {len(records)} raw regras base candidates from {len(source_ids)} sources.")


if __name__ == "__main__":
    main()
