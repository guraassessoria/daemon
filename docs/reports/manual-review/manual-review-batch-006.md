# Manual Review Batch 006

Scope: sources 151-180 in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, OCR quality, duplicates, version overlap, and suitability for the Daemon repository.

## Summary

- Reviewed: 30 books
- Good enough to continue: 18
- Usable with minor cleanup/noise: 12
- Critical extraction problems: 0
- Exact duplicates found in this range: 0
- Version / overlap candidates found: 1 pair

## Findings

### 151. `jedi`

Status: usable with broad segmentation.

Text is coherent and readable, covering Star Wars/Jedi adaptation material. Extraction begins with page-number/front-matter noise and the book is currently split into only three large parts.

Action: continue; later split powers, equipment and character options into smaller entries.

### 152. `jiraya`

Status: ok.

Readable short ninja/anime adaptation. Text is coherent after the previous encoding repair.

Action: continue.

### 153. `judaismo`

Status: ok.

Readable lore/religion supplement. Text is coherent and usable for setting and historical/religious categorization.

Action: continue.

### 154. `juppongatana`

Status: usable with minor footer/control-character noise.

The body is readable and coherent, but the extraction includes page-number starts and old footer/contact artifacts with control-style dash characters.

Action: continue; later clean footer/contact lines.

### 155. `jutsu-e-um-termo-japones-para-tecnica`

Status: usable with DOCX/layout cleanup needed.

Text is coherent, but it is one broad DOCX part with long lines and wiki-like fragments such as edit markers. It is usable but should be segmented before structured extraction.

Action: continue with caution; later split by jutsu/type and remove wiki markup.

### 156. `kidous-arte-das-trevas`

Status: ok.

Readable magic/combat supplement. Text is coherent and already divided into usable sections.

Action: continue.

### 157. `kits-arton`

Status: usable with cleanup needed.

The kit content is coherent and useful, but extraction includes repeated page/header material and some damaged characters. Segmentation is broad, especially the main `KITS` section.

Action: continue; later split each kit and clean headers.

### 158. `kits-militares`

Status: ok.

Single-page kit supplement. Text is coherent and readable.

Action: continue.

### 159. `kits-orientais`

Status: usable with DOCX/wiki cleanup needed.

Large oriental/ninja technique compilation. The content is readable, but there are many long DOCX lines, wiki-style markers, repeated labels and dense technique blocks.

Action: continue with caution; later split techniques and clean wiki markup.

### 160. `kits`

Status: ok.

Readable action/adventure kit supplement. Text is coherent and already split into several kit-oriented parts.

Action: continue.

### 161. `kitsat`

Status: ok.

Readable Arkanun/Trevas kit supplement. Text is coherent and well enough segmented for the current stage.

Action: continue.

### 162. `kitsdaemon`

Status: ok.

Readable short kit supplement. Text is coherent.

Action: continue.

### 163. `livrodomal`

Status: usable with decorative OCR/header noise.

The body text is coherent, but the cover and chapter headings have repeated decorative fragments such as split words in `O LIVRO DO MAL`.

Action: continue; later clean decorative headings.

### 164. `lobisomem-a-maldicao-v2-biblioteca-elfica`

Status: ok.

Readable full werewolf sourcebook. Text is coherent and usable for race/lineage, creature and rules extraction.

Action: continue.

### 165. `lobisomem02`

Status: ok.

Short werewolf rules article/supplement. Text is coherent and readable.

Action: continue.

### 166. `lobisomemv3`

Status: ok.

Readable werewolf powers/rules supplement. Text is coherent and distinct from `lobisomem-a-maldicao-v2-biblioteca-elfica`.

Action: continue.

### 167. `lobisomens`

Status: ok.

Readable short werewolf supplement. Minor dash artifacts appear in stat modifiers, but not enough to block categorization.

Action: continue.

### 168. `loucura`

Status: ok.

Short insanity/mental condition rule supplement. Text is coherent despite a noisy first line.

Action: continue.

### 169. `luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br`

Status: usable with source-boundary caveat.

Large, coherent full RPG rulebook. Extraction is readable and reasonably segmented, but this is a separate RPG system rather than a direct Daemon/Trevas supplement. It should be categorized carefully so its rules do not pollute Daemon core assumptions.

Action: continue as separate/system-adjacent source; later review taxonomy boundary.

### 170. `magia-negra`

Status: ok.

Readable black magic supplement. Text is coherent and suitable for ritual/spell and lore extraction.

Action: continue.

### 171. `magic-para-daemon`

Status: ok.

Readable short Magic adaptation. Text is coherent, with some rough original style but usable extraction.

Action: continue.

### 172. `mago-sistema-daemon`

Status: ok.

Readable Mage-to-Daemon style adaptation. Text is coherent and usable, with only minor noisy fragments.

Action: continue.

### 173. `manobras-de-combate`

Status: ok.

Readable combat maneuver supplement. Text is coherent and suitable for combat rules extraction.

Action: continue.

### 174. `manual-de-converscao`

Status: ok.

Readable conversion manual. Text is coherent, including conversion requirements and tables. Title slug has a typo, but the extraction itself is usable.

Action: continue; later normalize display title.

### 175. `marvel-rpg-7o-edicao`

Status: usable with table/OCR cleanup and version-overlap note.

Large Marvel RPG sourcebook. Main prose and rules are coherent, but equipment/tables include symbol-heavy extraction noise. It overlaps heavily with `marvel`, while also containing additional or differently extracted material.

Action: continue; likely prefer this as canonical Marvel version after comparing editions.

### 176. `marvel`

Status: usable with table/OCR cleanup and version-overlap note.

Readable Marvel RPG sourcebook with strong overlap against `marvel-rpg-7o-edicao`. It is not an exact duplicate, but much of the content appears shared. Tables, especially equipment/arms sections, contain symbol-heavy noise.

Action: keep for now as alternate version; compare before structured extraction to avoid double-counting.

### 177. `masmorra-goblin`

Status: usable with DOCX layout caveat.

Short dungeon/adventure material. Text is coherent, but page count is absent and one broad DOCX part should be split before indexing as encounters/rooms.

Action: continue; later segment adventure locations.

### 178. `masmorras`

Status: usable with DOCX layout caveat.

Readable dungeon/adventure material. Text is coherent, but it has absent page count, a few long lines and original spelling issues.

Action: continue; later segment rooms/encounters.

### 179. `mecha`

Status: ok.

Readable mecha rules supplement. Text is coherent and usable for equipment/combat/rules extraction.

Action: continue.

### 180. `metropolis-2`

Status: usable with cleanup needed.

Large Metrópolis sourcebook. Text is coherent and readable, with many usable lore, entity and power sections. Some headings repeat the book title and should be refined before final indexing.

Action: continue; later clean repeated headings and split entities/powers.

## Batch Actions

- Keep all 30 in the processing flow for now.
- No new critical extraction cases.
- Version / overlap pair to compare before final extraction:
  - `marvel-rpg-7o-edicao`
  - `marvel`
- Later cleanup candidates:
  - `jedi`
  - `juppongatana`
  - `jutsu-e-um-termo-japones-para-tecnica`
  - `kits-arton`
  - `kits-orientais`
  - `livrodomal`
  - `luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br`
  - `marvel-rpg-7o-edicao`
  - `marvel`
  - `masmorra-goblin`
  - `masmorras`
  - `metropolis-2`
