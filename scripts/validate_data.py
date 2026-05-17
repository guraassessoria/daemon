from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover - exercised in CLI environments.
    raise SystemExit("Missing dependency: install jsonschema to run data validation.") from exc

from common import DATA_DIR, ROOT


ENTITY_SCHEMA = ROOT / "schemas" / "entity.schema.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def entity_records(path: Path) -> list[dict[str, Any]]:
    payload = read_json(path)
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key in ("entities", "items", "records"):
            records = payload.get(key)
            if isinstance(records, list):
                return [item for item in records if isinstance(item, dict)]
    raise ValueError(f"{path} does not contain an entity list")


def validate_entities() -> list[str]:
    schema = read_json(ENTITY_SCHEMA)
    validator = Draft202012Validator(schema)
    errors: list[str] = []

    for path in sorted((DATA_DIR / "entities").glob("*.json")):
        if path.name == ".gitkeep":
            continue
        try:
            records = entity_records(path)
        except Exception as exc:
            errors.append(f"{path}: {exc}")
            continue

        for index, record in enumerate(records):
            for error in validator.iter_errors(record):
                location = ".".join(str(part) for part in error.absolute_path) or "<root>"
                record_id = record.get("id", f"#{index}")
                errors.append(f"{path}:{record_id}:{location}: {error.message}")

    return errors


def validate_json_tree(path: Path) -> list[str]:
    errors: list[str] = []
    for candidate in sorted(path.rglob("*.json")):
        try:
            read_json(candidate)
        except Exception as exc:
            errors.append(f"{candidate}: invalid JSON: {exc}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate generated Daemon Tools data files.")
    parser.add_argument("--json-only", action="store_true", help="Only check JSON syntax, skip entity schema validation.")
    args = parser.parse_args()

    errors = validate_json_tree(DATA_DIR)
    if not args.json_only:
        errors.extend(validate_entities())

    if errors:
        for error in errors[:200]:
            print(error)
        if len(errors) > 200:
            print(f"... {len(errors) - 200} more error(s)")
        raise SystemExit(1)

    print("Data validation passed.")


if __name__ == "__main__":
    main()
