# Manual Review Batch 001

Scope: first 30 sources in alphabetical order from `data/index/sources.json`.

Review focus: extracted text coherence, obvious corruption, missing content signals, segmentation quality, and suitability for the Daemon repository.

## Summary

- Reviewed: 30 books
- Good enough to continue: 25
- Usable with minor cleanup/noise: 4
- Critical extraction failure: 1

## Findings

### 01. `4killers`

Status: ok.

Text is coherent from beginning to end. It reads as a horror antagonist/adventure supplement with usable NPC/stat blocks for Freddy, Jason, Michael Myers and Leatherface. Segmentation into 5 parts is reasonable.

Action: continue.

### 02. `a-assassina`

Status: ok.

Text is coherent and complete enough. It reads as an investigative adventure with NPC description, locations, clues, murders and ending material. No obvious broken extraction.

Action: continue.

### 03. `abismo-infinito-quick-start`

Status: ok.

Text is coherent. There is minor OCR/encoding noise near character sheet terms and accent remnants, but the rules and setting text remain readable. Segmentation into 11 parts is good.

Action: continue; optional later cleanup for sheet/footer text.

### 04. `abismo`

Status: ok.

Large book, readable across beginning, middle and end. Structure is coherent: intro, origin/lore, Abismo, entities, places, creatures and stats. No missing-text signal.

Action: continue.

### 05. `alastores-a-justica-infernal`

Status: ok.

Text is coherent and readable. Contains fiction warning, origin/lore, infernal justice, powers, rules and stat blocks. End section remains usable.

Action: continue.

### 06. `alianca-daemon-01`

Status: ok.

Text is coherent. Minor layout artifacts exist in title spacing and line joins, but the article content is readable and complete enough. Segmentation into 8 parts is good.

Action: continue.

### 07. `animalidade`

Status: ok.

Readable and coherent throughout. Minor hyphenation from PDF line breaks, but rules/lore remain clear. Segmentation into 9 parts is useful.

Action: continue.

### 08. `anime-rpg-powers`

Status: usable with minor cleanup.

Text is mostly coherent, but there are visible extraction artifacts such as `sen dos`, `male$ cios`, `u" lizadas`, and ligature remnants. The content is still understandable and usable.

Action: continue, but mark for minor text cleanup later.

### 09. `anime-rpg-supers-monstros-e-viloes`

Status: ok.

Text is coherent. Some spacing loss appears in stat blocks, but creature entries remain readable. Segmentation into 13 parts is acceptable.

Action: continue.

### 10. `anime-rpg-supers-powers`

Status: usable with minor cleanup.

Text is coherent but has the same artifacts seen in `anime-rpg-powers`, including ligatures and broken syllables near the end. Only 1 part was generated, so internal segmentation is weak.

Action: continue; later split into powers/rules sections if needed.

### 11. `anjos-a-cidade-de-prata-angelicos-sicarios`

Status: usable with minor cleanup.

The body text is coherent and readable, but generated headings are noisy because the extractor picked partial lines as section titles. Content itself appears usable.

Action: continue; later refine section headings.

### 12. `anjos-involucro-e-barreira`

Status: critical extraction failure.

Text is not coherent. Most of the extraction is corrupted by PDF font encoding/control characters. The sample contains unreadable character sequences across beginning, middle and end.

Action: exclude from normal categorization for now. Treat as special case requiring OCR or a different extraction method.

### 13. `anjos-requiem-de-fe`

Status: ok.

Text is coherent across intro, middle rules/lore and end. Minor line-break hyphenation exists, but it does not block reading. Segmentation into 7 broad chapters is acceptable.

Action: continue.

### 14. `anjos-cacadores-alados`

Status: ok.

Readable and coherent. Some repeated title text and PDF layout artifacts exist, but powers/rules/lore remain understandable.

Action: continue.

### 15. `anjos-jyhad-faces-da-fe`

Status: ok.

Text is coherent and readable. Minor ligature artifacts in words like bibliography/faith-related words, but not enough to block use. Segmentation into 32 parts is useful, although some headings are partial.

Action: continue; later refine headings.

### 16. `anjos-jyhad-guerra-santa-biblioteca-elfica`

Status: usable with OCR noise.

OCR improved enough to be readable, but the beginning has noisy title/header extraction (`IVHAD`, `DAEMGN`, etc.) and some headings are malformed. Body text in middle/end is coherent.

Action: continue, but mark for OCR/header cleanup later.

### 17. `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica`

Status: usable with OCR noise.

Text is readable in the body, but OCR noise remains high in credits, ads and page-layout-heavy areas. Adventure content in the middle is coherent.

Action: continue, but mark for OCR cleanup; ignore ad/credit noise in categorization.

### 18. `anjos-a-cidade-de-prata`

Status: usable with OCR noise.

Main content is readable, but headings and title/credit pages have OCR noise (`Marcela Del Debato`, `INTR0DUCÃO`, etc.). Middle and end samples are coherent enough.

Action: continue, but mark for heading cleanup later.

### 19. `anjossombras01`

Status: ok.

Narrative text is coherent and readable. One broad part only, but acceptable for short fiction/adventure content.

Action: continue.

### 20. `anjossombras02`

Status: ok.

Narrative text is coherent. Segmentation into 3 location/theme blocks is acceptable.

Action: continue.

### 21. `anjossombras03`

Status: ok.

Narrative text is coherent and readable. One part only, but short length makes that acceptable.

Action: continue.

### 22. `anjossombras04`

Status: ok.

Text is coherent and readable. Segmentation into 4 parts is acceptable, though some headings are dialogue fragments.

Action: continue.

### 23. `anjossombras05`

Status: ok.

Narrative text is coherent and readable. One part only, but acceptable for this short chapter.

Action: continue.

### 24. `anoes`

Status: ok.

Lore/rules text is coherent and readable. Segmentation into culture/race/class blocks is useful.

Action: continue.

### 25. `aprimoramentos-1`

Status: ok.

Readable list/rules content. Segmentation is weak because the entire supplement is one broad part, but extraction itself is coherent.

Action: continue; later split by individual aprimoramentos if this becomes a structured rules database.

### 26. `aprimoramentos-2`

Status: ok.

Text is coherent and segmented by individual aprimoramentos. Good candidate for structured extraction.

Action: continue.

### 27. `aprimoramentos-3`

Status: ok.

Mostly coherent. Some generated headings are sentence fragments due to page layout, and the final line appears truncated/odd (`Viciado em Jogos Vide Dependência`), but the content is usable.

Action: continue; later refine headings and check final page if needed.

### 28. `aprimoramentos-4`

Status: ok.

Text is coherent and readable. Segmentation into 5 parts is acceptable.

Action: continue.

### 29. `aprimoramentostormenta`

Status: ok.

Text is coherent. It is a conversion/adaptation supplement with regional and magic aprimoramentos. No major extraction issues found.

Action: continue.

### 30. `arcanis`

Status: ok.

Text is coherent and readable. Some structure is broad, but extraction is usable. It appears to be a Yoshiro/RPG Anime Brasil supplement for Arcanis lineage.

Action: continue.

## Batch Actions

- Keep 29/30 in the normal processing flow.
- Move `anjos-involucro-e-barreira` to the special extraction/OCR problem list.
- Later cleanup candidates from this batch:
  - `anime-rpg-powers`
  - `anime-rpg-supers-powers`
  - `anjos-a-cidade-de-prata-angelicos-sicarios`
  - `anjos-jyhad-guerra-santa-biblioteca-elfica`
  - `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica`
  - `anjos-a-cidade-de-prata`
  - `aprimoramentos-1`
  - `aprimoramentos-3`
