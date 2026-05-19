from __future__ import annotations

import re
from typing import Any

TEXT_FIELDS = [
    "entries",
    "summary",
    "costText",
    "requirements",
    "skillsText",
    "attributesText",
    "advantagesText",
    "disadvantagesText",
    "aprimoramentosText",
    "classContext",
    "raceContext",
    "powerMagicContext",
    "ritualContext",
]

CRITICAL_PRESENTATION_FLAGS = {
    "invalid_title_or_ocr_header",
    "critical_ocr_gibberish",
    "symbol_noise_ocr",
    "front_matter_or_index_block",
    "generic_chapter_or_page_block",
    "source_part_without_specific_subject",
    "ocr_corrupted_title_or_body",
    "raw_source_part_requires_review",
    "manual_quarantine",
}

GIBBERISH_RE = re.compile(
    r"(?:\b[0-9oO]{5,}\b|[oO0]{6,}|[A-Za-z]{0,3}'{3,}[A-Za-z]{0,3}|[\\/_~]{3,}|[<>]{2,}|\b(?:IVOO|Kaoooo|Pooooo|Puoooo|Booooo)\b)",
    re.IGNORECASE,
)
BAD_TITLE_RE = re.compile(
    r"^(?:[0-9oO]{5,}|[oO0]{5,}|[\W_]+|\d+\s*[-–]\s*\d+|p[aá]gina\s+\d+)(?:\s*\(.*\))?$",
    re.IGNORECASE,
)
SYMBOL_CLUSTER_RE = re.compile(r"[\\/_~^`|<>]{2,}|\.{5,}|'{4,}|\"{4,}")
FRONT_MATTER_RE = re.compile(
    r"\b(?:cr[eé]ditos|agradecimentos|diagrama[cç][aã]o|arte\s+interna|capa|autores?\s+originais?|[ií]ndice)\b",
    re.IGNORECASE,
)
MECHANICAL_WORD_RE = re.compile(
    r"\b(?:custo|per[ií]cias|aprimoramentos|requisitos?|benef[ií]cio|especial|sistema|efeito|dura[cç][aã]o|alcance|dano|ataque|defesa|atributos|pontos?|magia|poder|ritual|classe|ra[cç]a)\b",
    re.IGNORECASE,
)
LETTER_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]")
VISIBLE_RE = re.compile(r"\S")


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def text_for_record(record: dict[str, Any]) -> str:
    values: list[str] = []
    for field in TEXT_FIELDS:
        value = record.get(field)
        if isinstance(value, list):
            values.extend(str(item) for item in value if item)
        elif value:
            values.append(str(value))
    return "\n".join(values)


def alpha_ratio(text: str) -> float:
    visible = len(VISIBLE_RE.findall(text))
    if not visible:
        return 0.0
    return len(LETTER_RE.findall(text)) / visible


def symbol_noise_ratio(text: str) -> float:
    visible = max(1, len(VISIBLE_RE.findall(text)))
    noisy = len(re.findall(r"[\\/_~^`|<>]", text)) + len(re.findall(r"'{3,}|\"{3,}|\.{4,}", text)) * 3
    return noisy / visible


def has_critical_gibberish(text: str) -> bool:
    compact = normalize_spaces(text)
    if not compact:
        return False
    if GIBBERISH_RE.search(compact):
        return True
    if len(compact) >= 160 and alpha_ratio(compact) < 0.48 and symbol_noise_ratio(compact) > 0.035:
        return True
    if len(SYMBOL_CLUSTER_RE.findall(compact)) >= 3 and alpha_ratio(compact) < 0.70:
        return True
    return False


def title_is_bad(title: str) -> bool:
    value = normalize_spaces(title)
    if not value:
        return True
    if BAD_TITLE_RE.match(value):
        return True
    if re.fullmatch(r"sum[aá]rio|[ií]ndice", value, flags=re.IGNORECASE):
        return True
    if re.search(r"\.{4,}\s*$", value):
        return True
    if len(value) <= 3 and not re.search(r"[A-Za-zÀ-ÖØ-öø-ÿ]{2,}", value):
        return True
    if has_critical_gibberish(value) and not MECHANICAL_WORD_RE.search(value):
        return True
    return False


def is_front_matter_block(record: dict[str, Any], compact: str) -> bool:
    if record.get("itemType") != "sourcePart":
        return False
    name = normalize_spaces(str(record.get("name") or ""))
    page = record.get("page")
    pages = record.get("pages")
    first_page = None
    if isinstance(page, int):
        first_page = page
    elif isinstance(pages, list) and pages:
        first = pages[0]
        if isinstance(first, int):
            first_page = first
        elif isinstance(first, list) and first:
            first_page = first[0]
    early = first_page is None or first_page <= 8
    front_hits = len(FRONT_MATTER_RE.findall(f"{name} {compact}"))
    has_rule_signal = bool(MECHANICAL_WORD_RE.search(compact))
    return early and front_hits >= 2 and not has_rule_signal


def presentation_flags(record: dict[str, Any]) -> list[str]:
    flags: list[str] = []
    name = str(record.get("name") or "")
    text = text_for_record(record)
    compact = normalize_spaces(text)
    if record.get("category") != "source" and title_is_bad(name):
        flags.append("invalid_title_or_ocr_header")
    if has_critical_gibberish(f"{name} {compact}"):
        flags.append("critical_ocr_gibberish")
    if len(compact) >= 120 and symbol_noise_ratio(compact) > 0.06:
        flags.append("symbol_noise_ocr")
    if is_front_matter_block(record, compact):
        flags.append("front_matter_or_index_block")
    return sorted(set(flags))


def is_quarantined(record: dict[str, Any], flags: list[str] | None = None) -> bool:
    record_flags = set(flags if flags is not None else presentation_flags(record))
    # Entidades da área Fontes são a ficha bibliográfica do livro e devem permanecer.
    # Trechos de livro dentro de Fontes, porém, podem ser ruído de OCR e devem ir para quarentena.
    if (record.get("category") == "source" or record.get("area") == "fontes") and record.get("itemType") != "sourcePart":
        return False
    if record_flags & CRITICAL_PRESENTATION_FLAGS:
        return True
    return False


def presentation_status(record: dict[str, Any], flags: list[str] | None = None) -> str:
    return "quarantine" if is_quarantined(record, flags) else "public"
