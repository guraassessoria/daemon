# Manual Review Batch 010

Scope: sources 271-289 in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, OCR quality, duplicates, version overlap, and suitability for the Daemon repository.

## Summary

- Reviewed: 19 books
- Good enough to continue: 10
- Usable with minor/significant cleanup: 9
- Critical extraction problems: 0
- Exact/known duplicates in this range: 0
- Version / overlap candidates found: 3 sets

## Findings

### 271. `um-sussurro-nas-trevas`

Status: usable with cleanup needed.

Large Lovecraftian/Trevas source. Text is coherent and well segmented overall, but it contains repeated separator lines and some OCR/layout noise.

Action: continue; later clean separators and split rules/entities more finely.

### 272. `uma-sucubo-em-extase`

Status: ok.

Readable short adventure/narrative supplement. Text is coherent with minor punctuation/footer artifacts.

Action: continue.

### 273. `umbral-e-seus-vales`

Status: ok.

Readable Umbral source. Text is coherent and already split into usable sections.

Action: continue.

### 274. `universo-daemon-01`

Status: ok.

Readable magazine/collection-style source. Text is coherent, though some short separator/table fragments exist.

Action: continue.

### 275. `utupia-d10`

Status: ok.

Readable Utopia d10 source. Text is coherent and usable.

Action: continue.

### 276. `vampiros-mitologicos`

Status: usable with significant OCR cleanup.

Large vampire sourcebook. The structure and many sections are usable, but front matter and several pages show heavy OCR damage and symbol noise.

Action: continue with caution; later verify against source/OCR before treating as authoritative.

### 277. `vantagens-regionais-ii`

Status: ok.

Readable regional advantages supplement. Text is coherent and usable.

Action: continue.

### 278. `vantagens`

Status: usable with DOCX segmentation cleanup.

Large list of advantages. Text is coherent, but it is one broad DOCX part with long lines and many entries joined together.

Action: continue; later split each advantage into its own entry.

### 279. `varna-chamado-da-guerra`

Status: usable with OCR/layout cleanup.

Readable Varna source in the body, but several headings and table-like sections have OCR artifacts and broken text.

Action: continue with caution; later clean headings and tables.

### 280. `vaticano`

Status: ok.

Readable Vatican/organization supplement. Text is coherent and usable.

Action: continue.

### 281. `veiculos`

Status: usable with broad segmentation.

Readable vehicle/equipment guide. Text is coherent, but it is split into broad 10-page blocks and includes table-heavy vehicle content.

Action: continue; later split vehicle rules/items.

### 282. `venenos`

Status: ok.

Readable short medieval poisons guide. Text is coherent and usable.

Action: continue.

### 283. `vikings-biblioteca-elfica`

Status: usable with OCR/front-matter cleanup.

Large Vikings sourcebook. Body text is coherent and substantial, but cover/front matter and some decorative headings contain OCR noise.

Action: continue with caution; later clean headings and split entities, rules and lore.

### 284. `vikings`

Status: ok / related source.

Readable short Vikings supplement. It is related thematically to `vikings-biblioteca-elfica`, but not a duplicate.

Action: continue; group with Vikings/Norse sources.

### 285. `watchmen`

Status: ok.

Readable Watchmen adaptation. Text is coherent and already segmented into usable sections.

Action: continue.

### 286. `youkai-kyuukai`

Status: ok / related source.

Readable Trevas do Oriente youkai/kyuukai supplement. Text is coherent and useful for creature, organization and setting extraction.

Action: continue; group with other Trevas do Oriente sources.

### 287. `youkais`

Status: ok / related source.

Readable short Youkais supplement for Anime RPG/Sistema Daemon. It is related to `youkai-kyuukai`, but not a duplicate.

Action: continue; compare taxonomy with Trevas do Oriente youkai entries.

### 288. `yuyu-hakusho-rpg-para-daemon`

Status: ok.

Readable Yu Yu Hakusho adaptation. Text is coherent and segmented into usable rules, races/classes and powers.

Action: continue.

### 289. `zoologico`

Status: ok.

Single-page animal/stat block source. Text is coherent and usable for creature extraction.

Action: continue.

## Batch Actions

- Keep all 19 in the processing flow for now.
- No new critical extraction cases.
- No new exact duplicates.
- Version / overlap sets to compare before final extraction:
  - `vikings` <-> `vikings-biblioteca-elfica`
  - `youkais` <-> `youkai-kyuukai`
  - `vantagens` <-> `vantagens-regionais-ii`
- Later cleanup candidates:
  - `um-sussurro-nas-trevas`
  - `vampiros-mitologicos`
  - `vantagens`
  - `varna-chamado-da-guerra`
  - `veiculos`
  - `vikings-biblioteca-elfica`
