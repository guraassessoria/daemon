from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from common import infer_category_hints, read_json, sha256_file, slugify, write_json  # noqa: E402


def test_slugify_removes_accents_and_punctuation() -> None:
    assert slugify("Raças & Linhagens: Dragões!") == "racas-linhagens-dragoes"


def test_slugify_returns_untitled_for_empty_string() -> None:
    assert slugify("") == "untitled"
    assert slugify("!!!") == "untitled"


def test_slugify_lowercases_and_replaces_spaces() -> None:
    assert slugify("Criaturas e Monstros") == "criaturas-e-monstros"


def test_infer_category_hints_uses_whole_tokens() -> None:
    assert "combat" not in infer_category_hints("Armario antigo")


def test_infer_category_hints_detects_explicit_terms() -> None:
    assert infer_category_hints("Guia de Magias e Rituais")[:2] == ["power_magic", "ritual_spell"]


def test_infer_category_hints_returns_source_as_fallback() -> None:
    result = infer_category_hints("texto sem palavras conhecidas xyzabc")
    assert result == ["source"]


def test_sha256_file_matches_hashlib(tmp_path: Path) -> None:
    content = b"conteudo de teste para hash"
    file = tmp_path / "file.bin"
    file.write_bytes(content)
    expected = hashlib.sha256(content).hexdigest()
    assert sha256_file(file) == expected


def test_sha256_file_handles_empty_file(tmp_path: Path) -> None:
    file = tmp_path / "empty.bin"
    file.write_bytes(b"")
    expected = hashlib.sha256(b"").hexdigest()
    assert sha256_file(file) == expected


def test_write_json_creates_parent_dirs(tmp_path: Path) -> None:
    target = tmp_path / "nested" / "deep" / "output.json"
    payload = {"key": "value", "number": 42}
    write_json(target, payload)
    assert target.exists()
    loaded = json.loads(target.read_text(encoding="utf-8"))
    assert loaded == payload


def test_write_json_uses_utf8_and_pretty_format(tmp_path: Path) -> None:
    target = tmp_path / "output.json"
    write_json(target, {"nome": "Raças e Linhagens"})
    raw = target.read_text(encoding="utf-8")
    assert "Raças e Linhagens" in raw
    assert "\n" in raw


def test_read_json_returns_default_when_missing(tmp_path: Path) -> None:
    missing = tmp_path / "nonexistent.json"
    assert read_json(missing, []) == []
    assert read_json(missing, {"a": 1}) == {"a": 1}


def test_read_json_parses_existing_file(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_text(json.dumps({"x": 99}), encoding="utf-8")
    assert read_json(path, {}) == {"x": 99}
