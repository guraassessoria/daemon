from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_data import entity_records, validate_json_tree  # noqa: E402


def test_entity_records_reads_plain_entity_list(tmp_path: Path) -> None:
    path = tmp_path / "entities.json"
    path.write_text(json.dumps([{"id": "one"}]), encoding="utf-8")

    assert entity_records(path) == [{"id": "one"}]


def test_entity_records_reads_wrapped_records(tmp_path: Path) -> None:
    path = tmp_path / "entities.json"
    path.write_text(json.dumps({"records": [{"id": "one"}]}), encoding="utf-8")

    assert entity_records(path) == [{"id": "one"}]


def test_entity_records_reads_wrapped_entities_key(tmp_path: Path) -> None:
    path = tmp_path / "entities.json"
    path.write_text(json.dumps({"entities": [{"id": "a"}, {"id": "b"}]}), encoding="utf-8")

    result = entity_records(path)
    assert len(result) == 2


def test_entity_records_skips_non_dicts(tmp_path: Path) -> None:
    path = tmp_path / "entities.json"
    path.write_text(json.dumps([{"id": "ok"}, "string-item", 42]), encoding="utf-8")

    result = entity_records(path)
    assert result == [{"id": "ok"}]


def test_validate_json_tree_detects_invalid_json(tmp_path: Path) -> None:
    bad = tmp_path / "bad.json"
    bad.write_text("{not valid json}", encoding="utf-8")

    errors = validate_json_tree(tmp_path)
    assert any("bad.json" in e for e in errors)


def test_validate_json_tree_passes_valid_files(tmp_path: Path) -> None:
    good = tmp_path / "good.json"
    good.write_text(json.dumps({"ok": True}), encoding="utf-8")

    errors = validate_json_tree(tmp_path)
    assert errors == []


def test_validate_json_tree_empty_directory(tmp_path: Path) -> None:
    assert validate_json_tree(tmp_path) == []


def _build_entities_dir(tmp_path: Path, files: dict[str, list[dict]]) -> Path:
    entities_dir = tmp_path / "entities"
    entities_dir.mkdir()
    for name, records in files.items():
        (entities_dir / name).write_text(json.dumps(records), encoding="utf-8")
    return tmp_path


def test_duplicate_id_detection(tmp_path: Path, monkeypatch: object) -> None:
    _build_entities_dir(tmp_path, {
        "adventure.json": [{"id": "a-assassina", "name": "A Assassina", "category": "adventure", "source": "x", "entries": []}],
        "source.json": [{"id": "a-assassina", "name": "A Assassina", "category": "source", "source": "x", "entries": []}],
    })
    monkeypatch.setattr("validate_data.DATA_DIR", tmp_path)
    monkeypatch.setattr("validate_data.ENTITY_SCHEMA", ROOT / "schemas" / "entity.schema.json")

    from validate_data import validate_entities
    errors = validate_entities()
    duplicate_errors = [e for e in errors if "duplicate ID" in e]
    assert len(duplicate_errors) == 1
    assert "a-assassina" in duplicate_errors[0]


def test_no_duplicate_id_passes(tmp_path: Path, monkeypatch: object) -> None:
    _build_entities_dir(tmp_path, {
        "adventure.json": [{"id": "aventura-1", "name": "A", "category": "adventure", "source": "x", "entries": []}],
        "source.json": [{"id": "fonte-1", "name": "B", "category": "source", "source": "x", "entries": []}],
    })
    monkeypatch.setattr("validate_data.DATA_DIR", tmp_path)
    monkeypatch.setattr("validate_data.ENTITY_SCHEMA", ROOT / "schemas" / "entity.schema.json")

    from validate_data import validate_entities
    errors = validate_entities()
    duplicate_errors = [e for e in errors if "duplicate ID" in e]
    assert duplicate_errors == []
