from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_entity_highlights import quality_flags  # noqa: E402


def test_quality_flags_detects_cut_text() -> None:
    flags = quality_flags({"id": "x", "category": "character_option", "entries": ["1 ponto: recebe bônus em todos"]})

    assert "too_short_possible_cut" in flags
    assert "does_not_end_like_complete_sentence" in flags


def test_quality_flags_accepts_complete_cost_entry() -> None:
    flags = quality_flags(
        {
            "id": "aprimoramento-exemplo",
            "subtype": "aprimoramento",
            "entries": ["1 ponto: o personagem recebe um bônus de 10% em testes específicos quando a situação apropriada ocorrer."],
        }
    )

    assert "too_short_possible_cut" not in flags
    assert "aprimoramento_without_cost_marker" not in flags
