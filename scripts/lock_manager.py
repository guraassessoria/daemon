"""LockManager — carrega e indexa arquivos de certificação por tipo de entidade.

Cenário B de refatoração: extrai a lógica de lock para módulo dedicado.
Pode substituir as funções *_locks() em build_area_catalog.py e ser reutilizado
pelos scripts certify_*.py sem duplicação de código.

Uso:
    from lock_manager import LockManager
    lm = LockManager()
    by_id, by_source_name = lm.load("aprimoramentos")
    is_certified = entity_id in by_id
"""
from __future__ import annotations

from typing import Any

from common import INDEX_DIR, read_json

LOCK_FILES: dict[str, str] = {
    "aprimoramentos": "aprimoramentos-certified-lock.json",
    "kits": "kits-certified-lock.json",
    "classes": "classes-certified-lock.json",
    "racas": "racas-certified-lock.json",
    "linhagens": "linhagens-certified-lock.json",
    "poderes": "poderes-certified-lock.json",
    "magias": "magias-certified-lock.json",
    "rituais": "rituais-certified-lock.json",
    "regras_base": "regras-base-certified-lock.json",
}

LockById = dict[str, dict[str, Any]]
LockBySourceName = dict[tuple[str, str], dict[str, Any]]


class LockManager:
    def __init__(self) -> None:
        self._cache: dict[str, tuple[LockById, LockBySourceName]] = {}

    def load(self, entity_type: str) -> tuple[LockById, LockBySourceName]:
        if entity_type not in self._cache:
            self._cache[entity_type] = _parse_lock_file(entity_type)
        return self._cache[entity_type]

    def load_all(self) -> dict[str, tuple[LockById, LockBySourceName]]:
        for entity_type in LOCK_FILES:
            self.load(entity_type)
        return dict(self._cache)

    def is_certified(self, entity_type: str, entity_id: str) -> bool:
        by_id, _ = self.load(entity_type)
        return entity_id in by_id

    def is_duplicate(self, entity_type: str, source_id: str, name_key: str) -> str | None:
        _, by_source_name = self.load(entity_type)
        record = by_source_name.get((source_id, name_key))
        return record["id"] if record else None

    def invalidate(self, entity_type: str | None = None) -> None:
        if entity_type is None:
            self._cache.clear()
        else:
            self._cache.pop(entity_type, None)


def _parse_lock_file(entity_type: str) -> tuple[LockById, LockBySourceName]:
    lock_file = LOCK_FILES[entity_type]
    lock = read_json(INDEX_DIR / lock_file, {"records": []})
    by_id: LockById = {}
    by_source_name: LockBySourceName = {}
    for record in lock.get("records", []):
        if not record.get("id") or not record.get("source") or not record.get("nameKey"):
            continue
        by_id[record["id"]] = record
        by_source_name[(record["source"], record["nameKey"])] = record
    return by_id, by_source_name
