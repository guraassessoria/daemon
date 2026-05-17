# Manual Review Batch 007

Scope: sources 181-210 in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, OCR quality, duplicates, version overlap, and suitability for the Daemon repository.

## Summary

- Reviewed: 30 books
- Good enough to continue: 17
- Usable with minor cleanup/noise: 10
- Critical extraction problems: 0
- Exact/known duplicates in this range: 3
- Version / overlap candidates found: 3 sets

## Findings

### 181. `metropolis`

Status: usable with version-overlap note.

Short Metrópolis article/source. Text is coherent and readable, with a compact structure around the city, angels, Pinhead and character construction. It is related to `metropolis-2`, but not an exact duplicate.

Action: continue; compare against `metropolis-2` before final entity extraction.

### 182. `mitologia-assirio-babilonica`

Status: ok.

Readable mythology supplement. Text is coherent and suitable for lore, entity and power extraction.

Action: continue.

### 183. `mitologia-celta`

Status: ok.

Readable mythology supplement. Text is coherent and usable.

Action: continue.

### 184. `mitologia-egipcia`

Status: ok.

Readable Egyptian mythology supplement. Text is coherent; the title has minor spacing noise, but the body is usable.

Action: continue.

### 185. `mitologia-nordica`

Status: ok / canonical duplicate target.

Readable Norse mythology supplement. Full extracted text matches `nordica`, but this slug is clearer and should be the canonical one.

Action: continue as canonical source; exclude `nordica`.

### 186. `mitraismo`

Status: ok.

Readable Mithraism supplement. Text is coherent and usable for lore, entity and power extraction.

Action: continue.

### 187. `monges-daemon`

Status: ok.

Single-page monk rules supplement. Text is coherent and usable.

Action: continue.

### 188. `monstros-e-viloes`

Status: duplicate.

Known duplicate of `anime-rpg-supers-monstros-e-viloes`.

Action: keep excluded from normal categorization.

### 189. `mortal-kombat`

Status: ok.

Readable Mortal Kombat adaptation. Text is coherent and already split into usable sections.

Action: continue.

### 190. `mortos-vivos-2`

Status: usable with version-overlap note.

Readable undead supplement. Text is coherent, but there is meaningful topic/content overlap with `mortos-vivos` without being an exact duplicate.

Action: continue; compare undead entries before final extraction.

### 191. `mortos-vivos`

Status: ok / overlap source.

Readable full undead sourcebook. Text is coherent and useful for creature, race/lineage, powers and rules extraction.

Action: continue; compare against `mortos-vivos-2` for repeated entries.

### 192. `mutacao`

Status: usable with table cleanup needed.

Large mutation/supers-style rules source. Text is coherent, but many equipment/combat tables and dense rule blocks should be cleaned before structured extraction.

Action: continue with caution; later split tables and mutation/rule entries.

### 193. `modulo-basico-expandido-e-modificado`

Status: usable with heading/encoding cleanup needed.

Core-rule text is readable and coherent, but several headings have encoding artifacts such as `Introdu÷‘o`, `Conceitos B–sicos` and spaced cover text.

Action: continue; later normalize headings and use as canonical over the known duplicate `sistema-daemon-modulo-basico-expandido-e-modificado`.

### 194. `modulo-combate`

Status: ok.

Readable combat module. Text is coherent and already split into focused parts.

Action: continue.

### 195. `naruto-rpg-daemon-2a-edicao`

Status: usable with version-overlap note.

Readable Naruto adaptation. Text is coherent, but it belongs to a group of Naruto versions that should be compared before final extraction.

Action: continue; compare against `naruto` and `naruto-daemon-2a-ed`.

### 196. `naruto-daemon-2a-ed`

Status: usable with version-overlap note.

Large Naruto adaptation with readable rules, equipment and jutsu content. It is not an exact duplicate of the other Naruto files, but overlaps in theme and possibly repeated mechanics.

Action: continue; keep as separate version until full comparison.

### 197. `naruto`

Status: usable with extraction/edition caveat.

Readable Naruto adaptation, but some sections show rough extraction and partial first letters. It is distinct from the two 2nd-edition Naruto sources.

Action: continue with caution; compare before extracting shared jutsu/rules.

### 198. `neokosmos-biblioteca-elfica`

Status: usable with significant OCR/layout cleanup needed.

Large NeoKosmos sourcebook. The main body is usable, but the front matter, headings and several table-heavy sections contain visible OCR/symbol noise such as broken words and decorative text artifacts.

Action: continue with caution; later clean headings, tables and race/class entries.

### 199. `neokosmos-biblioteca-elfica-compressed`

Status: duplicate.

Known duplicate of `neokosmos-biblioteca-elfica`.

Action: keep excluded from normal categorization.

### 200. `neter-khertet-a-cidade-dourada-de-ra-biblioteca-elfica`

Status: ok.

Readable large Egyptian/celestial sourcebook. Text is coherent and already split into many usable parts, though final extraction will still need entity-level refinement.

Action: continue.

### 201. `ninjutsu`

Status: ok.

Readable ninjutsu supplement. Text is coherent and suitable for combat/technique extraction.

Action: continue.

### 202. `nordica`

Status: duplicate.

Full extracted text matches `mitologia-nordica`.

Action: keep excluded from normal categorization.

### 203. `novas-armas-de-fogo`

Status: ok.

Short weapon supplement. Text is coherent and usable for equipment extraction.

Action: continue.

### 204. `novo-aeon-guia-basico`

Status: usable with taxonomy boundary caveat.

Large 3D&T/Novo Aeon sourcebook. Text is coherent and usable, but it is system-adjacent rather than a direct Daemon/Trevas source. It should be kept in a separate/adaptation boundary so its rules do not pollute Daemon core mechanics.

Action: continue as system-adjacent; later refine taxonomy.

### 205. `novos-poderes-para-fadas-e-fadas-da-luz`

Status: ok.

Readable short fairy powers supplement. Text is coherent and usable.

Action: continue.

### 206. `o-corvo`

Status: usable with encoding/heading cleanup needed.

Readable O Corvo adaptation. The body text is coherent, but headings contain encoding artifacts such as `INTRODUÀˇO`, `CONCEITOS BÐSICOS` and similar damaged accents.

Action: continue with caution; later normalize headings.

### 207. `o-segredo-das-artes-negras`

Status: ok.

Short dark arts/magic supplement. Text is coherent and readable.

Action: continue.

### 208. `one-punch-man-rpg`

Status: usable with cleanup needed.

Readable One Punch Man adaptation. Text is coherent and well enough segmented, but repeated underline/footer artifacts and some table-like sections should be cleaned later.

Action: continue with caution; later clean separators and repeated layout artifacts.

### 209. `onmyodo`

Status: ok.

Readable oriental magic/onmyodo supplement. Text is coherent and usable.

Action: continue.

### 210. `ordens-de-ark-a-nun`

Status: ok.

Readable short Arkanun orders supplement. Text is coherent and usable for organization/entity extraction.

Action: continue.

## Batch Actions

- Keep 27/30 in the processing flow for now.
- Exclude known/exact duplicates:
  - `monstros-e-viloes`
  - `neokosmos-biblioteca-elfica-compressed`
  - `nordica`
- New exact duplicate to register:
  - `nordica` -> `mitologia-nordica`
- Version / overlap sets to compare before final extraction:
  - `metropolis` <-> `metropolis-2`
  - `mortos-vivos` <-> `mortos-vivos-2`
  - `naruto` <-> `naruto-rpg-daemon-2a-edicao` <-> `naruto-daemon-2a-ed`
- Later cleanup candidates:
  - `metropolis`
  - `mortos-vivos-2`
  - `mutacao`
  - `modulo-basico-expandido-e-modificado`
  - `naruto-rpg-daemon-2a-edicao`
  - `naruto-daemon-2a-ed`
  - `naruto`
  - `neokosmos-biblioteca-elfica`
  - `novo-aeon-guia-basico`
  - `o-corvo`
  - `one-punch-man-rpg`
