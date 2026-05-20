from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from presentation_quality import (  # noqa: E402
    alpha_ratio,
    has_critical_gibberish,
    presentation_flags,
    presentation_status,
    symbol_noise_ratio,
    title_is_bad,
)


# --- alpha_ratio ---

def test_alpha_ratio_all_letters() -> None:
    assert alpha_ratio("abc") == 1.0


def test_alpha_ratio_mixed_text() -> None:
    ratio = alpha_ratio("abc123")
    assert 0.0 < ratio < 1.0


def test_alpha_ratio_empty_string() -> None:
    assert alpha_ratio("") == 0.0


def test_alpha_ratio_only_spaces() -> None:
    assert alpha_ratio("   ") == 0.0


# --- symbol_noise_ratio ---

def test_symbol_noise_ratio_clean_text() -> None:
    assert symbol_noise_ratio("texto limpo sem ruido") < 0.01


def test_symbol_noise_ratio_noisy_text() -> None:
    assert symbol_noise_ratio("abc\\\\// ~~~ |||") > 0.1


# --- has_critical_gibberish ---

def test_has_critical_gibberish_detects_ocr_repetition() -> None:
    assert has_critical_gibberish("9oooooo o ( oo ooo''''oooooooooo")


def test_has_critical_gibberish_clean_text() -> None:
    assert not has_critical_gibberish("Aprimoramento de Força: 2 pontos")


def test_has_critical_gibberish_empty() -> None:
    assert not has_critical_gibberish("")


# --- title_is_bad ---

def test_title_is_bad_empty() -> None:
    assert title_is_bad("")


def test_title_is_bad_ocr_pattern() -> None:
    assert title_is_bad("9ooooooo")


def test_title_is_bad_page_range() -> None:
    assert title_is_bad("12-34")


def test_title_is_bad_valid_title() -> None:
    assert not title_is_bad("Combate Corpo a Corpo")


def test_title_is_bad_valid_short_acronym() -> None:
    assert not title_is_bad("NPC")


# --- presentation_flags ---

def test_presentation_quality_quarantines_gibberish_title() -> None:
    record = {
        "itemType": "sourcePart",
        "name": "9oooooo (3-12)",
        "summary": "9oooooo o ( oo ooo''''oooooooooooo Tagmar-Daemon texto quebrado",
    }
    flags = presentation_flags(record)
    assert "invalid_title_or_ocr_header" in flags
    assert "critical_ocr_gibberish" in flags
    assert presentation_status(record, flags) == "quarantine"


def test_presentation_quality_preserves_source_entity() -> None:
    record = {
        "itemType": "entity",
        "area": "fontes",
        "category": "source",
        "name": "Livro Exemplo",
        "entries": ["Fonte processada para consulta digital."],
    }
    assert presentation_status(record, presentation_flags(record)) == "public"


def test_presentation_flags_clean_entity_has_no_flags() -> None:
    record = {
        "itemType": "entity",
        "name": "Força Sobrenatural",
        "entries": ["Permite ao personagem realizar feitos físicos além do normal."],
        "category": "character_option",
    }
    flags = presentation_flags(record)
    assert flags == []


def test_presentation_flags_front_matter_detected() -> None:
    record = {
        "itemType": "sourcePart",
        "name": "Créditos",
        "page": 2,
        "summary": "Créditos e agradecimentos ao autor e ao ilustrador desta obra.",
    }
    flags = presentation_flags(record)
    assert "front_matter_or_index_block" in flags


def test_presentation_flags_symbol_noise_detected() -> None:
    # symbol_noise_ocr exige len(compact) >= 120 chars visíveis E noise_ratio > 0.06
    noisy_text = "texto normal " + "\\/" * 70 + " fim do bloco"
    record = {
        "itemType": "sourcePart",
        "name": "Secao Normal",
        "summary": noisy_text,
    }
    flags = presentation_flags(record)
    assert "symbol_noise_ocr" in flags or "critical_ocr_gibberish" in flags


def test_presentation_status_public_for_warning_severity() -> None:
    record = {
        "itemType": "entity",
        "name": "Poder Válido",
        "entries": ["Descrição curta."],
        "category": "power_magic",
    }
    assert presentation_status(record, presentation_flags(record)) == "public"
