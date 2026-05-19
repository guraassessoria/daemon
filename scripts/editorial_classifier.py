from __future__ import annotations

import re
from typing import Any

from common import slugify

CONTENT_KIND_LABELS: dict[str, str] = {
    "source_catalog": "Ficha de fonte/livro",
    "rule_mechanic": "Regra ou mecânica",
    "character_option": "Opção de personagem",
    "power_spell": "Poder, magia ou ritual",
    "combat_maneuver": "Combate ou manobra",
    "item_equipment": "Item, equipamento ou material",
    "creature_npc": "Criatura, inimigo ou NPC",
    "lore_world": "História, mundo ou cenário",
    "organization_faction": "Organização, facção ou culto",
    "adventure_scene": "Aventura, cena ou campanha",
    "table_reference": "Tabela ou referência",
    "raw_chapter_block": "Capítulo/página bruto",
    "front_matter": "Créditos, índice ou metadado",
    "ocr_noise": "OCR/lixo de extração",
    "uncertain_fragment": "Fragmento incerto",
}

PUBLIC_CONTENT_KINDS = {
    "source_catalog",
    "rule_mechanic",
    "character_option",
    "power_spell",
    "combat_maneuver",
    "item_equipment",
    "creature_npc",
    "lore_world",
    "organization_faction",
    "adventure_scene",
    "table_reference",
}

GENERIC_TITLE_RE = re.compile(
    r"^(?:"
    r"cap[ií]tulo(?:\s+\d+)?(?:\s*[-–:])?|"
    r"parte\s+\d+(?:\s*[-–:])?|"
    r"p[aá]gina(?:\s+inicial)?|"
    r"page|"
    r"sum[aá]rio|[ií]ndice|editorial|introdu[cç][aã]o|"
    r"cr[eé]ditos|agradecimentos|bibliografia|licen[cç]a|download|"
    r"estrutura\s+do\s+texto|aten[cç][aã]o!?"
    r")\b",
    re.IGNORECASE,
)

BROAD_SECTION_RE = re.compile(
    r"^(?:"
    r"regras|combate|atributos|per[ií]cias|lista\s+de\s+per[ií]cias|"
    r"cria[cç][aã]o\s+de\s+personagens?|matem[aá]tica\s+de\s+jogo|"
    r"sequ[eê]ncia\s+de\s+cria[cç][aã]o|personagens?|powers?|magias?|rituais?|"
    r"itens?|equipamentos?|armas?|monstros?|criaturas?"
    r")(?:\s*[!:.-]*\s*)$",
    re.IGNORECASE,
)

PAGE_RANGE_TITLE_RE = re.compile(r"\(\s*\d{1,4}\s*[-–]\s*\d{1,4}\s*\)\s*$")
URL_RE = re.compile(r"https?://|www\.", re.IGNORECASE)

GENERIC_TITLE_SLUGS = {
    "aventura", "aventuras", "campanha", "campanhas", "experiencia", "experiencias",
    "historia", "a-historia", "regras", "regras-e-testes", "combate", "atributos",
    "pericias", "pericias-comuns", "poderes", "magias", "rituais", "itens", "equipamentos",
    "armas", "monstros", "criaturas", "inimigo", "inimigos", "consideracoes",
    "consideracoes-finais", "nota-dos-autores", "suplemento-para-rpg-daemon",
    "o-que-e-um-jogo-narrativo", "historico-do-anime", "resumo-historico",
    "estrutura-do", "novas", "valor-inicial", "passo-6-pericias-de-combate",
    "fazer-um-teste-de-pericia", "objetivos-motivacao", "objetivos",
}

BAD_TITLE_CHARS_RE = re.compile(r"[\\<>¤�]|[!]{2,}|[~]{1,}|[{}]")
FRAGMENT_TITLE_RE = re.compile(r"^(?:[a-zà-ÿ]|extra\b|alvos?\b|de\b|da\b|do\b|das\b|dos\b|sobrenaturais\b|arremessar\b|determinadas\b|fun[cç][oõ]es\b)", re.IGNORECASE)
COST_AS_TITLE_RE = re.compile(r"^(?:[-–—−]?\s*)?\d+\s*(?:pontos?|pts?\.?|d\d+)\s*:", re.IGNORECASE)


def is_specific_consultable_title(name: str, source_title: str) -> bool:
    clean = normalize_spaces(name)
    if is_generic_or_raw_title(clean, source_title):
        return False
    slug = slugify(clean)
    if not slug or slug in GENERIC_TITLE_SLUGS:
        return False
    if BAD_TITLE_CHARS_RE.search(clean):
        return False
    if COST_AS_TITLE_RE.match(clean):
        return False
    if FRAGMENT_TITLE_RE.match(clean) and not re.search(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}\b", clean):
        return False
    if clean.endswith((",", ";", ":")):
        return False
    if len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]", clean)) < 4:
        return False
    words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]{2,}", clean)
    if len(words) <= 2 and all(len(w) <= 3 for w in words):
        return False
    if len(clean) > 90 and PAGE_RANGE_TITLE_RE.search(clean):
        return False
    return True
OCR_SYMBOL_RE = re.compile(r"[\\/_~^`|<>]{2,}|'{3,}|\"{3,}|\.{5,}|[¤�]")
LETTER_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]")
VISIBLE_RE = re.compile(r"\S")

MECHANIC_RE = re.compile(
    r"\b(?:custo|custos|per[ií]cias?|aprimoramentos?|requisitos?|pr[eé]-requisitos?|"
    r"benef[ií]cios?|especial|sistema|efeitos?|dura[cç][aã]o|alcance|teste|testes|"
    r"atributos?|pontos?|b[oô]nus|penalidade|resist[eê]ncia|dificuldade)\s*:",
    re.IGNORECASE,
)
COMBAT_RE = re.compile(r"\b(?:ataque|defesa|dano|iniciativa|manobras?|esquiva|cr[ií]tico|IP|PVs?|arma|armas|armadura)\b", re.IGNORECASE)
POWER_RE = re.compile(r"\b(?:magia|magias|poder|poderes|ritual|rituais|c[ií]rculo|caminho|mana|focus|psiquismo|milagre|encantamento|invoca[cç][aã]o)\b", re.IGNORECASE)
ITEM_RE = re.compile(r"\b(?:item|itens|equipamento|equipamentos|arma|armas|armadura|escudo|pre[cç]o|custo|peso|dano|alcance|material|materiais|po[cç][aã]o|veneno|produto|compra)\b", re.IGNORECASE)
CREATURE_RE = re.compile(r"\b(?:CON|FR|DEX|AGI|INT|WILL|CAR|PER|PVs?|ataques?|IP|criatura|monstro|inimigo|NPC|dem[oô]nio|anjo|drag[aã]o|morto-vivo|vampiro)\b")
ORG_RE = re.compile(r"\b(?:ordem|irmandade|guilda|cl[aã]|seita|culto|igreja|fac[cç][aã]o|organiza[cç][aã]o|sociedade|cabala|tribo|fam[ií]lia|casa\s+nobre|tr[ií]ade)\b", re.IGNORECASE)
LORE_RE = re.compile(r"\b(?:hist[oó]ria|mundo|reino|cidade|cen[aá]rio|plano|dimens[aã]o|mitologia|deuses?|entidades?|regi[aã]o|continente|cultura|povo|civiliza[cç][aã]o|metrópole|metropole)\b", re.IGNORECASE)
ADVENTURE_RE = re.compile(r"\b(?:aventura|campanha|cena|encontro|gancho|miss[aã]o|cap[ií]tulo\s+de\s+aventura|quick\s*start)\b", re.IGNORECASE)
TABLE_RE = re.compile(r"\b(?:tabela|tabelas|lista|gerador|aleat[oó]rio|valores|modificadores|matriz)\b", re.IGNORECASE)
CHARACTER_OPTION_RE = re.compile(r"\b(?:kit|kits|classe|classes|ra[cç]a|ra[cç]as|linhagem|linhagens|aprimoramento|aprimoramentos|vantagem|desvantagem|talento)\b", re.IGNORECASE)


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def text_for_item(item: dict[str, Any]) -> str:
    values: list[str] = []
    for field in ("name", "summary", "entries", "tags", "sourceTitle"):
        value = item.get(field)
        if isinstance(value, list):
            values.extend(str(v) for v in value if v)
        elif value:
            values.append(str(value))
    return normalize_spaces("\n".join(values))


def alpha_ratio(text: str) -> float:
    visible = len(VISIBLE_RE.findall(text))
    if not visible:
        return 0.0
    return len(LETTER_RE.findall(text)) / visible


def symbol_noise_ratio(text: str) -> float:
    visible = max(1, len(VISIBLE_RE.findall(text)))
    noisy = len(re.findall(r"[\\/_~^`|<>]", text)) + len(re.findall(r"'{3,}|\"{3,}|\.{4,}|[¤�]", text)) * 3
    return noisy / visible


def is_probably_ocr_noise(name: str, text: str) -> bool:
    compact = normalize_spaces(f"{name} {text}")
    if not compact:
        return True
    if OCR_SYMBOL_RE.search(compact) and (symbol_noise_ratio(compact) > 0.035 or alpha_ratio(compact) < 0.62):
        return True
    if len(name) >= 6 and alpha_ratio(name) < 0.55 and OCR_SYMBOL_RE.search(name):
        return True
    if re.search(r"\b[0-9oO]{5,}\b|[oO0]{6,}", name):
        return True
    return False


def title_matches_source_title(name: str, source_title: str) -> bool:
    n = slugify(name or "")
    s = slugify(source_title or "")
    if not n or not s:
        return False
    return n == s or n.startswith(f"{s}-") or s.startswith(f"{n}-")


def is_generic_or_raw_title(name: str, source_title: str) -> bool:
    clean = normalize_spaces(name)
    if not clean:
        return True
    if URL_RE.search(clean):
        return True
    if title_matches_source_title(clean, source_title):
        return True
    if GENERIC_TITLE_RE.search(clean):
        return True
    if BROAD_SECTION_RE.fullmatch(clean):
        return True
    if PAGE_RANGE_TITLE_RE.search(clean) and len(clean.split()) <= 4:
        return True
    if re.fullmatch(r"\d{1,4}(?:\s*[-–]\s*\d{1,4})?", clean):
        return True
    return False


def infer_content_kind(item: dict[str, Any], source_title: str = "") -> tuple[str, list[str]]:
    name = normalize_spaces(str(item.get("name") or ""))
    summary = normalize_spaces(str(item.get("summary") or ""))
    text = normalize_spaces(f"{name} {summary} {' '.join(str(t) for t in item.get('tags', []) or [])}")
    flags: list[str] = []

    if is_probably_ocr_noise(name, text):
        return "ocr_noise", ["ocr_corrupted_title_or_body"]

    front_hits = len(re.findall(r"\b(?:cr[eé]ditos|agradecimentos|diagrama[cç][aã]o|arte\s+interna|capa|autores?|[ií]ndice|sum[aá]rio|download|e-mail|email)\b", text, flags=re.IGNORECASE))
    if front_hits >= 2 and not (MECHANIC_RE.search(text) or ITEM_RE.search(text) or CREATURE_RE.search(text)):
        return "front_matter", ["front_matter_or_index_block"]

    generic_title = is_generic_or_raw_title(name, source_title)
    if generic_title:
        flags.append("generic_chapter_or_page_block")

    if TABLE_RE.search(text) and ("tabela" in slugify(name) or item.get("area") == "tabelas"):
        kind = "table_reference"
    elif ORG_RE.search(text):
        kind = "organization_faction"
    elif POWER_RE.search(text) and (MECHANIC_RE.search(text) or "círculo" in text.lower() or "circulo" in text.lower()):
        kind = "power_spell"
    elif ITEM_RE.search(text) and (re.search(r"\b(?:dano|pre[cç]o|peso|alcance|arma|armadura|escudo|material|produto)\b", text, flags=re.IGNORECASE)):
        kind = "item_equipment"
    elif CREATURE_RE.search(text) and re.search(r"\b(?:CON|FR|DEX|AGI|INT|WILL|CAR|PER|PVs?|IP)\b", text):
        kind = "creature_npc"
    elif CHARACTER_OPTION_RE.search(text) and (MECHANIC_RE.search(text) or re.search(r"\b\d+\s+pontos?\b", text, re.IGNORECASE)):
        kind = "character_option"
    elif COMBAT_RE.search(text) and (MECHANIC_RE.search(text) or re.search(r"\b(?:manobra|ataque|defesa|dano|esquiva)\b", text, re.IGNORECASE)):
        kind = "combat_maneuver"
    elif MECHANIC_RE.search(text):
        kind = "rule_mechanic"
    elif ADVENTURE_RE.search(text) and not generic_title:
        kind = "adventure_scene"
    elif (LORE_RE.search(text) or ORG_RE.search(text)) and not generic_title:
        kind = "lore_world"
    else:
        kind = "raw_chapter_block" if generic_title else "uncertain_fragment"

    if kind in {"raw_chapter_block", "uncertain_fragment"}:
        flags.append("source_part_without_specific_subject")
    if generic_title and kind not in {"table_reference"}:
        kind = "raw_chapter_block"
    return kind, sorted(set(flags))


def classify_source_part(item: dict[str, Any], source_title: str = "") -> dict[str, Any]:
    kind, flags = infer_content_kind(item, source_title)
    specific_title = is_specific_consultable_title(str(item.get("name") or ""), source_title)
    if not specific_title:
        flags = sorted(set([*flags, "source_part_without_specific_subject"]))
    # Regra editorial rígida: sourceParts são blocos brutos de livro.
    # Eles ficam preservados e categorizados para revisão, mas não entram no
    # catálogo normal automaticamente. Para publicar um trecho bruto específico,
    # use data/editorial/overrides.json com action=publish após revisão manual.
    flags = sorted(set([*flags, "raw_source_part_requires_review"]))
    return {
        "contentKind": kind,
        "contentKindLabel": CONTENT_KIND_LABELS.get(kind, kind),
        "editorialFlags": flags,
        "editorialStatus": "raw_review",
        "presentationStatusHint": "quarantine",
    }


def content_kind_for_entity(item: dict[str, Any]) -> dict[str, Any]:
    area = item.get("area")
    category = item.get("category")
    subtype = item.get("subtype")
    if area == "fontes" or category == "source":
        kind = "source_catalog"
    elif area in {"aprimoramentos", "kits", "classes", "racas", "linhagens"} or subtype in {"aprimoramento", "kit", "class", "raca", "linhagem"}:
        kind = "character_option"
    elif area in {"poderes", "magias", "rituais"} or subtype in {"poder", "magia", "ritual"}:
        kind = "power_spell"
    elif area in {"combate"} or category == "combat":
        kind = "combat_maneuver"
    elif area in {"itens_equipamentos"} or category == "item_equipment":
        kind = "item_equipment"
    elif area in {"criaturas_npcs"} or category == "creature_npc":
        kind = "creature_npc"
    elif area in {"cenarios_lore"} or category == "setting_lore":
        kind = "lore_world"
    elif area in {"aventuras"} or category == "adventure":
        kind = "adventure_scene"
    elif area in {"tabelas"} or category == "table_generator":
        kind = "table_reference"
    else:
        kind = "rule_mechanic"
    return {"contentKind": kind, "contentKindLabel": CONTENT_KIND_LABELS.get(kind, kind)}
