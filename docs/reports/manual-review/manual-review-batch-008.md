# Manual Review Batch 008

Scope: sources 211-240 in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, OCR quality, duplicates, version overlap, and suitability for the Daemon repository.

## Summary

- Reviewed: 30 books
- Good enough to continue: 17
- Usable with minor cleanup/noise: 12
- Critical extraction problems: 0
- Exact/known duplicates in this range: 1
- Version / overlap candidates found: 3 sets

## Findings

### 211. `oriente-cronologia`

Status: ok.

Readable Trevas do Oriente chronology/source. Text is coherent and already divided into usable historical/lore sections.

Action: continue.

### 212. `origem-e-descendencia-racial-v-teste`

Status: usable with minor encoding cleanup.

Race/origin rules are coherent and readable, but there are repeated dash/control-character artifacts in the extracted text.

Action: continue; later normalize punctuation and split origins.

### 213. `os-caminhos-secundarios`

Status: ok.

Readable magic/path supplement. Text is coherent and already split into usable sections.

Action: continue.

### 214. `os-invocadores-de-demencia`

Status: usable with DOCX layout caveat.

Short DOCX creature/class style supplement. Text is coherent, but it is one broad part and has long lines from DOCX extraction.

Action: continue; later split powers/background into smaller entries.

### 215. `pactos`

Status: usable with front-matter corruption.

Main pact/dark magic content is readable, but the cover/front matter starts with control-character noise.

Action: continue with caution; later remove corrupt cover text.

### 216. `para-preservar-o-equilibrio-entre-o-ceu-eo-inferno`

Status: ok.

Short DOCX adaptation text is coherent and readable.

Action: continue.

### 217. `pets`

Status: ok.

Readable companion/pet supplement. Text is coherent and useful for creature/companion extraction.

Action: continue.

### 218. `phage`

Status: usable with DOCX layout caveat.

Readable Phage/character adaptation. Text is coherent, but the DOCX extraction leaves long lines and one broad part.

Action: continue; later segment biography, powers and stats.

### 219. `poder`

Status: ok.

Short thematic/rules supplement. Text is coherent and readable.

Action: continue.

### 220. `poderes-cabalisticos`

Status: ok.

Readable cabalistic powers supplement. Text is coherent and usable.

Action: continue.

### 221. `poderes-de-fe-02`

Status: ok.

Readable second-edition faith powers supplement. Text is coherent and already split into usable sections.

Action: continue.

### 222. `poderes-mentais`

Status: ok.

Readable mental powers supplement. Text is coherent with only minor original/extraction roughness near the end.

Action: continue.

### 223. `pontos-heroicos`

Status: ok.

Readable heroic points rules supplement. Text is coherent and usable.

Action: continue.

### 224. `principais-deuses-da-mitologia-n-u00d3rdica`

Status: ok / related source.

Readable Norse mythology/deity supplement. It is related to `mitologia-nordica`, but not a duplicate.

Action: continue; later group with Norse mythology sources.

### 225. `psi`

Status: usable with broad segmentation.

Readable mental powers sourcebook. Text is coherent, but the first part spans most of the book and should be split by power/rule groups.

Action: continue with caution; later segment powers.

### 226. `racas`

Status: ok.

Readable race supplement. Text is coherent and already split into race-level parts.

Action: continue.

### 227. `ray`

Status: ok.

Readable adaptation/source. Text is coherent and segmented into usable sections.

Action: continue.

### 228. `redentor`

Status: ok.

Readable caste/adaptation supplement for Anjos. Text is coherent and usable.

Action: continue.

### 229. `regra-opcional-ataques-a-objetos`

Status: usable with DOCX spacing/layout cleanup.

Short optional combat rule. Text is coherent, but spacing is damaged in some phrases and table-like content is compacted.

Action: continue; later clean spacing/table layout.

### 230. `religioes01`

Status: duplicate.

Full extracted text matches `mitraismo`.

Action: keep excluded from normal categorization.

### 231. `revolucao-francesa`

Status: ok.

Readable historical setting supplement. Text is coherent and usable.

Action: continue.

### 232. `rituais`

Status: ok.

Readable magic/ritual supplement. Text is coherent and usable.

Action: continue.

### 233. `rocknrt`

Status: ok.

Readable rock-and-roll themed kit/source. Text is coherent and already divided into useful sections.

Action: continue.

### 234. `rpg-dragon-ball-oficial-l-by-fractius`

Status: usable with taxonomy boundary caveat.

Readable Dragon Ball / 3D&T source. Text is coherent, but it is system-adjacent and should not be mixed into Daemon core rules without an adaptation boundary.

Action: continue as system-adjacent/adaptation source.

### 235. `samurai-shodown-v-move-list`

Status: usable with taxonomy/format caveat.

Readable move list, but mostly English fighting-game command material rather than a normal Daemon sourcebook. It relates to `samurai-shodown` but is not a duplicate.

Action: keep as reference/appendix-style source; do not treat as normal rules prose.

### 236. `samurai-shodown`

Status: usable with DOCX/wiki cleanup needed.

Readable Samurai Shodown adaptation. Text is coherent, but DOCX extraction has long lines, wiki-style headings and dense technique blocks.

Action: continue with caution; later split techniques and clean markup.

### 237. `samurai-x`

Status: usable with overlap note.

Readable Rurouni Kenshin/Samurai X material. Text is coherent, with visible footer/contact artifacts and thematic overlap with `juppongatana`, though not a duplicate.

Action: continue; compare with `juppongatana` before extracting repeated characters/techniques.

### 238. `samurais`

Status: ok.

Readable samurai supplement. Text is coherent and usable.

Action: continue.

### 239. `santa-cruz-biblioteca-elfica`

Status: usable with cleanup and source-boundary caveat.

Large Santa Cruz sourcebook. Text is coherent and substantial, but headings/index-derived segmentation is broad and contains some OCR/layout artifacts. It is a large standalone horror-colonial RPG/source and should be handled as its own setting boundary.

Action: continue with caution; later split chapters, tables and entities.

### 240. `santa-cruz-inferno-verde-biblioteca-elfica`

Status: usable with overlap/source-boundary caveat.

Readable Santa Cruz supplement. It overlaps thematically with `santa-cruz-biblioteca-elfica`, but is not a duplicate. Text is coherent and useful.

Action: continue; group under Santa Cruz setting and compare repeated rules/lore.

## Batch Actions

- Keep 29/30 in the processing flow for now.
- Exclude exact duplicate:
  - `religioes01`
- New exact duplicate to register:
  - `religioes01` -> `mitraismo`
- Version / overlap sets to compare before final extraction:
  - `principais-deuses-da-mitologia-n-u00d3rdica` <-> `mitologia-nordica`
  - `samurai-x` <-> `juppongatana`
  - `santa-cruz-biblioteca-elfica` <-> `santa-cruz-inferno-verde-biblioteca-elfica`
- Later cleanup candidates:
  - `origem-e-descendencia-racial-v-teste`
  - `os-invocadores-de-demencia`
  - `pactos`
  - `phage`
  - `psi`
  - `regra-opcional-ataques-a-objetos`
  - `rpg-dragon-ball-oficial-l-by-fractius`
  - `samurai-shodown-v-move-list`
  - `samurai-shodown`
  - `samurai-x`
  - `santa-cruz-biblioteca-elfica`
  - `santa-cruz-inferno-verde-biblioteca-elfica`
