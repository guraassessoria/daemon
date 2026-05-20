from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from catalog_processor import aprimoramento_subgroup  # noqa: E402
from catalog_loader import normalize_uppercase_name, normalize_uppercase_text  # noqa: E402
from extract_granular_aprimoramentos import Line, apply_source_fixes  # noqa: E402


def test_aprimoramento_subgroup_detects_negative_cost() -> None:
    subgroup, label, tag = aprimoramento_subgroup(
        {
            "name": "Marcado",
            "entries": ["- 2 pontos: sua marca e dificil de ocultar."],
            "costs": [],
        }
    )

    assert subgroup == "aprimoramentos_negativos"
    assert label == "Aprimoramentos Negativos"
    assert tag == "aprimoramento-negativo"


def test_aprimoramento_subgroup_defaults_to_positive() -> None:
    subgroup, label, tag = aprimoramento_subgroup(
        {
            "name": "Acrobatico",
            "entries": ["2 PONTOS: recebe bonus em testes de acrobacia."],
            "costs": ["2 pontos"],
        }
    )

    assert subgroup == "aprimoramentos_positivos"
    assert label == "Aprimoramentos Positivos"
    assert tag == "aprimoramento-positivo"


def test_aprimoramento_subgroup_uses_first_cost_marker() -> None:
    subgroup, label, tag = aprimoramento_subgroup(
        {
            "name": "Canalizador",
            "entries": [
                "2 pontos: troca PV por magia. 4 pontos: melhora a troca. Texto colado -1 ponto: outro aprimoramento."
            ],
            "costs": ["1 ponto", "2 pontos", "4 pontos"],
        }
    )

    assert subgroup == "aprimoramentos_positivos"
    assert label == "Aprimoramentos Positivos"
    assert tag == "aprimoramento-positivo"


def test_aprimoramentos_3_source_fix_splits_sono_leve_and_armas_de_fogo() -> None:
    entities = [
        {
            "id": "aprimoramento-aprimoramentos-3-sono-leve",
            "name": "Sono Leve",
            "source": "aprimoramentos-3",
            "page": 4,
            "entries": ["1 ponto: acorda facil.\nAprimoramentos\nSociais\nArmas de Fogo\ntexto colado"],
        }
    ]
    lines = [
        Line(4, "Sono Leve"),
        Line(4, "1 ponto: acorda facil."),
        Line(4, "Aprimoramentos"),
        Line(4, "Sociais"),
        Line(4, "Armas de Fogo"),
        Line(4, "Nao importa a origem."),
        Line(4, "1 ponto: revolver."),
        Line(5, "2 pontos: submetralhadoras."),
        Line(5, "3 pontos: militares."),
        Line(5, "Contatos e Aliados"),
    ]

    fixed = apply_source_fixes("aprimoramentos-3", "Aprimoramentos 3", lines, entities)
    by_id = {entity["id"]: entity for entity in fixed}

    assert by_id["aprimoramento-aprimoramentos-3-sono-leve"]["entries"] == ["1 ponto: acorda facil."]
    assert by_id["aprimoramento-aprimoramentos-3-armas-de-fogo"]["name"] == "Armas de Fogo"
    assert by_id["aprimoramento-aprimoramentos-3-armas-de-fogo"]["pages"] == [4, 5]


def test_normalize_uppercase_name_uses_title_case_with_particles() -> None:
    assert normalize_uppercase_name("ACERTO CRÍTICO APRIMORADO") == "Acerto Crítico Aprimorado"
    assert normalize_uppercase_name("ACUIDADE COM ARMA") == "Acuidade com Arma"


def test_normalize_uppercase_text_keeps_common_rpg_acronyms() -> None:
    text = normalize_uppercase_text("1 PONTO: O PERSONAGEM GANHA +3 PVS E IP NATURAL.")

    assert text == "1 ponto: o personagem ganha +3 PVs e IP natural."
