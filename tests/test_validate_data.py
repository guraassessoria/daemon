from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_data import entity_records  # noqa: E402


def test_entity_records_reads_plain_entity_list(tmp_path: Path) -> None:
    path = tmp_path / "entities.json"
    path.write_text(json.dumps([{"id": "one"}]), encoding="utf-8")

    assert entity_records(path) == [{"id": "one"}]


def test_entity_records_reads_wrapped_records(tmp_path: Path) -> None:
    path = tmp_path / "entities.json"
    path.write_text(json.dumps({"records": [{"id": "one"}]}), encoding="utf-8")

    assert entity_records(path) == [{"id": "one"}]
