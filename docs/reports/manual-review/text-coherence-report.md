# Text Coherence Report

Automated audit of extracted text coherence. Duplicates are tracked separately and not counted as failures.

## Summary

- ok: 273
- review: 0
- critical: 4
- duplicate: 0

## Critical

### anjos-involucro-e-barreira
- title: Anjos - Involucro e Barreira
- flags: encoding_noise, symbol_noise
- chars/pages: 31827 / 8
- weird ratio: 0.711094 | empty pages: 0
- sample: `' 323@ ;&(`

### cobaias
- title: cobaias
- flags: encoding_noise, symbol_noise
- chars/pages: 248190 / 56
- weird ratio: 0.758298 | empty pages: 0
- sample: `9   (1<5 `

### ficha-de-personagem-daemon
- title: Ficha de Personagem-Daemon
- flags: many_empty_or_tiny_pages, layout_or_linebreak_problem
- chars/pages: 14 / 1
- weird ratio: 0.0 | empty pages: 1

### tradicoes-magicas-vodu
- title: Tradições Mágicas - Vodu
- flags: encoding_noise, symbol_noise
- chars/pages: 20939 / 9
- weird ratio: 0.725106 | empty pages: 2
- sample: `ABC34D`

## Review
