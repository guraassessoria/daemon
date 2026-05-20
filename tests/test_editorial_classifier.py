from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from editorial_classifier import (  # noqa: E402
    classify_source_part,
    content_kind_for_entity,
    infer_content_kind,
    is_generic_or_raw_title,
    is_specific_consultable_title,
)


# --- is_generic_or_raw_title ---

def test_generic_title_capitulo() -> None:
    assert is_generic_or_raw_title("Capítulo 3", "Livro Teste")


def test_generic_title_sumario() -> None:
    assert is_generic_or_raw_title("Sumário", "Livro Teste")


def test_generic_title_numeric_range() -> None:
    assert is_generic_or_raw_title("12-34", "Livro Teste")


def test_non_generic_title() -> None:
    assert not is_generic_or_raw_title("Força Sobrenatural", "Livro Teste")


def test_title_matching_source_name_is_generic() -> None:
    assert is_generic_or_raw_title("A Assassina", "A Assassina")


# --- is_specific_consultable_title ---

def test_specific_title_valid() -> None:
    # Títulos iniciados com 2+ letras maiúsculas consecutivas são reconhecidos como específicos
    assert is_specific_consultable_title("NPC Especial do Cenário", "Manual de Regras")


def test_specific_title_too_short() -> None:
    assert not is_specific_consultable_title("AA", "Livro Teste")


def test_specific_title_ends_with_colon() -> None:
    assert not is_specific_consultable_title("Aprimoramento:", "Livro Teste")


def test_specific_title_slug_in_generic_set() -> None:
    assert not is_specific_consultable_title("Aventura", "Livro Teste")


def test_specific_title_url_is_invalid() -> None:
    assert not is_specific_consultable_title("https://example.com/regras", "Livro")


# --- infer_content_kind ---

def test_infer_content_kind_ocr_noise() -> None:
    item = {"name": "9ooooo (2-5)", "summary": "9oooo o ( oo ooo''''oooo texto quebrado"}
    kind, flags = infer_content_kind(item, "Livro")
    assert kind == "ocr_noise"
    assert "ocr_corrupted_title_or_body" in flags


def test_infer_content_kind_front_matter() -> None:
    item = {
        "name": "Créditos",
        "summary": "Créditos e agradecimentos ao autor e ao ilustrador da obra.",
    }
    kind, flags = infer_content_kind(item, "Livro")
    assert kind == "front_matter"


def test_infer_content_kind_power_spell() -> None:
    item = {
        "name": "Bola de Fogo",
        "summary": "Magia de círculo 3. Custo: 3 pontos. Efeito: dano em área.",
    }
    kind, _ = infer_content_kind(item, "Grimório")
    assert kind == "power_spell"


def test_infer_content_kind_creature_npc() -> None:
    item = {
        "name": "Demônio Menor",
        "summary": "CON 14, FR 12, DEX 10. PVs 30. IP 4. Criatura do plano sombrio.",
    }
    kind, _ = infer_content_kind(item, "Bestiário")
    assert kind == "creature_npc"


def test_infer_content_kind_combat() -> None:
    # Usa termos de manobra/esquiva sem mencionar 'dano' (que ativaria item_equipment primeiro)
    item = {
        "name": "Esquiva Perfeita",
        "summary": "Manobra de combate. Teste de defesa com esquiva. Penalidade -2 para o ataque.",
    }
    kind, _ = infer_content_kind(item, "Regras de Combate")
    assert kind == "combat_maneuver"


def test_infer_content_kind_item_equipment() -> None:
    item = {
        "name": "Espada Longa",
        "summary": "Arma corpo a corpo. Dano: 1d6. Preço: 50 moedas. Peso: 3kg.",
    }
    kind, _ = infer_content_kind(item, "Equipamentos")
    assert kind == "item_equipment"


def test_infer_content_kind_rule_mechanic() -> None:
    item = {
        "name": "Testes de Habilidade",
        "summary": "Custo: N/A. Requisitos: nenhum. Sistema de testes com atributos.",
    }
    kind, _ = infer_content_kind(item, "Regras Básicas")
    assert kind == "rule_mechanic"


def test_infer_content_kind_raw_chapter_for_generic_title() -> None:
    item = {"name": "Capítulo 5", "summary": "Texto genérico sobre regras gerais."}
    kind, flags = infer_content_kind(item, "Manual Completo")
    assert kind == "raw_chapter_block"
    assert "generic_chapter_or_page_block" in flags


# --- classify_source_part ---

def test_classify_source_part_adds_review_status() -> None:
    item = {"name": "Capítulo 1", "summary": "Introdução ao sistema."}
    result = classify_source_part(item, "Manual")
    assert result["editorialStatus"] == "raw_review"
    assert result["presentationStatusHint"] == "quarantine"
    assert "raw_source_part_requires_review" in result["editorialFlags"]


def test_classify_source_part_has_content_kind_label() -> None:
    item = {
        "name": "Bola de Fogo",
        "summary": "Magia de círculo 3. Custo: 3 pontos. Efeito: dano em área.",
    }
    result = classify_source_part(item, "Grimório")
    assert "contentKind" in result
    assert "contentKindLabel" in result
    assert result["contentKindLabel"]


# --- content_kind_for_entity ---

def test_content_kind_for_source_catalog() -> None:
    item = {"area": "fontes", "category": "source"}
    result = content_kind_for_entity(item)
    assert result["contentKind"] == "source_catalog"


def test_content_kind_for_character_option() -> None:
    item = {"area": "aprimoramentos", "subtype": "aprimoramento"}
    result = content_kind_for_entity(item)
    assert result["contentKind"] == "character_option"


def test_content_kind_for_power_spell() -> None:
    item = {"area": "poderes", "subtype": "poder"}
    result = content_kind_for_entity(item)
    assert result["contentKind"] == "power_spell"


def test_content_kind_defaults_to_rule_mechanic() -> None:
    item = {"area": "unknown_area"}
    result = content_kind_for_entity(item)
    assert result["contentKind"] == "rule_mechanic"


def test_content_kind_includes_label() -> None:
    item = {"area": "criaturas_npcs"}
    result = content_kind_for_entity(item)
    assert result["contentKind"] == "creature_npc"
    assert result["contentKindLabel"]
