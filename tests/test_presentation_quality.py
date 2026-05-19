from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from presentation_quality import presentation_flags, presentation_status  # noqa: E402


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
