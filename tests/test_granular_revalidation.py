from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_entity_highlights import quality_flags  # noqa: E402
from common import DATA_DIR, read_json  # noqa: E402
from granular_validation import CERTIFICATION_BLOCKING_FLAGS, certification_quality_failure  # noqa: E402
from revalidate_granular_from_zero import ORDERED_STEPS  # noqa: E402


VALIDATED_AREAS = {
    "aprimoramentos",
    "kits",
    "classes",
    "racas",
    "linhagens",
    "regras_base",
    "poderes",
    "magias",
    "rituais",
}


def test_full_revalidation_order_keeps_lock_priority() -> None:
    order = [area for area, _, _ in ORDERED_STEPS]

    assert order.index("aprimoramentos") < order.index("kits")
    assert order.index("kits") < order.index("racas_linhagens")
    assert order.index("racas_linhagens") < order.index("regras_base")
    assert order.index("regras_base") < order.index("poderes_magias")
    assert order.index("poderes_magias") < order.index("rituais")


def test_certification_quality_failure_blocks_hard_cut_text() -> None:
    failure = certification_quality_failure(
        {
            "name": "Entrada Cortada",
            "entries": [
                "1 ponto: esta entrada tem texto suficiente para parecer uma regra, mas termina em conector para"
            ],
        }
    )

    assert failure == "quality_ends_with_connector_possible_cut"


def test_certification_quality_failure_allows_complete_rule_text() -> None:
    failure = certification_quality_failure(
        {
            "name": "Entrada Completa",
            "entries": [
                "1 ponto: esta entrada descreve uma regra completa com custo, efeito e uma frase encerrada corretamente."
            ],
        }
    )

    assert failure is None


def test_validated_area_entities_have_no_blocking_quality_flags() -> None:
    failures: list[str] = []
    for path in sorted((DATA_DIR / "areas").glob("*.json")):
        area = path.stem
        if area not in VALIDATED_AREAS:
            continue
        payload = read_json(path, {})
        for kind in ("entities", "sourceParts"):
            for record in payload.get(kind, []) or []:
                flags = set(quality_flags({**record, "itemType": "entity" if kind == "entities" else "sourcePart"}))
                blocking = sorted(flags & CERTIFICATION_BLOCKING_FLAGS)
                if blocking:
                    failures.append(f"{area}:{record.get('id') or record.get('name')}:{','.join(blocking)}")

    assert failures == []
