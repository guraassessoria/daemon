# Manual Review Batch 005

Scope: sources 121-150 in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, OCR quality, duplicates, and suitability for the Daemon repository.

## Summary

- Reviewed: 30 books
- Good enough to continue: 18
- Usable with minor cleanup/noise: 7
- Critical extraction problems: 0
- Duplicates / duplicate candidates found in this range: 5

## Findings

### 121. `grimorio101`

Status: ok.

Readable Grimorio de Arton 1.01. Text is coherent from beginning to end, with broad but usable page-range segmentation.

Action: continue; later split rituals/spells into smaller entries.

### 122. `grimorio-compressed`

Status: duplicate.

Known duplicate of `grimorio`. No need to categorize separately.

Action: keep excluded from normal categorization.

### 123. `guerra-de-monstros`

Status: ok.

Short werewolf/vampire supplement with readable setting, adventure and rules material. Text is coherent.

Action: continue.

### 124. `guerreiros-orientais`

Status: ok.

Readable oriental warrior supplement. The opening has intentionally humorous/odd front matter, but the body text about Japan, seppuku and character material is coherent.

Action: continue.

### 125. `guia-de-armas-de-fogo-3a-edicao`

Status: usable with extraction/table noise.

The body rules and equipment content are readable. Cover/front matter has OCR substitutions such as `Daernon`/`Debblo`, and the ending tables are partially garbled.

Action: continue with caution; later clean front matter and weapon tables.

### 126. `guia-de-armas-medievais-3a-edicao`

Status: usable with OCR noise.

The weapon rules and descriptions are readable, but cover/front matter and closing ad/back-cover sections contain OCR damage.

Action: continue with caution; later clean front/back matter and tables.

### 127. `guia-de-itens-magicos`

Status: usable with accent/OCR noise.

Large magic item guide with coherent body text and many usable item entries. Several accents and symbols are damaged, with patterns like `Cria~ao`, `variat;:ao` and `pOl'`.

Action: continue with caution; later normalize accents and split item entries carefully.

### 128. `guia-de-itens-magicos-compressed`

Status: duplicate.

Known duplicate of `guia-de-itens-magicos`.

Action: keep excluded from normal categorization.

### 129. `guia-de-monstros-de-arkanum`

Status: duplicate candidate.

Full extracted text matches `gmonark`, reviewed in batch 004. This appears to be the same Guia de Monstros de Arkanum under a clearer slug.

Action: keep one canonical source only; prefer this clearer slug as canonical.

### 130. `guia-de-monstros-de-arton`

Status: usable with minor OCR noise.

Monster guide text is coherent and readable. Front matter has minor OCR/address artifacts, but creature content is usable.

Action: continue; later split creature entries and clean front matter.

### 131. `guia-do-aventureiro-de-arton`

Status: ok.

Readable adventurer/kits guide for Arton. Text is coherent and suitable for categorization.

Action: continue.

### 132. `guia-de-classes-de-prestigio-biblioteca-elfica`

Status: usable with extraction noise.

The body text is readable, but title/front-matter extraction has damaged words such as `Guiaae` and `Cfntroaucao`-style artifacts.

Action: continue with caution; later clean heading/front-matter text and split prestige classes.

### 133. `guia-dos-dragoes-1-biblioteca-elfica`

Status: ok.

Readable dragon guide. Text is coherent and suitable for lore, creature and rule extraction.

Action: continue.

### 134. `guia-dragoes-vol-ii`

Status: ok.

Readable second dragon guide volume. Text is coherent and usable.

Action: continue.

### 135. `guia-de-racas-de-arton-tormentarpg`

Status: ok.

Readable race guide for Arton/Tormenta. Text is coherent and categorizes naturally into race/lineage content.

Action: continue.

### 136. `guia-guerreiro`

Status: ok.

Readable interpretive/character guide for warriors. Text is coherent.

Action: continue.

### 137. `guia-pericias`

Status: ok.

Readable skill guide. Text is coherent and directly useful for attribute/skill categorization.

Action: continue.

### 138. `guiademagias`

Status: ok.

Readable magic guide/list. Text is coherent and usable for spell/power extraction.

Action: continue.

### 139. `guiadragoes`

Status: duplicate.

Known duplicate of `guia-dos-dragoes-1-biblioteca-elfica`.

Action: keep excluded from normal categorization.

### 140. `harrypotter`

Status: ok.

Readable adaptation material. Some original spelling/style is rough, but the extracted text itself is coherent.

Action: continue.

### 141. `heroismo`

Status: ok.

Readable heroic rules/supplement text. Coherence is good.

Action: continue.

### 142. `hi-brazil-biblioteca-elfica`

Status: usable with OCR/extraction noise.

The body text is readable, but title/front matter and some words are damaged, with artifacts such as `C(lm ~ndo Cj)iferente`, `Hi-CfiraEiC` and similar substitutions.

Action: continue with caution; later clean headings/front matter and verify noisy terms.

### 143. `hydora`

Status: ok.

Readable short supplement. Text is coherent.

Action: continue.

### 144. `imortal-a-centelha`

Status: ok.

Readable Imortal sourcebook. Text is coherent and has useful sections for immortal types, rules and setting material.

Action: continue.

### 145. `imortal-a-centelha-2`

Status: ok / alternate version.

Readable and closely related to `imortal-a-centelha`, but extracted summaries are not identical. It appears to be an alternate layout/version rather than a confirmed duplicate.

Action: keep for now; compare full text/source files before choosing a canonical version.

### 146. `imortal`

Status: ok.

Readable Highlander/immortal-style supplement. Front matter has minor layout glyph noise, but the body text is coherent.

Action: continue.

### 147. `inquisicao-biblioteca-elfica`

Status: usable with extraction noise.

The body text is readable, but front matter, table/form sections and some headings are noisy.

Action: continue with caution; later clean front/table sections.

### 148. `inquisicao-celestial`

Status: ok.

Readable celestial inquisition supplement. Text is coherent and usable.

Action: continue.

### 149. `inquisicao`

Status: duplicate.

Known duplicate of `inquisicao-biblioteca-elfica`.

Action: keep excluded from normal categorization.

### 150. `ismails-anjos-islamicos`

Status: ok.

Readable angelic/islamic supplement. Text is coherent and usable for lore and celestial entity extraction.

Action: continue.

## Batch Actions

- Keep 25/30 in the processing flow for now.
- Exclude known duplicates from normal categorization:
  - `grimorio-compressed`
  - `guia-de-itens-magicos-compressed`
  - `guiadragoes`
  - `inquisicao`
- Resolve duplicate candidate:
  - `gmonark` -> `guia-de-monstros-de-arkanum`
- Compare before canonicalizing:
  - `imortal-a-centelha`
  - `imortal-a-centelha-2`
- Later cleanup candidates:
  - `guia-de-armas-de-fogo-3a-edicao`
  - `guia-de-armas-medievais-3a-edicao`
  - `guia-de-itens-magicos`
  - `guia-de-monstros-de-arton`
  - `guia-de-classes-de-prestigio-biblioteca-elfica`
  - `hi-brazil-biblioteca-elfica`
  - `inquisicao-biblioteca-elfica`
