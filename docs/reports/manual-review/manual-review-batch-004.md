# Manual Review Batch 004

Scope: sources 91-120 in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, form/sheet-only sources, OCR quality, duplicates, and suitability for the Daemon repository.

## Summary

- Reviewed: 30 books
- Good enough to continue: 22
- Usable with minor cleanup/noise: 7
- Critical / special non-book extraction case: 1
- Duplicate candidates found: 0

## Findings

### 91. `domini-urbs-biblioteca-elfica`

Status: ok.

Text is coherent and readable across beginning, middle and end. It is a substantial sourcebook with kits, organizations and angelic/celestial mechanics. Segmentation is broad by chapters but usable.

Action: continue.

### 92. `dragao`

Status: ok.

Short supplement about dragon blood/prole. Text is coherent and readable. One broad part is acceptable.

Action: continue.

### 93. `dragoes-reis-caidos-sistema-daemon`

Status: ok.

Readable and coherent dragon sourcebook. Headings are somewhat repetitive because of page headers, but body text is good.

Action: continue; later refine headings.

### 94. `dragoes2`

Status: ok.

Readable dragon supplement with lore, powers and references. Text is coherent from beginning to end.

Action: continue.

### 95. `dragao-brasil-especial-06-trevas`

Status: usable with extraction noise.

The body has readable rules and ritual content, but front matter/index and closing ad/order pages are noisy. Some words are OCR-damaged in tables and headers.

Action: continue with caution; later clean front/back matter and headings.

### 96. `elf`

Status: ok.

Readable race/lore supplement about elves. Text is coherent and usable.

Action: continue.

### 97. `enciclopedia-a10`

Status: ok.

Readable encyclopedia-style entries. Text is coherent; one broad part is acceptable for now.

Action: continue.

### 98. `energia-mistica`

Status: ok.

Readable magic supplement. Some title/front-matter repetition and spelling issues exist, but content is coherent.

Action: continue.

### 99. `equip`

Status: ok.

Short equipment/pricing table. Text is coherent, though dense because it is table-like. Usable for item/equipment extraction.

Action: continue.

### 100. `era-dos-herois`

Status: ok.

Readable fantasy-medieval supplement. Text is coherent and complete enough.

Action: continue.

### 101. `escudos02`

Status: ok.

Short shield rules supplement. Text is coherent and readable.

Action: continue.

### 102. `etruscos`

Status: ok.

Readable and coherent sourcebook about Etruscans, secret societies and rules. Some generated headings are partial sentences, but body text is good.

Action: continue; later refine headings.

### 103. `evolucao-alternativa`

Status: ok.

Readable rules supplement for alternate advancement/training. Text is coherent.

Action: continue.

### 104. `existe-uma-cidade-nos-distritos-cujo-unico-objetivo-e-a-satisfac-u00e3o`

Status: usable with segmentation caveat.

DOCX text is coherent, but page count is absent and it is one broad part. The source reads like lore about Akash/pleasure/corruption rather than a fully structured supplement.

Action: continue; later segment DOCX and improve title slug/display title.

### 105. `fadadaluz`

Status: ok.

Readable homebrew class/creature supplement. Text is coherent, though original spelling/style is rough.

Action: continue.

### 106. `fadas-2`

Status: ok.

Readable full netbook about fadas. Text is coherent and usable, with broad but acceptable segmentation.

Action: continue.

### 107. `fadas-3-edicao`

Status: ok.

Readable follow-up/third-edition fairy supplement. Text is coherent, with some dense tables near the end.

Action: continue.

### 108. `fadas`

Status: ok.

Short fairy supplement. Text is coherent and readable.

Action: continue.

### 109. `ficha-de-personagem-daemon`

Status: critical / special non-book extraction case.

This appears to be a character sheet/form. The extraction produced essentially no useful text. It should not be treated as a normal book source for categorization.

Action: exclude from normal book categorization; keep as sheet/form asset or OCR/form-special case if needed.

### 110. `ficha-mago-trevas`

Status: usable sheet/form.

This is also a character sheet, but text fields and labels are extracted. It is coherent as a form, not as a sourcebook.

Action: keep as sheet/form category, not a rules/lore book.

### 111. `frankenstein`

Status: ok.

Readable monster/golem supplement. Text is coherent and usable.

Action: continue.

### 112. `fusd-r6`

Status: usable sheet/form.

Universal Daemon sheet. Text is coherent as a form with fields, attributes and grimório sections. Not a normal sourcebook.

Action: keep as sheet/form category.

### 113. `gaki`

Status: ok.

Readable supplement about Gaki. Text is coherent and includes intro, rules, kits and sheet material.

Action: continue.

### 114. `gdac-light`

Status: ok.

Readable Guia de Aliados Conjurados/light supplement. Text is coherent and usable.

Action: continue.

### 115. `gerador-de-criaturas`

Status: ok.

Large creature generation rules supplement. Text is coherent and readable. Segmentation is acceptable.

Action: continue.

### 116. `geradoritem02`

Status: ok.

Readable magic item generator. Text is coherent, including examples and effects.

Action: continue.

### 117. `gigantes-mitologicos`

Status: ok.

Readable sourcebook about mythological giants. Text is coherent, with usable race/power/rules sections.

Action: continue.

### 118. `gmonark`

Status: ok.

Readable Guia de Monstros de Arkanum. One broad part, but content is coherent and usable.

Action: continue; later split creature entries if needed.

### 119. `grimark201`

Status: ok.

Readable Arkanun grimório/magic supplement. Text is coherent.

Action: continue.

### 120. `grimorio`

Status: usable with OCR noise.

OCR output is largely readable in ritual entries, but front matter/title pages contain errors (`Daemon Editors`, `deemonBdaemon`, noisy credits). Body ritual text is coherent enough for extraction.

Action: continue with caution; later clean front matter and possibly verify ritual entries during structured extraction.

## Batch Actions

- Keep 29/30 in the processing flow.
- Treat as special sheet/form asset rather than normal book:
  - `ficha-de-personagem-daemon`
  - `ficha-mago-trevas`
  - `fusd-r6`
- Later cleanup candidates:
  - `dragoes-reis-caidos-sistema-daemon`
  - `dragao-brasil-especial-06-trevas`
  - `etruscos`
  - `existe-uma-cidade-nos-distritos-cujo-unico-objetivo-e-a-satisfac-u00e3o`
  - `gmonark`
  - `grimorio`
