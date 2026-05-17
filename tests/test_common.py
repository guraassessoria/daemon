from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from common import infer_category_hints, slugify  # noqa: E402


def test_slugify_removes_accents_and_punctuation() -> None:
    assert slugify("Raças & Linhagens: Dragões!") == "racas-linhagens-dragoes"


def test_infer_category_hints_uses_whole_tokens() -> None:
    assert "combat" not in infer_category_hints("Armario antigo")


def test_infer_category_hints_detects_explicit_terms() -> None:
    assert infer_category_hints("Guia de Magias e Rituais")[:2] == ["power_magic", "ritual_spell"]
