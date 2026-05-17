from __future__ import annotations

import re
from dataclasses import dataclass

from common import DATA_DIR, INDEX_DIR, ROOT, slugify, read_json, write_json


TEXT_DIR = DATA_DIR / "text"
ENTITIES_DIR = DATA_DIR / "entities"
REPORTS_DIR = ROOT / "docs"

PAGE_RE = re.compile(r"^--- page (\d+) ---$")


@dataclass
class Line:
    page: int
    text: str


def fix_mojibake(text: str) -> str:
    if "Ã" not in text and "â" not in text:
        return text
    try:
        fixed = text.encode("latin1", errors="ignore").decode("utf-8", errors="ignore")
    except UnicodeError:
        return text
    return fixed if fixed.count("Ã") + fixed.count("â") < text.count("Ã") + text.count("â") else text


def split_lines_by_page(source_id: str) -> list[Line]:
    text = (TEXT_DIR / f"{source_id}.txt").read_text(encoding="utf-8", errors="ignore")
    lines: list[Line] = []
    page = 0
    for raw in text.splitlines():
        marker = PAGE_RE.match(raw.strip())
        if marker:
            page = int(marker.group(1))
            continue
        line = fix_mojibake(raw).strip()
        if line:
            lines.append(Line(page, line))
    return lines


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip(" .;\n\t")


def lines_for_pages(lines: list[Line], start: int, end: int) -> list[Line]:
    return [line for line in lines if start <= line.page <= end]


def find_heading_indices(lines: list[Line], names: list[str]) -> list[tuple[str, int]]:
    normalized_names = {slugify(name): name for name in names}
    matches: list[tuple[str, int]] = []
    for index, line in enumerate(lines):
        key = slugify(line.text)
        if key in normalized_names:
            matches.append((normalized_names[key], index))
    return matches


def field(pattern: str, body: str) -> str | None:
    match = re.search(pattern, body, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    return clean_text(match.group(1))


def cost_payload(text: str) -> dict[str, int | str]:
    payload: dict[str, int | str] = {}
    cost_text = field(r"(?:Custo em pontos de Aprimoramento|Custos?)\s*:\s*(.*?)(?=Atributos Principais|Per[ií]cias|Tempo de aprendizado|$)", text)
    if cost_text:
        payload["costText"] = cost_text
    aprim = re.search(r"(\d+)\s*(?:pontos?|pts?)\s*(?:de\s*)?Aprimoramento", text, flags=re.IGNORECASE)
    pericia = re.search(r"(\d+)\s*(?:pontos?|pts?)\s*(?:de\s*)?Per[ií]cia", text, flags=re.IGNORECASE)
    if aprim:
        payload["aprimoramentoCost"] = int(aprim.group(1))
    if pericia:
        payload["periciaCost"] = int(pericia.group(1))
    return payload


def build_entity(
    source: str,
    title: str,
    name: str,
    chunk: list[Line],
    confidence: float,
    class_context: str = "manual-extractor",
    class_kind: str = "classe",
) -> dict:
    body = "\n".join(line.text for line in chunk[1:]).strip()
    pages = sorted({line.page for line in chunk if line.page})
    entity = {
        "id": f"classe-{source}-{slugify(name)}",
        "name": name,
        "category": "character_class",
        "subtype": "class",
        "source": source,
        "sourceTitle": title,
        "page": pages[0] if pages else None,
        "pages": pages,
        "entries": [body],
        "tags": ["classe", "auto-extraido"],
        "confidence": confidence,
        "extractionMethod": "auto-class-pass-1",
        "classContext": class_context,
        "classKind": class_kind,
    }
    entity.update(cost_payload(body))
    attrs = field(r"Atributos Principais\s*:\s*(.*?)(?=Per[ií]cias Obrigat[oó]rias|Pericias Obrigatorias|$)", body)
    required = field(r"Per[ií]cias Obrigat[oó]rias\s*:\s*(.*?)(?=Per[ií]cias Sugeridas|B[oô]nus de Treino|$)", body)
    suggested = field(r"Per[ií]cias Sugeridas\s*:\s*(.*?)(?=B[oô]nus de Treino|Poder B[aá]sico|$)", body)
    if attrs:
        entity["primaryAttributes"] = attrs
    if required:
        entity["requiredSkillsText"] = required
    if suggested:
        entity["suggestedSkillsText"] = suggested
    return entity


def extract_gerador() -> list[dict]:
    source = "gerador-de-criaturas"
    lines = lines_for_pages(split_lines_by_page(source), 99, 110)
    names = ["Mestre das Feras", "Caçador", "Convocador", "Imitador", "Mestre da Transformação"]
    headings = find_heading_indices(lines, names)
    entities: list[dict] = []
    for pos, (name, start) in enumerate(headings):
        end = headings[pos + 1][1] if pos + 1 < len(headings) else len(lines)
        chunk = lines[start:end]
        if len(chunk) > 5:
            entities.append(build_entity(source, "Gerador de criaturas", name, chunk, 0.82))
    return entities


def extract_abismo_quick_start_roles() -> list[dict]:
    source = "abismo-infinito-quick-start"
    lines = lines_for_pages(split_lines_by_page(source), 24, 27)
    names = [
        "Astrogeólogo",
        "Engenheiro",
        "Cosmólogo",
        "Criptólogo",
        "Navegador",
        "Exobiólogo",
        "Médico",
        "Psicólogo",
        "Segurança",
        "Videomaker",
    ]
    headings = find_heading_indices(lines, names)
    entities: list[dict] = []
    for pos, (name, start) in enumerate(headings):
        end = headings[pos + 1][1] if pos + 1 < len(headings) else len(lines)
        chunk = lines[start:end]
        if len(chunk) > 2:
            entities.append(
                build_entity(
                    source,
                    "Abismo-Infinito-Quick-Start",
                    name,
                    chunk,
                    0.84,
                    class_context="book-part,cargo-section",
                    class_kind="cargo",
                )
            )
    return entities


def extract_demonios() -> list[dict]:
    source = "demonios-a-divina-comedia"
    lines = lines_for_pages(split_lines_by_page(source), 104, 105)
    names = ["EXORCISTA DE ROMA", "EXORCISTA DE ESPANHOL", "EXORCISTA DE CONSTANTINOPLA"]
    headings = find_heading_indices(lines, names)
    # Each exorcist appears once in prose and once in the stat block; keep the stat-block occurrence.
    stat_headings: list[tuple[str, int]] = []
    for name, index in headings:
        lookahead = " ".join(line.text for line in lines[index:index + 8])
        if re.search(r"Tempo de aprendizado|Custos", lookahead, flags=re.IGNORECASE):
            stat_headings.append((name.title().replace(" De ", " de "), index))
    entities: list[dict] = []
    all_heading_indices = [index for _, index in headings]
    for name, start in stat_headings:
        next_indices = [index for index in all_heading_indices if index > start]
        end = next_indices[0] if next_indices else len(lines)
        chunk = lines[start:end]
        if len(chunk) > 5:
            entities.append(build_entity(source, "Demônios - A Divina Comédia", name, chunk, 0.8))
    return entities


def stat_heading_indices(lines: list[Line], names: list[str], marker: str) -> list[tuple[str, int]]:
    headings = find_heading_indices(lines, names)
    selected: list[tuple[str, int]] = []
    for name, index in headings:
        lookahead = " ".join(line.text for line in lines[index:index + 5])
        if re.search(marker, lookahead, flags=re.IGNORECASE):
            selected.append((name, index))
    return selected


def extract_monges() -> list[dict]:
    source = "monges-daemon"
    lines = split_lines_by_page(source)
    if not lines:
        return []
    entity = build_entity(source, "Monges para Daemon", "Monge", lines, 0.8)
    return [entity]


def extract_fadas_3() -> list[dict]:
    source = "fadas-3-edicao"
    lines = lines_for_pages(split_lines_by_page(source), 18, 19)
    headings = find_heading_indices(lines, ["A Lendária Fada da Morte", "A Lendária Artista marcial"])
    starts = {name: index for name, index in headings}
    if "A Lendária Fada da Morte" not in starts:
        return []
    start = starts["A Lendária Fada da Morte"]
    end = starts.get("A Lendária Artista marcial", len(lines))
    chunk = lines[start:end]
    if len(chunk) <= 5:
        return []
    entity = build_entity(
        source,
        "Fadas 3ª Edição",
        "A Lendária Fada da Morte",
        chunk,
        0.78,
        class_context="text-class-term",
        class_kind="classe rara",
    )
    return [entity]


def queue_class_candidates(ready: set[str]) -> list[dict]:
    patterns = re.compile(
        r"\b(classe|classes|profiss[aã]o|profiss[oõ]es|arqu[eé]tipo|arquetipo|arqu[eé]tipos|arquetipos|caminho|caminhos)\b",
        re.IGNORECASE,
    )
    mechanical = re.compile(
        r"\b(Custo|Per[ií]cias?|Aprimoramentos?|Requisitos?|N[ií]vel|Poderes?|Pontos Her[oó]icos|Pontos de Per[ií]cia)\b",
        re.IGNORECASE,
    )
    candidates: list[dict] = []
    for source_id in sorted(ready):
        text_path = TEXT_DIR / f"{source_id}.txt"
        if not text_path.exists():
            continue
        lines = split_lines_by_page(source_id)
        for index, line in enumerate(lines):
            if not patterns.search(line.text):
                continue
            window = lines[max(0, index - 3):index + 12]
            body = "\n".join(item.text for item in window)
            normalized = slugify(body)
            if any(false_positive in normalized for false_positive in ["classe-social", "classe-media", "classe-dominante"]):
                continue
            if not mechanical.search(body):
                continue
            candidates.append(
                {
                    "source": source_id,
                    "page": line.page,
                    "matchedLine": line.text,
                    "context": body,
                    "reason": "possivel classe por profissao/arquetipo/caminho",
                    "status": "needs_manual_classification",
                }
            )
            if sum(1 for item in candidates if item["source"] == source_id) >= 8:
                break
    return candidates


def main() -> None:
    ready = set(read_json(INDEX_DIR / "area-summary.json", {}).get("readySources", []))
    entities: list[dict] = []
    per_source: list[dict] = []

    if "abismo-infinito-quick-start" in ready:
        found = extract_abismo_quick_start_roles()
        entities.extend(found)
        per_source.append({"source": "abismo-infinito-quick-start", "extractedCount": len(found)})
    if "monges-daemon" in ready:
        found = extract_monges()
        entities.extend(found)
        per_source.append({"source": "monges-daemon", "extractedCount": len(found)})
    if "fadas-3-edicao" in ready:
        found = extract_fadas_3()
        entities.extend(found)
        per_source.append({"source": "fadas-3-edicao", "extractedCount": len(found)})

    write_json(ENTITIES_DIR / "class_granular.json", entities)
    candidates = queue_class_candidates(ready)
    write_json(DATA_DIR / "work" / "class-profession-archetype-path-candidates.json", candidates)
    report = {
        "version": 1,
        "subtype": "class",
        "publishedExtractedCount": len(entities),
        "reviewCandidateCount": len(candidates),
        "sources": per_source,
    }
    write_json(INDEX_DIR / "granular-classes-report.json", report)

    lines = [
        "# Granular classes pass 001",
        "",
        f"- Published extracted classes: {len(entities)}",
        f"- Profession/archetype/path candidates for review: {len(candidates)}",
        "",
        "| Source | Extracted |",
        "| --- | ---: |",
    ]
    for item in per_source:
        lines.append(f"| `{item['source']}` | {item['extractedCount']} |")
    lines.append("")
    (REPORTS_DIR / "granular-classes-pass-001.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Published {len(entities)} granular classes from {len(per_source)} sources.")


if __name__ == "__main__":
    main()
