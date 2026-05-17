# Manual Review Batch 009

Scope: sources 241-270 in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, OCR quality, duplicates, version overlap, sheet/form sources, and suitability for the Daemon repository.

## Summary

- Reviewed: 30 books
- Good enough to continue: 13
- Usable with minor/significant cleanup: 12
- Critical extraction problems: 1
- Sheet/form special cases: 1
- Exact/known duplicates in this range: 3
- Version / overlap candidates found: 4 sets

## Findings

### 241. `sda-rpg`

Status: usable with broad segmentation.

Readable Senhor dos Aneis RPG adaptation. Text is coherent, but sections are broad 10-page blocks and the final page is a sheet-like section.

Action: continue; later split rules, races and sheet material.

### 242. `se-eu-pudesse-voar`

Status: ok.

Readable short narrative/adventure-style source. Text is coherent despite minor punctuation artifacts.

Action: continue.

### 243. `secundarios`

Status: ok.

Readable Caminhos Secundarios magic supplement. Text is coherent and already split into usable sections.

Action: continue.

### 244. `seitas`

Status: ok.

Readable secret-society/religious group supplement. Text is coherent and usable.

Action: continue.

### 245. `sistema-daemon-2-x`

Status: usable with version-overlap note.

Core Sistema Daemon text is coherent and readable. It strongly overlaps with `sistema-daemon-3-0` and also overlaps with the expanded/modified module, but is not an exact duplicate.

Action: continue; compare with other Sistema Daemon variants before final canonicalization.

### 246. `sistema-daemon-3-0`

Status: usable with version-overlap note.

Core Sistema Daemon text is coherent and readable. It shares substantial content with `sistema-daemon-2-x`, but differs enough to keep as a separate version for now.

Action: continue; compare edition differences before extracting core rules.

### 247. `sistema-daemon-modulo-basico-dragonslayer-01-e-02`

Status: usable with OCR/heading cleanup.

Readable module excerpt from DragonSlayer. Body rules are usable, but cover/title text and some headings have OCR damage such as mixed-case and misread letters.

Action: continue with caution; later clean headings and compare with core Sistema Daemon modules.

### 248. `sistema-daemon-modulo-basico-expandido-e-modificado`

Status: duplicate.

Known duplicate of `modulo-basico-expandido-e-modificado`.

Action: keep excluded from normal categorization.

### 249. `sobrenatural`

Status: usable with broad segmentation.

Readable supernatural adaptation/source. Text is coherent, but it is currently one large part and should be split before structured extraction.

Action: continue; later segment powers, creatures and rules.

### 250. `spawn`

Status: ok.

Readable Spawn adaptation. Text is coherent and already divided into useful sections.

Action: continue.

### 251. `spiritum`

Status: usable with heading cleanup.

Large Spiritum sourcebook. Text is coherent and well segmented, but some opening/title text and headings have OCR damage.

Action: continue with caution; later normalize headings.

### 252. `steampunk`

Status: ok.

Readable steampunk supplement. Text is coherent and usable.

Action: continue.

### 253. `supers-monstros-e-viloes-biblioteca-elfica`

Status: duplicate.

Known duplicate of `anime-rpg-supers-monstros-e-viloes`.

Action: keep excluded from normal categorization.

### 254. `supers`

Status: usable with significant OCR/table cleanup.

Large Supers sourcebook. Some prose and rules are usable, but front matter, tables and several early pages contain heavy OCR/symbol noise.

Action: continue with caution; later inspect against original/OCR before extracting equipment and power tables.

### 255. `supers01`

Status: ok.

Short Supers powers supplement. Text is coherent and readable.

Action: continue.

### 256. `tagmar-daemon`

Status: usable with version-overlap note.

Readable Tagmar-to-Daemon adaptation. Text is coherent and better segmented than the complete version. It overlaps heavily with `tagmar-daemon-versao-completa`.

Action: continue; compare before choosing canonical Tagmar extraction.

### 257. `tagmar-daemon-versao-completa`

Status: usable with OCR/header cleanup and version-overlap note.

Readable in the body, but repeated decorative header artifacts such as `9oooooo` appear throughout. It overlaps very strongly with `tagmar-daemon` while adding/differing in sections.

Action: continue with caution; compare with `tagmar-daemon` and clean repeated headers.

### 258. `talentos`

Status: usable with front-matter corruption.

The talent entries are readable, but cover/title extraction begins with control-character noise.

Action: continue; later clean cover text and split talents.

### 259. `tartarugasninja`

Status: ok.

Readable Tartarugas Ninja adaptation. Text is coherent and usable.

Action: continue.

### 260. `templarios-biblioteca-elfica`

Status: usable with OCR/heading cleanup.

Readable Templarios sourcebook. Body is coherent, but headings and several words have OCR damage such as `Cemplarios`, `Dersonagem` and similar substitutions.

Action: continue with caution; canonical source over `templarios`.

### 261. `templarios`

Status: duplicate.

Known duplicate/variant of `templarios-biblioteca-elfica`.

Action: keep excluded from normal categorization.

### 262. `terras-natais`

Status: usable with DOCX layout caveat.

Readable Magic/Otaria-related source. Text is coherent, but DOCX extraction leaves long lines and one broad part.

Action: continue; later split by location/faction/background.

### 263. `tradicoes-magicas-vodu`

Status: critical extraction problem.

The extracted text is mostly binary/control-symbol noise and does not preserve coherent Portuguese content.

Action: set aside for re-extraction/OCR/manual source handling; do not categorize from this text.

### 264. `trappers`

Status: ok.

Readable short creature/class supplement. Text is coherent and usable.

Action: continue.

### 265. `trev3-fi`

Status: sheet/form special case.

This is a Trevas character/form sheet, not a normal sourcebook. The extracted labels are partly readable but sparse.

Action: keep as sheet/form asset, not normal rules/lore source.

### 266. `trevas-campanha-epica`

Status: ok.

Large Trevas campaign source. Text is coherent and usable, with many lore, entity and power sections.

Action: continue; later split large page-range sections more finely.

### 267. `trevas-3-0`

Status: usable with significant OCR/layout cleanup.

Large Trevas 3.0 sourcebook. Many sections are readable, but front matter and several pages contain heavy OCR/symbol noise. This needs careful cleanup before being treated as a high-authority core source.

Action: continue with caution; later verify against source/OCR and clean noisy pages.

### 268. `trevas-do-oriente-28-palacios`

Status: usable with overlap note.

Readable Trevas do Oriente supplement. Text is coherent and related to `oriente-cronologia`, but it is not a duplicate.

Action: continue; group with Trevas do Oriente sources.

### 269. `trevas-de-marte`

Status: ok.

Readable Trevas de Marte source. Text is coherent and usable, with a sheet-like ending section.

Action: continue; later separate the sheet/form ending.

### 270. `trevas-diego`

Status: usable with version-overlap note.

Readable Trevas revision/core rules document. Text is coherent and likely overlaps conceptually with other Trevas core editions, but is not an exact duplicate.

Action: continue; compare with `trevas-3-0` and other Trevas core sources before canonical extraction.

## Batch Actions

- Keep 26/30 in the processing flow for now.
- Exclude known duplicates:
  - `sistema-daemon-modulo-basico-expandido-e-modificado`
  - `supers-monstros-e-viloes-biblioteca-elfica`
  - `templarios`
- Set aside as critical extraction problem:
  - `tradicoes-magicas-vodu`
- Treat as sheet/form asset:
  - `trev3-fi`
- Version / overlap sets to compare before final extraction:
  - `sistema-daemon-2-x` <-> `sistema-daemon-3-0` <-> `modulo-basico-expandido-e-modificado` <-> `sistema-daemon-modulo-basico-dragonslayer-01-e-02`
  - `tagmar-daemon` <-> `tagmar-daemon-versao-completa`
  - `trevas-3-0` <-> `trevas-diego`
  - `trevas-do-oriente-28-palacios` <-> `oriente-cronologia`
- Later cleanup candidates:
  - `sda-rpg`
  - `sistema-daemon-2-x`
  - `sistema-daemon-3-0`
  - `sistema-daemon-modulo-basico-dragonslayer-01-e-02`
  - `sobrenatural`
  - `spiritum`
  - `supers`
  - `tagmar-daemon`
  - `tagmar-daemon-versao-completa`
  - `talentos`
  - `templarios-biblioteca-elfica`
  - `terras-natais`
  - `trevas-3-0`
  - `trevas-do-oriente-28-palacios`
  - `trevas-diego`
