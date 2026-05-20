from __future__ import annotations

from collections.abc import Iterable

from common import INDEX_DIR, slugify, read_json
from audit_entity_highlights import quality_flags


LOCK_FILE_BY_AREA = {
    "aprimoramentos": "aprimoramentos-certified-lock.json",
    "kits": "kits-certified-lock.json",
    "classes": "classes-certified-lock.json",
    "racas": "racas-certified-lock.json",
    "linhagens": "linhagens-certified-lock.json",
    "regras_base": "regras-base-certified-lock.json",
    "poderes": "poderes-certified-lock.json",
    "magias": "magias-certified-lock.json",
    "rituais": "rituais-certified-lock.json",
}

CERTIFICATION_BLOCKING_FLAGS = {
    "empty_display_text",
    "starts_mid_sentence_possible_left_cut",
    "ends_with_connector_possible_cut",
    "too_long_possible_merged_blocks",
    "critical_ocr_gibberish",
    "symbol_noise_ocr",
    "invalid_title_or_ocr_header",
    "front_matter_or_index_block",
    "ocr_corrupted_title_or_body",
    "source_part_without_specific_subject",
}


def lock_source_names(path_name: str) -> set[tuple[str, str]]:
    lock = read_json(INDEX_DIR / path_name, {"records": []})
    return {
        (record["source"], record["nameKey"])
        for record in lock.get("records", [])
        if record.get("source") and record.get("nameKey")
    }


def locked_names_for_areas(areas: Iterable[str]) -> dict[str, set[tuple[str, str]]]:
    return {
        area: lock_source_names(path_name)
        for area in areas
        if (path_name := LOCK_FILE_BY_AREA.get(area))
    }


def first_locked_area(entity: dict, locked_names: dict[str, set[tuple[str, str]]]) -> str | None:
    source_name = (entity.get("source"), slugify(str(entity.get("name") or "")))
    for area, names in locked_names.items():
        if source_name in names:
            return area
    return None


def certification_quality_failure(entity: dict) -> str | None:
    flags = set(quality_flags({**entity, "itemType": "entity"}))
    blocking = sorted(flags & CERTIFICATION_BLOCKING_FLAGS)
    if blocking:
        return f"quality_{blocking[0]}"
    return None
