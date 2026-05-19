# Auditoria semântica inicial dos destaques

Este relatório identifica trechos publicados que parecem cortados, colados, duplicados, incompletos ou contaminados por artefatos de extração.
Ele não substitui conferência com o PDF/texto oficial; serve para priorizar revisão profissional.

## Resumo

- Registros sinalizados: 2301

### Flags

- `aprimoramento_without_cost_marker`: 26
- `critical_ocr_gibberish`: 158
- `does_not_end_like_complete_sentence`: 1019
- `encoding_or_ocr_artifact`: 194
- `ends_with_connector_possible_cut`: 318
- `front_matter_or_index_block`: 14
- `hyphenated_word_split`: 893
- `invalid_title_or_ocr_header`: 29
- `lowercase_sentence_after_section_possible_leak`: 313
- `many_cost_markers_possible_merged_aprimoramentos`: 9
- `page_number_inside_text`: 160
- `repeated_fragment_possible_duplication`: 29
- `starts_mid_sentence_possible_left_cut`: 35
- `symbol_noise_ocr`: 111
- `too_long_possible_merged_blocks`: 21
- `too_short_possible_cut`: 85
- `unbalanced_brackets`: 76
- `unbalanced_parentheses`: 374

### Por área

- `aprimoramentos`: 211
- `aventuras`: 41
- `cenarios_lore`: 63
- `classes`: 12
- `criaturas_npcs`: 214
- `itens_equipamentos`: 288
- `kits`: 186
- `linhagens`: 70
- `magias`: 217
- `poderes`: 358
- `racas`: 47
- `regras_base`: 462
- `rituais`: 122
- `tabelas`: 10

## Primeiros itens para revisão

### Acrobático

- ID: `aprimoramento-talentos-acrobatico`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 4
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: 1 ponto:o personagem é muito ágil. Ele ganha um bônus de 10% em todos

### Agilidade

- ID: `aprimoramento-talentos-agilidade`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 7
- Flags: `too_short_possible_cut`
- Amostra: 1 ponto: o personagem ganha um ponto extra em AGI a cada dois níveis.

### Alvo Elusivo

- ID: `aprimoramento-talentos-alvo-elusivo`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 4
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: 1 ponto:o personagem,quando em combate corpo-a-corpo,consegue usar

### Carismático

- ID: `aprimoramento-talentos-carismatico`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 4
- Flags: `too_short_possible_cut`
- Amostra: 1 ponto: o personagem ganha um ponto extra em CAR a cada dois níveis.

### Converso

- ID: `aprimoramento-aprimoramentos-2-converso`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-2` p. 8
- Flags: `too_short_possible_cut`
- Amostra: 2 PONTOS: O psiônico pode converter 4 Pontos de Vida em 1 ponto de PSI.

### Duro na Queda

- ID: `aprimoramento-aprimoramentos-2-duro-na-queda`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-2` p. 3
- Flags: `too_short_possible_cut`
- Amostra: 2 PONTOS:O personagem só recebe apenas metade do dano por quedas.

### Esquiva Sobrenatural

- ID: `aprimoramento-talentos-esquiva-sobrenatural`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 3
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `too_short_possible_cut`
- Amostra: 2 pontos:o personagem pode fazer um teste de AGI para se desviar de

### Ferro Frio

- ID: `aprimoramento-aprimoramentos-3-ferro-frio`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 18
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `too_short_possible_cut`
- Amostra: -2 pontos: o ferro frio se opõe às coisas magicas; seu

### Força

- ID: `aprimoramento-talentos-forca`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 7
- Flags: `too_short_possible_cut`
- Amostra: 1 ponto: o personagem ganha um ponto extra em FR cada dois níveis.

### Magia Máxima

- ID: `aprimoramento-aprimoramentos-3-magia-maxima`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 8
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `too_short_possible_cut`
- Amostra: 2 pontos: A Magia tem efeito máximo (dano máximo, cura máxima). Os

### Médium

- ID: `aprimoramento-aprimoramentos-3-medium`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 9
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `too_short_possible_cut`
- Amostra: 2 pontos: o Personagem consegue se comunicar com espíritos, podendo comprar a

### Presença Horripilante

- ID: `aprimoramento-talentos-presenca-horripilante`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 6
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: 1 ponto: o personagem é horrendo,monstruoso. Todos os seus oponentes

### Raciocínio

- ID: `aprimoramento-talentos-raciocinio`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 7
- Flags: `too_short_possible_cut`
- Amostra: 1 ponto: o personagem ganha um ponto extra em INT a cada dois níveis.

### Resistência

- ID: `aprimoramento-talentos-resistencia`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 7
- Flags: `too_short_possible_cut`
- Amostra: 1 ponto: o personagem ganha um ponto extra em CON a cada dois níveis.

### Resistência à Magia

- ID: `aprimoramento-aprimoramentos-3-resistencia-a-magia`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 14
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `page_number_inside_text`, `too_short_possible_cut`
- Amostra: Não pode ser comprada por Personagens que usam Magia. 1 ponto: seu

### Visão Monocromática

- ID: `aprimoramento-aprimoramentos-1-visao-monocromatica`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-1` p. 17
- Flags: `too_short_possible_cut`
- Amostra: -1 ponto: seu personagem enxerga apenas em preto, branco e tons de cinza.

### Vontade

- ID: `aprimoramento-talentos-vontade`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 7
- Flags: `too_short_possible_cut`
- Amostra: 1 ponto: o personagem ganha um ponto extra em WILL a cada dois níveis.

### A historia

- ID: `abismo-infinito-quick-start--abismo-story-structure`
- Área: `aventuras`
- Fonte: `abismo-infinito-quick-start` p. 38
- Flags: `too_short_possible_cut`
- Amostra: Estrutura de historias em tres fases: Despertar, Pesadelo e Redencao.

### Argos

- ID: `argos`
- Área: `aventuras`
- Fonte: `abismo-infinito-quick-start` p. 12
- Flags: `too_short_possible_cut`
- Amostra: Tipo de nave/equipamento de apoio descrito no quick start de Abismo Infinito.

### Experiencia

- ID: `a-assassina--a-assassina-experience`
- Área: `aventuras`
- Fonte: `a-assassina` p. 5
- Flags: `too_short_possible_cut`
- Amostra: Recompensas de experiencia associadas a conclusao da aventura.

### Hipérions

- ID: `hiperions`
- Área: `aventuras`
- Fonte: `abismo-infinito-quick-start` p. 11
- Flags: `too_short_possible_cut`
- Amostra: Tipo de nave/equipamento espacial descrito no quick start de Abismo Infinito.

### Prometeus

- ID: `prometeus`
- Área: `aventuras`
- Fonte: `abismo-infinito-quick-start` p. 11
- Flags: `too_short_possible_cut`
- Amostra: Tipo de cruzador/nave descrito no quick start de Abismo Infinito.

### ARRANUN

- ID: `arkanun-1e-ultra-raro--arkanun-1e-ultra-raro-arranun-2`
- Área: `cenarios_lore`
- Fonte: `arkanun-1e-ultra-raro` p. 2
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: ARRANUN Marcelo Del Debbio Digitalizado com CamScanner

### Arkanun

- ID: `arkanun-1e-ultra-raro--arkanun-1e-ultra-raro-arkanun-41`
- Área: `cenarios_lore`
- Fonte: `arkanun-1e-ultra-raro` p. 41
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Arkanun Digitalizado com CamScanner

### Nha Eta

- ID: `arkanun-1e-ultra-raro--arkanun-1e-ultra-raro-nha-eta-51`
- Área: `cenarios_lore`
- Fonte: `arkanun-1e-ultra-raro` p. 51
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Nha Eta DO MESTRE RAN N

### Pagina inicial

- ID: `arkanun-1e-ultra-raro--arkanun-1e-ultra-raro-pagina-inicial-1`
- Área: `cenarios_lore`
- Fonte: `arkanun-1e-ultra-raro` p. 1
- Flags: `too_short_possible_cut`, `unbalanced_brackets`, `unbalanced_parentheses`
- Amostra: pa o e e q [ê) (99) E [e] (6) E fo) fa) (o) o) o N o) = = jm)

### Pagina inicial

- ID: `trevas-3-0--trevas-3-0-pagina-inicial-1`
- Área: `cenarios_lore`
- Fonte: `trevas-3-0` p. -
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Pagina inicial

- ID: `trevas-de-marte--trevas-de-marte-pagina-inicial-1`
- Área: `cenarios_lore`
- Fonte: `trevas-de-marte` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: T

### Pagina inicial

- ID: `um-sussurro-nas-trevas--um-sussurro-nas-trevas-pagina-inicial-1`
- Área: `cenarios_lore`
- Fonte: `um-sussurro-nas-trevas` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Um Sussurro

- ID: `um-sussurro-nas-trevas--um-sussurro-nas-trevas-um-sussurro-2`
- Área: `cenarios_lore`
- Fonte: `um-sussurro-nas-trevas` p. 2
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Um Sussurro nas Trevas Alexander “El Brujo” Siqueira

### (2) DRAGÃO ESPECIAL

- ID: `arkanun-1e-ultra-raro--arkanun-1e-ultra-raro-2-dragao-especial-32`
- Área: `criaturas_npcs`
- Fonte: `arkanun-1e-ultra-raro` p. 32
- Flags: `does_not_end_like_complete_sentence`, `encoding_or_ocr_artifact`, `too_short_possible_cut`
- Amostra: (2) DRAGÃO ESPECIAL Digitalizado com CamScanner

### ...E ESSA É À

- ID: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica--anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica-e-essa-e-a-6`
- Área: `criaturas_npcs`
- Fonte: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica` p. 6
- Flags: `starts_mid_sentence_possible_left_cut`, `too_short_possible_cut`
- Amostra: ...E ESSA É À HISTÓRIA. O RESTO VOCÊ JA SABE.

### ; NA à.

- ID: `anjos-jyhad-guerra-santa-biblioteca-elfica--anjos-jyhad-guerra-santa-biblioteca-elfica-na-a-50`
- Área: `criaturas_npcs`
- Fonte: `anjos-jyhad-guerra-santa-biblioteca-elfica` p. 50
- Flags: `does_not_end_like_complete_sentence`, `starts_mid_sentence_possible_left_cut`, `too_short_possible_cut`
- Amostra: ; NA à. PA »,

### ANY

- ID: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica--anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica-any-12`
- Área: `criaturas_npcs`
- Fonte: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica` p. -
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: ANY A \\ ies \ \ é XN “ NY Wort ONDE ESTA ELE? — ANA a gd AA | VORA

### Capítulo 1 - História dos Dragões

- ID: `dragoes-reis-caidos-sistema-daemon--dragoes-reis-caidos-sistema-daemon-capitulo-1-historia-dos-dragoes-11`
- Área: `criaturas_npcs`
- Fonte: `dragoes-reis-caidos-sistema-daemon` p. 11
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Capítulo 1 - História dos Dragões

### Capítulo 2 - Criação de Personagem

- ID: `dragoes-reis-caidos-sistema-daemon--dragoes-reis-caidos-sistema-daemon-capitulo-2-criacao-de-personagem-21`
- Área: `criaturas_npcs`
- Fonte: `dragoes-reis-caidos-sistema-daemon` p. 21
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Capítulo 2 - Criação de Personagem

### Death Knight

- ID: `death-knight`
- Área: `criaturas_npcs`
- Fonte: `alastores-a-justica-infernal` p. 41
- Flags: `too_short_possible_cut`
- Amostra: Ficha de criatura/inimigo apresentada no suplemento Alastores.

### Documento DOCX estruturado

- ID: `tabela-de-fadiga-dos-jogadores-e-npc--docx-structured-source`
- Área: `criaturas_npcs`
- Fonte: `tabela-de-fadiga-dos-jogadores-e-npc` p. -
- Flags: `too_short_possible_cut`
- Amostra: Fonte DOCX estruturada: Tabela de Fadiga dos Jogadores e NPC.

### DragõeS

- ID: `dragoes-reis-caidos-sistema-daemon--dragoes-reis-caidos-sistema-daemon-dragoes-1`
- Área: `criaturas_npcs`
- Fonte: `dragoes-reis-caidos-sistema-daemon` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: DragõeS Reis Caídos

### Dragões

- ID: `dragoes2--dragoes2-dragoes-1`
- Área: `criaturas_npcs`
- Fonte: `dragoes2` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Dragões by BURP

### GUIA DOS

- ID: `guia-dos-dragoes-1-biblioteca-elfica--guia-dos-dragoes-1-biblioteca-elfica-guia-dos-3`
- Área: `criaturas_npcs`
- Fonte: `guia-dos-dragoes-1-biblioteca-elfica` p. 3
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: GUIA DOS DRAGÕES Maury “Shi Dark” Abreu 3

### GUIA DOS

- ID: `guia-dragoes-vol-ii--guia-dragoes-vol-ii-guia-dos-3`
- Área: `criaturas_npcs`
- Fonte: `guia-dragoes-vol-ii` p. 3
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: GUIA DOS DRAGÕES Volume II Maury “Shi Dark” Abreu 3

### Guerreiros Notaveis

- ID: `alastores-a-justica-infernal--alastores-guerreiros-notaveis`
- Área: `criaturas_npcs`
- Fonte: `alastores-a-justica-infernal` p. -
- Flags: `too_short_possible_cut`
- Amostra: Guerreiros e figuras notaveis dos Alastores, incluindo Gathering e Seddim.

### Marcela Del Debato

- ID: `anjos-a-cidade-de-prata--anjos-a-cidade-de-prata-marcela-del-debato-1`
- Área: `criaturas_npcs`
- Fonte: `anjos-a-cidade-de-prata` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: M Marcela Del Debato

### Marcelo Del Debbio

- ID: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica--anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica-marcelo-del-debbio-1`
- Área: `criaturas_npcs`
- Fonte: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Marcelo Del Debbio O Evandro Gregori

### Mortos Vivos

- ID: `mortos-vivos--mortos-vivos-mortos-vivos-2`
- Área: `criaturas_npcs`
- Fonte: `mortos-vivos` p. 2
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Mortos Vivos 2ª edição

### PARADOS!

- ID: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica--anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica-parados-17`
- Área: `criaturas_npcs`
- Fonte: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica` p. 17
- Flags: `too_short_possible_cut`
- Amostra: PARADOS! POLÍCIA! VEM COMIGO SE QUISER | VIVER! SOU \ AMIGA!

### Pagina inicial

- ID: `anjos-jyhad-guerra-santa-biblioteca-elfica--anjos-jyhad-guerra-santa-biblioteca-elfica-pagina-inicial-1`
- Área: `criaturas_npcs`
- Fonte: `anjos-jyhad-guerra-santa-biblioteca-elfica` p. 1
- Flags: `does_not_end_like_complete_sentence`, `starts_mid_sentence_possible_left_cut`, `too_short_possible_cut`
- Amostra: E! Ê E q 5 rf : g E q

### Pagina inicial

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-pagina-inicial-1`
- Área: `criaturas_npcs`
- Fonte: `demonios-a-divina-comedia` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Pagina inicial

- ID: `guia-de-monstros-de-arton--guia-de-monstros-de-arton-pagina-inicial-1`
- Área: `criaturas_npcs`
- Fonte: `guia-de-monstros-de-arton` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Pagina inicial

- ID: `guia-dos-dragoes-1-biblioteca-elfica--guia-dos-dragoes-1-biblioteca-elfica-pagina-inicial-1`
- Área: `criaturas_npcs`
- Fonte: `guia-dos-dragoes-1-biblioteca-elfica` p. -
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: 1 2

### Pagina inicial

- ID: `mortos-vivos--mortos-vivos-pagina-inicial-1`
- Área: `criaturas_npcs`
- Fonte: `mortos-vivos` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Pagina inicial

- ID: `guia-dragoes-vol-ii--guia-dragoes-vol-ii-pagina-inicial-1`
- Área: `criaturas_npcs`
- Fonte: `guia-dragoes-vol-ii` p. -
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: 1 2

### ARMAS DA SEGUNDA GUERRA

- ID: `armas-da-segunda-guerra-mundial--armas-da-segunda-guerra-mundial-armas-da-segunda-guerra-30`
- Área: `itens_equipamentos`
- Fonte: `armas-da-segunda-guerra-mundial` p. -
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: ARMAS DA SEGUNDA GUERRA MUNDIAL EIXO ARMAS DA SEGUNDA GUERRA MUNDIAL Alemanha

### ARMAS DA SEGUNDA GUERRA

- ID: `armas-da-segunda-guerra-mundial--armas-da-segunda-guerra-mundial-armas-da-segunda-guerra-17`
- Área: `itens_equipamentos`
- Fonte: `armas-da-segunda-guerra-mundial` p. 17
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: ARMAS DA SEGUNDA GUERRA MUNDIAL FRANÇA

### ARMAS DA SEGUNDA GUERRA

- ID: `armas-da-segunda-guerra-mundial--armas-da-segunda-guerra-mundial-armas-da-segunda-guerra-21`
- Área: `itens_equipamentos`
- Fonte: `armas-da-segunda-guerra-mundial` p. 21
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: ARMAS DA SEGUNDA GUERRA MUNDIAL INGLATERRA

### ARMAS DA SEGUNDA GUERRA

- ID: `armas-da-segunda-guerra-mundial--armas-da-segunda-guerra-mundial-armas-da-segunda-guerra-25`
- Área: `itens_equipamentos`
- Fonte: `armas-da-segunda-guerra-mundial` p. 25
- Flags: `too_short_possible_cut`
- Amostra: ARMAS DA SEGUNDA GUERRA MUNDIAL U.R.S.S.

### ARMAS DA SEGUNDA GUERRA

- ID: `armas-da-segunda-guerra-mundial--armas-da-segunda-guerra-mundial-armas-da-segunda-guerra-36`
- Área: `itens_equipamentos`
- Fonte: `armas-da-segunda-guerra-mundial` p. 36
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `too_short_possible_cut`
- Amostra: ARMAS DA SEGUNDA GUERRA MUNDIAL I t á l i a

### ARMAS DA SEGUNDA GUERRA

- ID: `armas-da-segunda-guerra-mundial--armas-da-segunda-guerra-mundial-armas-da-segunda-guerra-39`
- Área: `itens_equipamentos`
- Fonte: `armas-da-segunda-guerra-mundial` p. 39
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: ARMAS DA SEGUNDA GUERRA MUNDIAL JAPãO

### Areia de Agaures

- ID: `areia-de-agaures`
- Área: `itens_equipamentos`
- Fonte: `alastores-a-justica-infernal` p. 34
- Flags: `too_short_possible_cut`
- Amostra: Alforja/objeto magico citado na secao de objetos de Alastores.

### Armas, Armaduras &

- ID: `armamedieval--armamedieval-armas-armaduras-1`
- Área: `itens_equipamentos`
- Fonte: `armamedieval` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Armas, Armaduras & Escudos Por Lobo de Diamante

### Caixa e Besouro

- ID: `caixa-e-besouro`
- Área: `itens_equipamentos`
- Fonte: `alastores-a-justica-infernal` p. 34
- Flags: `too_short_possible_cut`
- Amostra: Objeto magico descrito no suplemento Alastores.

### Pagina inicial

- ID: `armas-da-segunda-guerra-mundial--armas-da-segunda-guerra-mundial-pagina-inicial-1`
- Área: `itens_equipamentos`
- Fonte: `armas-da-segunda-guerra-mundial` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Pagina inicial

- ID: `guia-de-armas-de-fogo-3a-edicao--guia-de-armas-de-fogo-3a-edicao-pagina-inicial-1`
- Área: `itens_equipamentos`
- Fonte: `guia-de-armas-de-fogo-3a-edicao` p. -
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### A Contenda Eterna

- ID: `luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br--luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br-a-contenda-eterna-1`
- Área: `regras_base`
- Fonte: `luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: A Contenda Eterna A Contenda Eterna João Fernando Rech Wachelke

### Atributos

- ID: `atributos--atributos-atributos-1`
- Área: `regras_base`
- Fonte: `atributos` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Atributos Por Lobo

### Capítulo 8 – Armas e Equipamentos

- ID: `daemon-medieval--daemon-medieval-capitulo-8-armas-e-equipamentos-52`
- Área: `regras_base`
- Fonte: `daemon-medieval` p. 52
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Capítulo 8 – Armas e Equipamentos 52

### Capítulo 8 – Armas e Equipamentos

- ID: `daemon-medieval--daemon-medieval-capitulo-8-armas-e-equipamentos-54`
- Área: `regras_base`
- Fonte: `daemon-medieval` p. 54
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Capítulo 8 – Armas e Equipamentos 54

### Daemon Medieval

- ID: `daemon-medieval--daemon-medieval-daemon-medieval-51`
- Área: `regras_base`
- Fonte: `daemon-medieval` p. 51
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Daemon Medieval 51

### Daemon Medieval

- ID: `daemon-medieval--daemon-medieval-daemon-medieval-53`
- Área: `regras_base`
- Fonte: `daemon-medieval` p. 53
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Daemon Medieval 53

### Documento DOCX estruturado

- ID: `compendio-de-regras-daemon-trevas--docx-structured-source`
- Área: `regras_base`
- Fonte: `compendio-de-regras-daemon-trevas` p. -
- Flags: `too_short_possible_cut`
- Amostra: Fonte DOCX estruturada: Compendio de regras DAEMON Trevas.

### Documento DOCX estruturado

- ID: `regras-de-boa-convivencia--docx-structured-source`
- Área: `regras_base`
- Fonte: `regras-de-boa-convivencia` p. -
- Flags: `too_short_possible_cut`
- Amostra: Fonte DOCX estruturada: Regras de boa convivência.

### E X P A N D I D O E M O D I F I C A D O

- ID: `modulo-basico-expandido-e-modificado--modulo-basico-expandido-e-modificado-e-x-p-a-n-d-i-d-o-e-m-o-d-i-f-i-c-a-d-o-1`
- Área: `regras_base`
- Fonte: `modulo-basico-expandido-e-modificado` p. 1
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `starts_mid_sentence_possible_left_cut`, `too_short_possible_cut`
- Amostra: E X P A N D I D O E M O D I F I C A D O M Ó D U L O B Á S I C O

### Hakusho

- ID: `yuyu-hakusho-rpg-para-daemon--yuyu-hakusho-rpg-para-daemon-hakusho-1`
- Área: `regras_base`
- Fonte: `yuyu-hakusho-rpg-para-daemon` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Hakusho RPG Por Marcelo Matos “Guaxinim”, Ajota & Grupo de RPG PVH Yu Yu V2.01

### Iniciativa

- ID: `mago-sistema-daemon--mago-sistema-daemon-iniciativa-1`
- Área: `regras_base`
- Fonte: `mago-sistema-daemon` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Iniciativa DAEMON Hatalíbio Almeida Sistema Daemon

### Pagina inicial

- ID: `daemon-anime-rpg--daemon-anime-rpg-pagina-inicial-1`
- Área: `regras_base`
- Fonte: `daemon-anime-rpg` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Pagina inicial

- ID: `modulo-combate--modulo-combate-pagina-inicial-1`
- Área: `regras_base`
- Fonte: `modulo-combate` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Pagina inicial

- ID: `sistema-daemon-modulo-basico-dragonslayer-01-e-02--sistema-daemon-modulo-basico-dragonslayer-01-e-02-pagina-inicial-1`
- Área: `regras_base`
- Fonte: `sistema-daemon-modulo-basico-dragonslayer-01-e-02` p. -
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Pagina inicial

- ID: `tagmar-daemon-versao-completa--tagmar-daemon-versao-completa-pagina-inicial-1`
- Área: `regras_base`
- Fonte: `tagmar-daemon-versao-completa` p. -
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

### Sistema Daemon

- ID: `mago-sistema-daemon--mago-sistema-daemon-sistema-daemon-2`
- Área: `regras_base`
- Fonte: `mago-sistema-daemon` p. 2
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Sistema Daemon 1ª edição

### TORMENTA RPG – SISTEMA DAEMON – VERSÃO DE THIAGO “MESTRE KWAN” RODRIGUES (181-181)

- ID: `daemon-tormenta--daemon-tormenta-tormenta-rpg-sistema-daemon-versao-de-thiago-mestre-kwan-rodrigues-1-19`
- Área: `regras_base`
- Fonte: `daemon-tormenta` p. 181
- Flags: `does_not_end_like_complete_sentence`, `encoding_or_ocr_artifact`, `too_short_possible_cut`
- Amostra: TORMENTA RPG – SISTEMA DAEMON – VERSÃO DE THIAGO “MESTRE KWAN” RODRIGUES 181

### www.daemon.com.br

- ID: `varna-chamado-da-guerra--varna-chamado-da-guerra-www-daemon-com-br-2`
- Área: `regras_base`
- Fonte: `varna-chamado-da-guerra` p. 2
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: www.daemon.com.br fone/fax: (11) 5539-1122 São Paulo - SP

### ADEQUADO

- ID: `grimorio--grimorio-adequado-1`
- Área: `rituais`
- Fonte: `grimorio` p. -
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: ADEQUADO Pak 16 E Marcelo Del Debbio system Sistema Daemon

### Rituais

- ID: `alastores-a-justica-infernal--alastores-rituais`
- Área: `rituais`
- Fonte: `alastores-a-justica-infernal` p. -
- Flags: `too_short_possible_cut`
- Amostra: Rituais como Convocar Lukhavim, Sellas locum e Ipsa Nomina.

### Documento DOCX estruturado

- ID: `tabela-e-regras-para-magos--docx-structured-source`
- Área: `tabelas`
- Fonte: `tabela-e-regras-para-magos` p. -
- Flags: `too_short_possible_cut`
- Amostra: Fonte DOCX estruturada: Tabela e Regras para magos.

### Afinidade com Magia

- ID: `aprimoramento-aprimoramentos-3-afinidade-com-magia`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 10
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: Apenas para não-magos. 1 ponto: seu Personagem, apesar de não ser um mago, possui algum tipo de afinidade com um dos Caminhos de Magia. Ele recebe sempre 1D de proteção contra Magias desse Caminho e pode realizar efeitos sutis (equivalentes a uma Magia de Focu

### Alma Escravizada

- ID: `aprimoramento-aprimoramentos-3-alma-escravizada`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 16
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: -3 pontos: sua alma foi escravizada por habitantes de Spiritum, criaturas poderosas que agora o enviam para várias missões, ou o forçam a cometer atos insanos. Muitas vezes o Personagem possui livre arbítrio enquanto seu dono não necessita dele para alguma mis

### Analfabeto

- ID: `aprimoramento-aprimoramentos-3-analfabeto`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 16
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: -1 ponto: por algum motivo, o Personagem não aprendeu a ler e escrever. Pode ser um marginal de rua, um trabalhador rural, ou apenas alguém que nunca teve chance de ir à escola. Um analfabeto não tem Perícias que tenham valor inicial baseado em INT: perícias d

### Anjo da Guarda

- ID: `aprimoramento-aprimoramentos-3-anjo-da-guarda`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 10
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: 2 pontos: o Personagem possui um espírito guia, que às vezes pode se comunicar com ele em sonhos. O espírito pode passar algum tipo de dica para o Personagem, quando o Mestre julgar apropriado. Quem é o espírito, e porque ele ajuda o

### Bom Senso

- ID: `aprimoramento-aprimoramentos-3-bom-senso`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 3
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: 1 ponto: todas as vezes que um Personagem que tenha bom senso for fazer alguma coisa obviamente estúpida, o Mestre pode dizer a ele que o que ele pretende fazer é uma burrice. Este Aprimoramento é muito útil para Jogadores iniciantes, como uma forma de justifi

### Caçador de Vampiros

- ID: `aprimoramento-aprimoramentos-3-cacador-de-vampiros`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 1
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: 1 ponto: o Personagem é treinado para caçar vampiros e possui um amplo conhecimento sobre suas fraquezas, poderes e diferentes linhagens, mitos e lendas. Em termos de jogo, o

### Comunicação em Sonhos

- ID: `aprimoramento-aprimoramentos-3-comunicacao-em-sonhos`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 11
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: 2 pontos: o Personagem pode se comunicar com outras pessoas enquanto elas sonham. Para isso a pessoa deve estar adormecida. O Personagem precisa de alguns minutos de transe até formar uma conexão. Não existe um limite de distncia para a comunicao em sonhos, ma

### Conhecimento de Itens Mágicos

- ID: `aprimoramento-aprimoramentostormenta-conhecimento-de-itens-magicos`
- Área: `aprimoramentos`
- Fonte: `aprimoramentostormenta` p. 4
- Flags: `aprimoramento_without_cost_marker`, `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: [regional: Wynlla]: Muitos nativos de Wynlla tem um forte conhecimento sobre itens mágicos. Em regras, o Personagem é capaz de identificar itens mágicos com 50% de chance de sucesso e mesmo que não seja um mago é capaz de ativar itens mágicos que exijam conhec

### Conjuração

- ID: `aprimoramento-aprimoramentos-3-conjuracao`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 11
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: 4 pontos: com este Aprimoramento, o Personagem possui o conhecimento sobre a Forma-Pensamento e a capacidade de canalizar essa energia para os planos físicos. Com um Teste de WILL, o Personagem é capaz de tatear o mundo espiritual em busca de algum objeto e ma

### Escutar

- ID: `aprimoramento-aprimoramentostormenta-escutar`
- Área: `aprimoramentos`
- Fonte: `aprimoramentostormenta` p. 6
- Flags: `aprimoramento_without_cost_marker`, `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `starts_mid_sentence_possible_left_cut`
- Amostra: e Sobrevivência contra qualquer tipo de goblinóide (goblins, hobgoblins e bugbears apenas). Esse Aprimoramento Regional é mais comum entre os nativos do lado sul de Tyrondir, que tem mais contato com a Aliança Negra. (1 ponto): Personagens que tenham passado p

### Sanguinário

- ID: `aprimoramento-aprimoramentos-1-sanguinario`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-1` p. 16
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: -1 ponto: quando o personagem entra em uma batalha, esta será até o fim. Não existe misericórdia ou rendição: um dos dois lados deve perder obrigatoriamente. Para o Personagem, a luta se prolongará até que ele reduza seus inimigos à poças de san- gue. Assim co

### Sincronia

- ID: `aprimoramento-aprimoramentos-2-sincronia`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-2` p. 6
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: 1 PONTO: O personagem adquiriu um árduo treinamento em grupo. Quando ele entra em combate junto com um ou mais colegas (personagens que devem obrigatoriamente possuir este Aprimoramento) eles atuam como se fosse uma só criatura - combinando as características

### Sortudo

- ID: `aprimoramento-aprimoramentos-3-sortudo`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 14
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: 2 pontos: este Personagem é portador de uma sorte incrível. Uma vez por sessão de jogo, o Jogador pode Rolar novamente um dado caso tenha falhado em um Teste (qualquer tipo de rolagem de dados). Ele deve anunciar essa decisão ANTES de rolar os dados (ou seja,

### Tutor

- ID: `aprimoramento-aprimoramentos-3-tutor`
- Área: `aprimoramentos`
- Fonte: `aprimoramentos-3` p. 9
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `page_number_inside_text`
- Amostra: Todo o Personagem Mago teve, em algum momento de sua aprendizado, um Tutor que lhe ensinou sobre a Magia. Se você desejar que este Tutor ainda esteja com o seu personagem por alguma razão, então gaste seu pontos neste Aprimoramento. O Mestre deve criar toda a

### 2. Verifique detalhes da história.

- ID: `inquisicao-biblioteca-elfica--inquisicao-biblioteca-elfica-2-verifique-detalhes-da-historia-11`
- Área: `aventuras`
- Fonte: `inquisicao-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 2. Verifique detalhes da história. Faça esta parte em conjunto com o Mestre, pois muito do que for escolhido aqui será utilizado por ele como fundo para sua Aventura posterior. Tente localizar a his- . tória do seu Personagem com a dos ou tros Personagens da C

### A Temperanl'"

- ID: `guia-de-itens-magicos--guia-de-itens-magicos-a-temperanl-248`
- Área: `aventuras`
- Fonte: `guia-de-itens-magicos` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: A Temperanl'" Arcano Quatorze (Samekh) Significa acordos ou comprometimentos. Este Arcana indica quea soluc;ao para a Aventura reside em urn acardo, e dificilmente 0 problema sent solucionado de Qutra maneira. o Diabo Arcana Quinz. (Ayin) o Diabo representa 0

### CAMPANHA

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-campanha-106`
- Área: `aventuras`
- Fonte: `demonios-a-divina-comedia` p. 106
- Flags: `ends_with_connector_possible_cut`
- Amostra: CAMPANHA Seu personagem foi o único sobrevivente de uma aventura? Dos outros quatro personagens, 2 foram destruídos pelos Templários, um ficou louco, e o ultimo acabou aprisionado em Arkanun para sempre. Em um RPG de horror, sobreviver a uma aventura muitas ve

### Capítulo 10

- ID: `daemon-medieval--daemon-medieval-capitulo-10-60`
- Área: `aventuras`
- Fonte: `daemon-medieval` p. 60
- Flags: `ends_with_connector_possible_cut`
- Amostra: Capítulo 10 – Regras de testes e combate 60 Capítulo 10 Regras de Testes e Combate or mais cautelosos que os Personagens sejam, por maiores os cuidados que eles tenham, em algum momento da Aventura eles serão obrigados a enfrentar algo ou alguém. Para isso, é

### Cenários

- ID: `um-sussurro-nas-trevas--um-sussurro-nas-trevas-cenarios-35`
- Área: `aventuras`
- Fonte: `um-sussurro-nas-trevas` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Cenários Não esqueça que os anos 20 estão repletos de cenários que não estão relacionados com o gangsterismo e as melindrosas. Em Nova York, o Harlem tinha a melhor vida noturna do mundo conhecido para negros e brancos ricos, e circulava rumores sobre locais o

### Combate não Mortal

- ID: `daemon-anime-rpg--daemon-anime-rpg-combate-nao-mortal-113`
- Área: `aventuras`
- Fonte: `daemon-anime-rpg` p. 113
- Flags: `ends_with_connector_possible_cut`
- Amostra: Combate não Mortal Dois Personagens podem estar brigando e não lutando. São os casos clássicos de Personagens da campanha que se desentenderam por algum problema da aventura e acabam perdendo a paciência um com o outro. As lutas de Boxe e Artes Marciais também

### Considerações

- ID: `luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br--luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br-consideracoes-125`
- Área: `aventuras`
- Fonte: `luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Considerações Finais Agradecimentos João Agradeço a meu irmão Luiz por ter me ajudado nesse projeto, sem ele isso aqui não “rolava”. Agradeço a Moema, meu amor, por ter suportado todas as sessões de jogo e “alabardas” e “bolas de rubi”. Também mando um abraço

### EVOLUÇÃO ALTERNATIVA

- ID: `evolucao-alternativa--evolucao-alternativa-evolucao-alternativa-3`
- Área: `aventuras`
- Fonte: `evolucao-alternativa` p. -
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: EVOLUÇÃO ALTERNATIVA Originalmente no sistema Daemon, o tipo de campanha é o fator que determina o potencial inicial de um personagem. Em campanhas épicas um personagem inicial equivale a um personagem de alto nível de uma campanha mais realista. Porém essa di

### Experiência

- ID: `um-sussurro-nas-trevas--um-sussurro-nas-trevas-experiencia-32`
- Área: `aventuras`
- Fonte: `um-sussurro-nas-trevas` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Experiência Dos outros quatro Personagens da Campanha, dois foram destruídos pela Inquisição, um ficou louco e o último acabou aprisionado em Arkanun para sempre. Em um RPG de horror, sobreviver a uma Aventura muitas vezes já é um prêmio em si, mas para recomp

### PASSADO

- ID: `conan--conan-passado-4`
- Área: `aventuras`
- Fonte: `conan` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: 4 PASSADO Imagine o que aconteceu com seu Personagem desde o seu nascimento até a data do início da Campanha. Escreva a história primeiro, depois se preocupe com os detalhes numéricos. Núme- ros não são importantes, o importante é criar um Personagem coe- rent

### Perguntas

- ID: `spiritum--spiritum-perguntas-19`
- Área: `aventuras`
- Fonte: `spiritum` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Perguntas Válido para esta encarnação, mas recomendamos que Jo- gadores e Mestres resolvem pequenas pontas em encarnações passadas, que serão resolvidas durante a campanha. Irmãos, amigos e colegas nunca estão com seu Personagem por acaso. Invista algum tempo

### REGRAS E TESÍES

- ID: `sistema-daemon-modulo-basico-dragonslayer-01-e-02--sistema-daemon-modulo-basico-dragonslayer-01-e-02-regras-e-tesies-25`
- Área: `aventuras`
- Fonte: `sistema-daemon-modulo-basico-dragonslayer-01-e-02` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: REGRAS E TESÍES Por mais cautelosos que os Personagens sejam, por maiores os cuidados que eles tenham, em algum momento da Aventura eles serão obnigados a enfrentar algo ou alguém. Para isso, é necessário definir com bastante cuidado as regras para Combates e

### Regras e Testes

- ID: `one-punch-man-rpg--one-punch-man-rpg-regras-e-testes-22`
- Área: `aventuras`
- Fonte: `one-punch-man-rpg` p. 22
- Flags: `ends_with_connector_possible_cut`
- Amostra: Regras e Testes Por mais cautelosos que os Personagens sejam, por maiores os cuidados que eles tenham, em algum momento da Aventura eles serão obrigados a enfrentar algo ou alguém. Para isso, é necessário definir com bastante cuidado as regras para Combates e

### Regras e Testes

- ID: `spiritum--spiritum-regras-e-testes-67`
- Área: `aventuras`
- Fonte: `spiritum` p. 67
- Flags: `ends_with_connector_possible_cut`
- Amostra: Regras e Testes Por mais cautelosos que os Personagens sejam, por maiores os cuidados que eles tenham, em algum momento da Aventura eles serão obrigados a enfrentar algo ou alguém. Para isso, é necessário definir com bastante cuidado as regras para Combates e

### Viajantes Espirituais

- ID: `spiritum--spiritum-viajantes-espirituais-41`
- Área: `aventuras`
- Fonte: `spiritum` p. 41
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Viajantes Espirituais Viajantes espirituais, também conhecidos como viajantes astrais, são aventureiros que escolheram os vales de Spiritum para suas campanhas. Podem ser aventureiros isolados ou per- tencerem a grandes grupos organizados (como os Estudiosos d

### '-,,, (,,<mp't" "''''ulm,,,«do ,\""",,,,,",,,,,,.,,,,,1,, :,,,,

- ID: `trevas-3-0--trevas-3-0-mp-t-ulm-do-1-59`
- Área: `cenarios_lore`
- Fonte: `trevas-3-0` p. 59
- Flags: `critical_ocr_gibberish`, `ends_with_connector_possible_cut`, `invalid_title_or_ocr_header`, `symbol_noise_ocr`, `unbalanced_parentheses`
- Amostra: '-,,, (,,<mp't" "''''ulm,,,«do ,\""",,,,,",,,,,,.,,,,,1,, :,,,, .1"""" '''' ,·",""tc' ",," .1,,«,.., d, <>",1>,. o><go<u",I" "nu P"'''''''' I"'~ti.;. den"" J" \;r""de h ",m"I,,1<, Sl~ f:1,nJ<o "".- do. do. ~I,p" !'.1I0' , qu< : .. ,'07", (0""'«'" .,."." J< '.,

### A Lei

- ID: `trevas-3-0--trevas-3-0-a-lei-173`
- Área: `cenarios_lore`
- Fonte: `trevas-3-0` p. 173
- Flags: `critical_ocr_gibberish`, `ends_with_connector_possible_cut`, `symbol_noise_ocr`, `unbalanced_parentheses`
- Amostra: A Lei ','" d. '"'' u,J .. I~d, l"n<b".l.I"'~-u" .I. <.,dj '-e,,,. r,c"-'''' P.roc'I><"""n'" nn,·o. Rt,u:U.,lou_ ,,,, f""f,>d".<k.J;,,,,,,,. ,n,",u><;""l'''~''''''''-'." "'''no. ,I, .Iu~,,<l_ 1""""u<>' ,"'" 4.IX~) mo. ,Jc ,d,<k. «0""" '1"< ,,,,,1< nl':'"""" ,1"

### A Tdade

- ID: `trevas-3-0--trevas-3-0-a-tdade-178`
- Área: `cenarios_lore`
- Fonte: `trevas-3-0` p. -
- Flags: `critical_ocr_gibberish`, `ends_with_connector_possible_cut`, `symbol_noise_ocr`
- Amostra: A Tdade D<,,, "J. <k m,lh 'f<" .1< ""'" ",,,,,, 10m' """,ou...., .. ,, 'c Clm duro .... " '1 ""I,. f,,, funJ",h "" ",,,,I ,~, ><'<:olo ~~ 11 O ,lo,."" Tn"k I"'''''''' J. I~',çl<> ,~, ,-<,~" I,,~,,<m < t<."".N,,,,,,,,,,,,ru'h po<n""'f""'''I'''''«t<,f,,,,,,,,,<m

### Advog~do

- ID: `trevas-3-0--trevas-3-0-advog-do-41`
- Área: `cenarios_lore`
- Fonte: `trevas-3-0` p. 41
- Flags: `critical_ocr_gibberish`, `ends_with_connector_possible_cut`, `symbol_noise_ocr`, `unbalanced_parentheses`
- Amostra: Advog~do F..ú«m ~">'-' ... d< ,.I"~" n,,. ~u'" "'" aJ",I' ,J" poJ, ''''''. "", "" I~,""h , ,j" ·II~T'\·_\S. 8" '""'''''' ,,, Ih",,,,!;,,", 'io ~,lvog."I". <"","",;,;" .. , "" ~.1l" «: "-"",oJ,,, <lo .1r.UI:O' (o",,-,e,-,,," pt"hl." ... ,I. ,,' .. ,k '~'n,I,. n

### llllllu

- ID: `trevas-3-0--trevas-3-0-llllllu-122`
- Área: `cenarios_lore`
- Fonte: `trevas-3-0` p. 122
- Flags: `critical_ocr_gibberish`, `ends_with_connector_possible_cut`, `symbol_noise_ocr`, `unbalanced_brackets`, `unbalanced_parentheses`
- Amostra: llllllu "HHH : Ii"! ;; i-!i~~ ~s~~~ ~ § !l-;: C ~ ~ mil' mttt HíHi t}lW lf~{t HW ~ ~ f g ~ HlU ~. ~ ~ • , .., ('J } ~~ ,... • l Pt-~ ~ ::; iI '" ~ ~ o ? &. v , , ,q ,"1 [1 8 r- ~ ~S * ~ g ~ ,; [ ~ ~ f ~ ! i ~ ; ~ e r , li 1 ~ ~ i:' ~ k 5 I ª ~ 11 ;'1 ~ t t:; ~

### & jJuDaísme

- ID: `anjos-jyhad-guerra-santa-biblioteca-elfica--anjos-jyhad-guerra-santa-biblioteca-elfica-jjudaisme-11`
- Área: `criaturas_npcs`
- Fonte: `anjos-jyhad-guerra-santa-biblioteca-elfica` p. 11
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: & jJuDaísme INTREDUÇÃO O nome judaísmo vem do chamado reino de Judá, antigo reino do Oriente Médio e, durante muito tempo, a palavra ju- deu foi usada para designar os habitantes deste reino. Com o passar os séculos, o termo passou a abranger os seguidores der
