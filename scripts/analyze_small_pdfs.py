#!/usr/bin/env python3
"""Analyze the smallest PDFs in Livros/.

This script is designed to run inside GitHub Actions with Git LFS enabled.
It sorts PDFs by file size, extracts basic PDF metadata and text samples,
then emits Markdown and JSON reports.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "arquivo"


def classify_by_name_and_text(name: str, text: str) -> tuple[str, list[str], list[str]]:
    hay = f"{name}\n{text}".lower()
    categories: list[str] = []
    targets: list[str] = []

    def has(*terms: str) -> bool:
        return any(term in hay for term in terms)

    doc_type = "indeterminado"

    if has("ficha"):
        doc_type = "ficha_modelo"
        categories += ["ficha", "personagem"]
        targets += ["campos_de_ficha", "atributos", "pericias"]
    elif has("atributo", "atributos"):
        doc_type = "regra_basica"
        categories += ["atributos", "sistema"]
        targets += ["atributos", "regras", "tabelas"]
    elif has("aprimoramento", "vantagem", "desvantagem", "poder", "talento", "kit", "classe de prestigio", "classe de prestígio"):
        doc_type = "catalogo_opcoes_personagem"
        categories += ["personagem", "opcoes", "poderes"]
        targets += ["aprimoramentos", "kits", "poderes", "requisitos"]
    elif has("grim", "magia", "ritual", "caminho", "cabala", "vodu", "onmyodo", "mago"):
        doc_type = "catalogo_magia_rituais"
        categories += ["magia", "rituais"]
        targets += ["magias", "rituais", "custos", "efeitos"]
    elif has("arma", "armadura", "escudo", "equip", "veiculo", "veículo", "veneno"):
        doc_type = "catalogo_equipamentos"
        categories += ["equipamentos"]
        targets += ["itens", "armas", "armaduras", "precos", "dano"]
    elif has("monstro", "criatura", "lobisom", "vampir", "youkai", "drag", "fada", "mortos vivos", "morto-vivo", "zoologico", "zoológico"):
        doc_type = "bestiario_ou_suplemento_criaturas"
        categories += ["criaturas", "bestiario"]
        targets += ["criaturas", "habilidades", "estatisticas"]
    elif has("daemon", "sistema-daemon", "módulo básico", "modulo basico", "playtest"):
        doc_type = "livro_basico_ou_regras_daemon"
        categories += ["daemon", "regras"]
        targets += ["regras", "atributos", "pericias", "combate"]
    elif has("anjos", "cidade de prata", "angel", "azrael", "miguel", "gabriel", "lúcifer", "lucifer"):
        doc_type = "suplemento_anjos"
        categories += ["anjos", "cenario"]
        targets += ["locais", "npcs", "lore", "poderes"]
    elif has("demônio", "demonio", "demônios", "demonios", "inferno"):
        doc_type = "suplemento_demonios"
        categories += ["demonios", "inferno"]
        targets += ["lore", "criaturas", "poderes"]
    elif has("combate", "artes marciais", "samurai", "ninjutsu", "guerra"):
        doc_type = "suplemento_combate"
        categories += ["combate"]
        targets += ["manobras", "armas", "regras"]
    elif has("quick start", "quick-start", "guia básico", "guia basico"):
        doc_type = "quickstart_ou_guia_basico"
        categories += ["introducao", "regras"]
        targets += ["regras_basicas", "personagens_prontos"]
    elif has("mitologia", "inquis", "vaticano", "trevas", "ark", "arkanun", "neokosmos", "spiritum"):
        doc_type = "livro_cenario_ou_lore"
        categories += ["cenario", "lore"]
        targets += ["locais", "organizacoes", "npcs", "ganchos"]

    if not categories:
        categories = ["revisar_manual"]
    if not targets:
        targets = ["sumario", "metadados", "classificacao_manual"]

    return doc_type, sorted(set(categories)), sorted(set(targets))


def analyze_pdf(path: Path, max_pages: int) -> dict[str, Any]:
    result: dict[str, Any] = {
        "arquivo": str(path),
        "nome": path.name,
        "tamanho_bytes": path.stat().st_size,
        "erro": None,
    }
    try:
        import fitz  # PyMuPDF
    except Exception as exc:  # pragma: no cover
        result["erro"] = f"PyMuPDF indisponivel: {exc}"
        return result

    try:
        doc = fitz.open(path)
        result["paginas"] = doc.page_count
        meta = doc.metadata or {}
        result["metadata"] = {k: v for k, v in meta.items() if v}

        samples: list[dict[str, Any]] = []
        text_parts: list[str] = []
        pages_to_read = min(max_pages, doc.page_count)
        for page_index in range(pages_to_read):
            page = doc.load_page(page_index)
            text = page.get_text("text") or ""
            text_norm = re.sub(r"\s+", " ", text).strip()
            text_parts.append(text_norm)
            samples.append({
                "pagina": page_index + 1,
                "chars_texto": len(text_norm),
                "amostra": text_norm[:1500],
            })
        combined = "\n".join(text_parts)
        result["texto_chars_amostra"] = len(combined)
        result["texto_extraivel"] = len(combined.strip()) > 80
        result["provavel_precisa_ocr"] = result["paginas"] > 0 and (len(combined.strip()) / max(1, pages_to_read)) < 80
        result["amostras_paginas"] = samples
        doc_type, categories, targets = classify_by_name_and_text(path.name, combined)
        result["tipo_documento"] = doc_type
        result["categorias"] = categories
        result["alvos_extracao"] = targets
        doc.close()
    except Exception as exc:
        result["erro"] = str(exc)

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="Livros")
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--max-pages", type=int, default=3)
    parser.add_argument("--out", default="reports/pdf_content_analysis")
    args = parser.parse_args()

    root = Path(args.root)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(
        [p for p in root.iterdir() if p.is_file() and p.suffix.lower() == ".pdf"],
        key=lambda p: (p.stat().st_size, p.name.lower()),
    )
    selected = pdfs[: args.limit]
    results = [analyze_pdf(p, args.max_pages) for p in selected]

    json_path = out_dir / "menores_pdfs_analise.json"
    json_path.write_text(json.dumps({
        "total_pdfs_encontrados": len(pdfs),
        "limite_analisado": args.limit,
        "pdfs_analisados": len(results),
        "resultados": results,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# Análise de conteúdo - menores PDFs em `Livros/`",
        "",
        f"Total de PDFs encontrados: {len(pdfs)}",
        f"PDFs analisados neste lote: {len(results)}",
        f"Páginas amostradas por PDF: até {args.max_pages}",
        "",
        "| # | Arquivo | Tamanho | Páginas | Texto extraível | Precisa OCR? | Tipo |",
        "|---:|---|---:|---:|---|---|---|",
    ]
    for idx, item in enumerate(results, start=1):
        md_lines.append(
            f"| {idx} | `{item['arquivo']}` | {item.get('tamanho_bytes', 0)} | {item.get('paginas', '')} | "
            f"{item.get('texto_extraivel', '')} | {item.get('provavel_precisa_ocr', '')} | {item.get('tipo_documento', 'erro')} |"
        )

    md_lines += ["", "## Detalhes", ""]
    for item in results:
        md_lines += [
            f"### `{item['arquivo']}`",
            "",
            f"- Tamanho: {item.get('tamanho_bytes')} bytes",
            f"- Páginas: {item.get('paginas')}",
            f"- Texto extraível: {item.get('texto_extraivel')}",
            f"- Provável precisa OCR: {item.get('provavel_precisa_ocr')}",
            f"- Tipo documental: `{item.get('tipo_documento')}`",
            f"- Categorias: {', '.join(item.get('categorias', []))}",
            f"- Alvos de extração: {', '.join(item.get('alvos_extracao', []))}",
            "",
        ]
        if item.get("erro"):
            md_lines += [f"Erro: `{item['erro']}`", ""]
        for sample in item.get("amostras_paginas", [])[:2]:
            md_lines += [
                f"#### Página {sample['pagina']} - amostra",
                "",
                "```txt",
                sample.get("amostra", "")[:2000],
                "```",
                "",
            ]

    md_path = out_dir / "menores_pdfs_analise.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
