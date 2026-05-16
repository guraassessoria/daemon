# Manual Review Batch 003

Scope: sources 61-90 in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, duplicates, and suitability for the Daemon repository.

## Summary

- Reviewed: 30 books
- Good enough to continue: 20
- Usable with minor cleanup/noise: 7
- Critical extraction failure: 3
- Duplicate candidates found: 1 pair

## Findings

### 61. `cdd`

Status: ok.

Text is coherent and readable. It is a Caverna do Dragão adaptation with editorial, setting sections, characters and sheet material. End section is mostly form/table content but expected.

Action: continue.

### 62. `ceifadores`

Status: ok.

Text is coherent. Contains warning, order description, rituals, NPCs and adventure rumors. No major extraction issue found.

Action: continue.

### 63. `charadas`

Status: ok.

Short riddle supplement. Text is coherent and readable from beginning to end.

Action: continue.

### 64. `ciganos`

Status: ok.

Text is coherent and readable. It contains cultural background, customs and a kit/class section. Minor line-break hyphenation only.

Action: continue.

### 65. `cimeria`

Status: usable with minor cleanup.

DOCX text is coherent and readable, but BBCode-like remnants such as `[align=center]` remain. Segmentation is broad with one part.

Action: continue; later clean markup and refine sections.

### 66. `clube-de-caca-guia-do-jogador`

Status: ok.

Text is coherent and readable. Minor ligature artifacts appear, but the hunter/player-guide content is usable.

Action: continue.

### 67. `clube-de-caca`

Status: critical extraction failure.

Text is largely unreadable across beginning, middle and end. It appears to be a bad OCR/extraction result with many distorted characters and broken words. Some final character sheet labels are partially readable, but the book body is not reliable.

Action: move to special extraction/OCR problem list.

### 68. `cobaias`

Status: critical extraction failure.

Known critical. Text remains corrupted by PDF font encoding/control characters across beginning and middle, with only scattered readable bibliography/media references near the end.

Action: keep in special extraction/OCR problem list.

### 69. `cobaias15`

Status: ok.

Text is coherent and readable. It appears to contain additional powers/aprimoramentos for Cobaias. Segmentation is broad but acceptable.

Action: continue.

### 70. `conan`

Status: ok.

Text is coherent and readable. It contains Hyborian chronology/lore and Conan material. No major extraction issue.

Action: continue.

### 71. `corondor`

Status: usable with segmentation caveat.

DOCX segmentation fixed the blob problem and text is coherent. The source appears to combine chronology, rules, mechanized content and rituals; generated parts are still broad.

Action: continue; later refine internal structure.

### 72. `cura`

Status: ok.

Text is coherent and readable. It mixes healing rules, magical healing and recipe-like items/effects. No extraction corruption found.

Action: continue.

### 73. `cyfell`

Status: ok.

Readable Anime RPG/Cyfell supplement with cyberwarriors, lore, rules and vehicle stats. Text is coherent.

Action: continue.

### 74. `caes-de-guerra`

Status: critical extraction failure.

Text is largely unreadable across beginning, middle and end. It has many OCR-like distortions and broken words, despite a few recognizable labels. Not reliable for categorization beyond filename/title.

Action: move to special extraction/OCR problem list.

### 75. `daemon-anime-rpg`

Status: usable with extraction noise.

Body text is readable and coherent, but cover/front matter has OCR substitutions (`Dae111on`, etc.) and the end contains dense table output. Usable for rules extraction with cleanup.

Action: continue; later clean front matter/tables.

### 76. `daemon-medieval`

Status: ok.

Text is coherent and readable. It has repeated title headers and character sheet content at the end, but the rules body is usable.

Action: continue.

### 77. `daemon-tormenta`

Status: usable with segmentation caveat.

Text is readable and coherent. Generated part names are repetitive because the header appears on many pages. Body content is usable.

Action: continue; later improve heading detection.

### 78. `daemon-sem-nivel`

Status: ok.

Short rules variant for Daemon without levels. Text is coherent and readable.

Action: continue.

### 79. `daemon-revisado-playtest-alfa-3-6`

Status: ok.

Readable playtest document. Text is coherent through introduction, character creation, skills and disadvantages. No major extraction issue.

Action: continue.

### 80. `daemonium`

Status: ok.

Readable supplement. Some title styling (`DD æmonion`) is unusual but body text is coherent.

Action: continue.

### 81. `daiphir-legado-de-sangue`

Status: usable with minor encoding cleanup.

Text is coherent and readable, but contains mojibake-like apostrophe/encoding artifacts (`Introduç‘o`, `fam¤lias`, `pr‡prias`, `s�culos`). Text hash matches `daiphir-legado-de-sangue-biblioteca-elfica`.

Action: continue using one canonical version only; later clean encoding artifacts.

### 82. `daiphir-legado-de-sangue-biblioteca-elfica`

Status: duplicate candidate.

Text appears identical to `daiphir-legado-de-sangue` based on hash and samples.

Action: mark as duplicate candidate of `daiphir-legado-de-sangue`.

### 83. `dbz-rpg`

Status: ok.

Readable Dragon Ball adaptation. Contains editorial, history, attributes, rules, techniques and character sheet. No major extraction issue.

Action: continue.

### 84. `deform`

Status: ok.

Readable magic deformation supplement. Text is coherent and segmented by magical paths.

Action: continue.

### 85. `dem-nio-o-pre-o-do-poder`

Status: usable with encoded chunks.

Body text is readable and coherent, but title/front matter and the end contain large encoded-looking chunks (`235...`, `VSDOKDQGR...`). The usable body seems substantial, but headings/footer need cleanup.

Action: continue with caution; later repair encoded chunks or strip them.

### 86. `demon-cthulhu`

Status: ok.

Readable Cthulhu/Daemon adaptation. Segmentation is broad by page ranges, but the text is coherent.

Action: continue; later refine sections.

### 87. `demonios-a-divina-comedia`

Status: ok.

Readable official/supplement-like book with concepts, infernal society, powers and sheets. End contains form fields, expected for character sheets.

Action: continue.

### 88. `desentsu`

Status: ok.

Readable Anime RPG/oriental warrior supplement. Text is coherent, though writing has original spelling/style issues.

Action: continue.

### 89. `devilmaycry`

Status: ok.

Readable Devil May Cry adaptation. Coherent NPC/item/lore sections.

Action: continue.

### 90. `diferencas`

Status: ok.

Short Maytréia explanatory supplement. Text is coherent and readable.

Action: continue.

## Batch Actions

- Move to special extraction/OCR list:
  - `clube-de-caca`
  - `cobaias`
  - `caes-de-guerra`
- Mark duplicate candidate:
  - `daiphir-legado-de-sangue-biblioteca-elfica` -> `daiphir-legado-de-sangue`
- Later cleanup candidates:
  - `cimeria`
  - `corondor`
  - `daemon-anime-rpg`
  - `daemon-tormenta`
  - `daiphir-legado-de-sangue`
  - `dem-nio-o-pre-o-do-poder`
  - `demon-cthulhu`
