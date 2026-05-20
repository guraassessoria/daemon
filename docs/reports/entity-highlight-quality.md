# Auditoria semântica inicial dos destaques

Este relatório identifica trechos publicados que parecem cortados, colados, duplicados, incompletos ou contaminados por artefatos de extração.
Ele não substitui conferência com o PDF/texto oficial; serve para priorizar revisão profissional.

## Resumo

- Registros sinalizados: 2301

### Flags

- `aprimoramento_without_cost_marker`: 23
- `critical_ocr_gibberish`: 71
- `does_not_end_like_complete_sentence`: 1417
- `encoding_or_ocr_artifact`: 166
- `ends_with_connector_possible_cut`: 108
- `front_matter_or_index_block`: 3
- `hyphenated_word_split`: 984
- `invalid_title_or_ocr_header`: 6
- `lowercase_sentence_after_section_possible_leak`: 389
- `many_cost_markers_possible_merged_aprimoramentos`: 7
- `page_number_inside_text`: 199
- `repeated_fragment_possible_duplication`: 28
- `starts_mid_sentence_possible_left_cut`: 20
- `symbol_noise_ocr`: 67
- `too_short_possible_cut`: 56
- `unbalanced_brackets`: 53
- `unbalanced_parentheses`: 262

### Por área

- `aprimoramentos`: 189
- `aventuras`: 4
- `cenarios_lore`: 75
- `classes`: 12
- `criaturas_npcs`: 301
- `itens_equipamentos`: 118
- `kits`: 293
- `linhagens`: 70
- `magias`: 396
- `poderes`: 460
- `racas`: 54
- `regras_base`: 255
- `rituais`: 74

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

### Força

- ID: `aprimoramento-talentos-forca`
- Área: `aprimoramentos`
- Fonte: `talentos` p. 7
- Flags: `too_short_possible_cut`
- Amostra: 1 ponto: o personagem ganha um ponto extra em FR cada dois níveis.

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

### Trevas do

- ID: `onmyodo--onmyodo-trevas-do-1`
- Área: `cenarios_lore`
- Fonte: `onmyodo` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Trevas do Oriente ONMYODO HENRIQUE “MORCEGO” SANTOS

### Trevas do

- ID: `oriente-cronologia--oriente-cronologia-trevas-do-1`
- Área: `cenarios_lore`
- Fonte: `oriente-cronologia` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Trevas do Oriente Cronologia HENRIQUE “MORCEGO” SANTOS

### Trevas do

- ID: `trevas-do-oriente-28-palacios--trevas-do-oriente-28-palacios-trevas-do-1`
- Área: `cenarios_lore`
- Fonte: `trevas-do-oriente-28-palacios` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Trevas do Oriente OS 28 PALACIOS LUNARES HENRIQUE “MORCEGO” SANTOS

### Trevas do

- ID: `youkai-kyuukai--youkai-kyuukai-trevas-do-1`
- Área: `cenarios_lore`
- Fonte: `youkai-kyuukai` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Trevas do Oriente YOUKAI E KYUUKAI HENRIQUE “MORCEGO” SANTOS

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

### Death Knight

- ID: `death-knight`
- Área: `criaturas_npcs`
- Fonte: `alastores-a-justica-infernal` p. 41
- Flags: `too_short_possible_cut`
- Amostra: Ficha de criatura/inimigo apresentada no suplemento Alastores.

### Dragões

- ID: `dragoes2--dragoes2-dragoes-1`
- Área: `criaturas_npcs`
- Fonte: `dragoes2` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Dragões by BURP

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

### Areia de Agaures

- ID: `areia-de-agaures`
- Área: `itens_equipamentos`
- Fonte: `alastores-a-justica-infernal` p. 34
- Flags: `too_short_possible_cut`
- Amostra: Alforja/objeto magico citado na secao de objetos de Alastores.

### Argos

- ID: `argos`
- Área: `itens_equipamentos`
- Fonte: `abismo-infinito-quick-start` p. 12
- Flags: `too_short_possible_cut`
- Amostra: Tipo de nave/equipamento de apoio descrito no quick start de Abismo Infinito.

### Caixa e Besouro

- ID: `caixa-e-besouro`
- Área: `itens_equipamentos`
- Fonte: `alastores-a-justica-infernal` p. 34
- Flags: `too_short_possible_cut`
- Amostra: Objeto magico descrito no suplemento Alastores.

### Capítulo 8 – Armas e Equipamentos

- ID: `daemon-medieval--daemon-medieval-capitulo-8-armas-e-equipamentos-52`
- Área: `itens_equipamentos`
- Fonte: `daemon-medieval` p. 52
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Capítulo 8 – Armas e Equipamentos 52

### Capítulo 8 – Armas e Equipamentos

- ID: `daemon-medieval--daemon-medieval-capitulo-8-armas-e-equipamentos-54`
- Área: `itens_equipamentos`
- Fonte: `daemon-medieval` p. 54
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Capítulo 8 – Armas e Equipamentos 54

### Hipérions

- ID: `hiperions`
- Área: `itens_equipamentos`
- Fonte: `abismo-infinito-quick-start` p. 11
- Flags: `too_short_possible_cut`
- Amostra: Tipo de nave/equipamento espacial descrito no quick start de Abismo Infinito.

### Prometeus

- ID: `prometeus`
- Área: `itens_equipamentos`
- Fonte: `abismo-infinito-quick-start` p. 11
- Flags: `too_short_possible_cut`
- Amostra: Tipo de cruzador/nave descrito no quick start de Abismo Infinito.

### Adequado

- ID: `regra-grimorio-grimorio-adequado-1`
- Área: `regras_base`
- Fonte: `grimorio` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: ADEQUADO Pak 16 E Marcelo Del Debbio system Sistema Daemon

### Documento DOCX estruturado

- ID: `regra-compendio-de-regras-daemon-trevas-docx-structured-source`
- Área: `regras_base`
- Fonte: `compendio-de-regras-daemon-trevas` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Fonte DOCX estruturada: Compendio de regras DAEMON Trevas.

### Documento DOCX estruturado

- ID: `regra-regras-de-boa-convivencia-docx-structured-source`
- Área: `regras_base`
- Fonte: `regras-de-boa-convivencia` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Fonte DOCX estruturada: Regras de boa convivência.

### Documento DOCX estruturado

- ID: `regra-tabela-e-regras-para-magos-docx-structured-source`
- Área: `regras_base`
- Fonte: `tabela-e-regras-para-magos` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Fonte DOCX estruturada: Tabela e Regras para magos.

### Experiencia

- ID: `regra-a-assassina-a-assassina-experience`
- Área: `regras_base`
- Fonte: `a-assassina` p. 5
- Flags: `too_short_possible_cut`
- Amostra: Recompensas de experiencia associadas a conclusao da aventura.

### Iniciativa

- ID: `regra-mago-sistema-daemon-mago-sistema-daemon-iniciativa-1`
- Área: `regras_base`
- Fonte: `mago-sistema-daemon` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Iniciativa DAEMON Hatalíbio Almeida Sistema Daemon

### Tormenta Rpg – Sistema Daemon – Versão de Thiago “mestre Kwan” Rodrigues (181-181)

- ID: `regra-daemon-tormenta-daemon-tormenta-tormenta-rpg-sistema-daemon-versao-de-thiago-mestre-kwan-rodrigues-1-19`
- Área: `regras_base`
- Fonte: `daemon-tormenta` p. 181
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Tormenta rpg – sistema daemon – versão de thiago “mestre kwan” rodrigues 181

### Cenários

- ID: `um-sussurro-nas-trevas--um-sussurro-nas-trevas-cenarios-35`
- Área: `aventuras`
- Fonte: `um-sussurro-nas-trevas` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Cenários Não esqueça que os anos 20 estão repletos de cenários que não estão relacionados com o gangsterismo e as melindrosas. Em Nova York, o Harlem tinha a melhor vida noturna do mundo conhecido para negros e brancos ricos, e circulava rumores sobre locais o

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

### 'HP{QLR

- ID: `dem-nio-o-pre-o-do-poder--dem-nio-o-pre-o-do-poder-hp-qlr-9`
- Área: `criaturas_npcs`
- Fonte: `dem-nio-o-pre-o-do-poder` p. -
- Flags: `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: 8 'HP{QLR 235(|2'232'(5 PARTE 1: CORPO Muito acontece nas sombras. Poucos vêem. O mundo é um lugar sombrio, apenas isso. Os poderosos controlam tudo. Tudo. Mas alguém observa. Alguém que vive nas sombras. O demônio. Ele sabe o que acontece, e ri... Ri porqu

### -Paris.

- ID: `anjossombras04--anjossombras04-paris-9`
- Área: `criaturas_npcs`
- Fonte: `anjossombras04` p. 9
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: -Paris. -Então vamos. Ângelus então se concentra e abre um portal. Yaba acha engraçado e mostra a Benael o enorme sorriso que se abriu no rosto de Igor. Aelus é o primeiro a entrar, seguido por Yaba, Benael, Igor, Mikael e Salvatore, Ângelus entra logo após se

### -kkkkkkkkkkkkkkkk.

- ID: `anjossombras04--anjossombras04-kkkkkkkkkkkkkkkk-6`
- Área: `criaturas_npcs`
- Fonte: `anjossombras04` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: -kkkkkkkkkkkkkkkk. -Tu ri né peste? Tu ri porque não era você que tinha que passar a noite todinha acordado ouvindo as besteiras que vocês falam dormindo. -rsrsrsrsrsrsrs. -Agora que a gente ta aqui me diz uma coisa. -Que é Biel? -Alguém sabe como a Lilith foi

### A AMÉRICA DO NORTE

- ID: `dem-nio-o-pre-o-do-poder--dem-nio-o-pre-o-do-poder-a-america-do-norte-34`
- Área: `criaturas_npcs`
- Fonte: `dem-nio-o-pre-o-do-poder` p. 34
- Flags: `ends_with_connector_possible_cut`
- Amostra: 33 A AMÉRICA DO NORTE Deus abençoe a América. — Citação do Hino Nacional dos EUA As grandes cidades da América do Norte, em particular no Estados Unidos, são mais do que metrópoles cheias de gente. Nos arranha-céus mais altos, agentes vampíricos manipulam a po

### A WYRM E A AMÉRICA LATINA

- ID: `dem-nio-o-pre-o-do-poder--dem-nio-o-pre-o-do-poder-a-wyrm-e-a-america-latina-35`
- Área: `criaturas_npcs`
- Fonte: `dem-nio-o-pre-o-do-poder` p. 35
- Flags: `ends_with_connector_possible_cut`
- Amostra: 34 A WYRM E A AMÉRICA LATINA A presença da Wyrm, ou Vermis Magnus, na América Latina é muito forte. A Pentex, uma empresa a serviço das forças da destruição, possui muitas subsidiárias no continente, e os mundos espirituais fervilham com espíritos Malditos. Mu

### A._njos

- ID: `arkanun--arkanun-a-njos-150`
- Área: `criaturas_npcs`
- Fonte: `arkanun` p. 150
- Flags: `ends_with_connector_possible_cut`
- Amostra: A._njos Paris foi considerada desde a sua fundação como um ponto extremamente importante para a Cidade de Prata, pela sua localização (no coração da Europa). Os dois primeiros Anjos enviados pelo Conselho à Paris foram Pierre de Chelles e Jean Ravy, no século

### ALGUNS DIALETOS ROMANIS

- ID: `ciganos--ciganos-alguns-dialetos-romanis-3`
- Área: `criaturas_npcs`
- Fonte: `ciganos` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: 3 ALGUNS DIALETOS ROMANIS A língua dos ciganos é conhecida como romani, bastante pró- xima dos idiomas indo-arianos. Tanto o sistema fonológico como a morfologia podem ter sua evolução facilmente reconstruída a partir do sânscrito. O sistema numeral também ref

### APÊNDICE: DRAGÕES EM TREVAS

- ID: `guia-dos-dragoes-1-biblioteca-elfica--guia-dos-dragoes-1-biblioteca-elfica-apendice-dragoes-em-trevas-46`
- Área: `criaturas_npcs`
- Fonte: `guia-dos-dragoes-1-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: APÊNDICE: DRAGÕES EM TREVAS Ao longo dos anos, principalmente durante a Idade Mé- dia, diversas organizações e movimentos idealistas persegui- ram magos e bruxos do mundo todo, provocando seu isola- mento e quase extinção. Todo o conhecimento sobre Magia parec

### ATIVAÇÃO DE ITENS MÁGICOS

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-ativacao-de-itens-magicos-121`
- Área: `criaturas_npcs`
- Fonte: `demonios-a-divina-comedia` p. 121
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: ATIVAÇÃO DE ITENS MÁGICOS Alguns itens mágicos (em especial aqueles criados pelos seres da Cidade de Prata) requerem Pontos de Fé para serem ativados ou utilizados. Somente pessoas com Fé podem utilizar tais artefatos. BÊNÇÃO O Inquisidor pode abençoar um grup

### Anjos, Demônios e Vampiros).

- ID: `spawn--spawn-anjos-demonios-e-vampiros-1`
- Área: `criaturas_npcs`
- Fonte: `spawn` p. 1
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: Criado por Todd McFarlane, Spawn tornou-se rapidamente o personagem de quadrinhos mais vendido nos Estados Unidos, e mais tarde também se tornaria um sucesso de vendas aqui no Brasil. A DRAGÃO BRASIL traz com exclusividade para vocês todo o background de SPAWN

### Aprimoramentos

- ID: `spiritum--spiritum-aprimoramentos-43`
- Área: `criaturas_npcs`
- Fonte: `spiritum` p. 43
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Aprimoramentos Aprimoramentos são detalhes incomuns, raros ou sobre- naturais que tornam o Personagem dos demais, além de conce- ber algumas vantagens dentro do Jogo. Estes pontos não devem ser simplesmente “gastos”, mas o Jogador precisa justificá-los com o M

### Aprimoramentos Básicos

- ID: `um-sussurro-nas-trevas--um-sussurro-nas-trevas-aprimoramentos-basicos-11`
- Área: `criaturas_npcs`
- Fonte: `um-sussurro-nas-trevas` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Aprimoramentos Básicos Aprimoramentos são detalhes incomuns, raros ou até mesmo sobrenaturais que tornam o Personagem diferente dos demais, além de conceder certas vantagens em jogo. Cada Personagem humano começa o jogo com 5 pontos de Aprimoramentos e o Jogad

### Arcádia

- ID: `arkanun--arkanun-arcadia-13`
- Área: `criaturas_npcs`
- Fonte: `arkanun` p. -
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: Arcádia O episódio Arcádia também acontece mais ou me­ nos nessa época. Existia uma parte da Grécia chamada Licania, governada por um soberano chamado Licaon, que possuía diversas esposas e cinqüenta filhos e filhas. As terras de Licaon estavam entre as mais p

### Ataques com Fogo

- ID: `daemon-anime-rpg--daemon-anime-rpg-ataques-com-fogo-95`
- Área: `criaturas_npcs`
- Fonte: `daemon-anime-rpg` p. 95
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: Ataques com Fogo O Monstro de Bolso pode realizar ataques baseados em fogo, como bafo de dragão, gar­ ras incandescentes, jatos de plasma e outros ataques. O Monstro pode realizar um ataque com fogo a cada 3 rodadas. O pontos: incapaz de atacar. 1 ponto: dano

### Barcelona

- ID: `inquisicao-biblioteca-elfica--inquisicao-biblioteca-elfica-barcelona-41`
- Área: `criaturas_npcs`
- Fonte: `inquisicao-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Barcelona , A cidade de Barcelona é· urna das mais antigas da Espanha e esconde muitos segJ:edos. Dizem que um per deroso Demónio chamado Aquel esconde-se naquela ci- dadee que todos os padres de Barcelona estão de algu- ma forma sob sua influência. . Os Templ

### C0RP0RÊ

- ID: `anjos-a-cidade-de-prata--anjos-a-cidade-de-prata-c0rp0re-29`
- Área: `criaturas_npcs`
- Fonte: `anjos-a-cidade-de-prata` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: C0RP0RÊ Os Corpore representam a maior parte dos anjos da Cidade de Prata. De acordo com o papa Urbano I, são as almas boas e caridosas que alcançaram os céus. Quando uma pessoa morre, sua alma parte para Spiritum e é recepcionada pelas grandes for- ças de Spi

### CAMPANHA

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-campanha-106`
- Área: `criaturas_npcs`
- Fonte: `demonios-a-divina-comedia` p. 106
- Flags: `ends_with_connector_possible_cut`
- Amostra: CAMPANHA Seu personagem foi o único sobrevivente de uma aventura? Dos outros quatro personagens, 2 foram destruídos pelos Templários, um ficou louco, e o ultimo acabou aprisionado em Arkanun para sempre. Em um RPG de horror, sobreviver a uma aventura muitas ve

### Capítulo 10

- ID: `tagmar-daemon--tagmar-daemon-capitulo-10-61`
- Área: `criaturas_npcs`
- Fonte: `tagmar-daemon` p. -
- Flags: `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: Capítulo 10: Magia Uma definição formal (e um pouco pomposa) de magia é: "A arte de se provocar mudanças de acordo com a vontade". Magia é uma coisa muito importante – senão a mais importante – dos mundos e campanhas de fantasia medieval. Em Tagmar Daemon, as

### Capítulo 2

- ID: `anjos-jyhad-faces-da-fe--anjos-jyhad-faces-da-fe-capitulo-2-9`
- Área: `criaturas_npcs`
- Fonte: `anjos-jyhad-faces-da-fe` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Capítulo 2 Seitas, Sociedades e Ordens Angelicais A H o s t e de Miguel As falanges do anjo Miguel sempre foram a principal divisão do exército celestial. São tropas de choque e de defesa ao mesmo tempo. Anjos treinados por pelo menos cem anos são selecionados

### Capítulo 3 - A cidade Torpe

- ID: `metropolis-2--metropolis-2-capitulo-3-a-cidade-torpe-25`
- Área: `criaturas_npcs`
- Fonte: `metropolis-2` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 25 Capítulo 3 - A cidade Torpe controle acaba os colocando em débito com os Cenobitas. Mesmo assim, eles ainda preferem permanecer em Metrópolis, devido ao lucro. Açougue das Finas Refeições O plano astral está repleto de seres com paladares exóticos e diverso

### Capítulo 3 - A cidade Torpe

- ID: `metropolis-2--metropolis-2-capitulo-3-a-cidade-torpe-35`
- Área: `criaturas_npcs`
- Fonte: `metropolis-2` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 35 Capítulo 3 - A cidade Torpe acompanhada pela dor do vidro e dos espinhos penetrando na pele. Ficar muito tempo parado piora a situação, pois ouve-se os xingamentos que são seguidos por chicotes dos Guardiões que surgem no local. A Dura Caminhada é um caminh

### Capítulo 4

- ID: `anjos-jyhad-faces-da-fe--anjos-jyhad-faces-da-fe-capitulo-4-28`
- Área: `criaturas_npcs`
- Fonte: `anjos-jyhad-faces-da-fe` p. 28
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Capítulo 4 Antagonistas As religiões possuem grandes pro- blemas com a fragmentação e as próprias divergências internas, que quase sempre acabam em brigas e disputas violentas. Para piorar a situação, ainda existem grupos que batalham para deturpar os va- lore

### Capítulo 7 – Perícias

- ID: `daemon-medieval--daemon-medieval-capitulo-7-pericias-36`
- Área: `criaturas_npcs`
- Fonte: `daemon-medieval` p. 36
- Flags: `ends_with_connector_possible_cut`
- Amostra: Capítulo 7 – Perícias 36 Filosofia: Apesar de não ser uma ciência no sentido estrito da palavra, a filosofia é o estudo do pensamento humano. O Personagem conhece os métodos científicos e é capaz de criticar um raciocínio com clareza e objetividade – por isso

### Capítulo Sete: Os Filhos de Deus

- ID: `domini-urbs-biblioteca-elfica--domini-urbs-biblioteca-elfica-capitulo-sete-os-filhos-de-deus-143`
- Área: `criaturas_npcs`
- Fonte: `domini-urbs-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 142 Capítulo Sete: Os Filhos de Deus Os anjos não conhecem Pai a não ser aquele a quem chamam de Deus, Senhor e Mestre. Suas vidas consistem em servir e conviver com a fé que devem propagar e o desespero que sentem ecoar dos mundos inferiores. Vivendo em uma c

### CaríTULO

- ID: `arkanun-1e-ultra-raro--arkanun-1e-ultra-raro-caritulo-78`
- Área: `criaturas_npcs`
- Fonte: `arkanun-1e-ultra-raro` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: CaríTULO OB DEIAS PARA AVENTURA Si vis pacem, para bellum (Se desejas a paz, prepara-te para a guerra) Em ARKANUN as possibilidades de conflitos são quase infi- nitas, Por ser um mundo onde diversas forças antagônicas estão reunidas, confrontos entre elas pass

### Chaneque

- ID: `imortal-a-centelha--imortal-a-centelha-chaneque-10`
- Área: `criaturas_npcs`
- Fonte: `imortal-a-centelha` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Chaneque espíritos da noite espíritos da noite espíritos da noite espíritos da noite Origem e História Os astecas contam lendas sobre certos protetores da natureza que viviam nas cachoeiras, com características muito semelhantes às dos Elfos europeus. Os Chane

### Ciências Proibidas*

- ID: `arkanun-1e-ultra-raro--arkanun-1e-ultra-raro-ciencias-proibidas-24`
- Área: `criaturas_npcs`
- Fonte: `arkanun-1e-ultra-raro` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Ciências Proibidas* Valor inicial: O A perícia sobre conhecimentos ocultos abrange uma diver- sidade de assuntos que devem ser escolhidos pelo jogador. Incluem conhecimentos sobre Arkanun, Infernun, Paradisia, Éden e Spiritun, bem como reconhecimento de posses

### Clfistót9ia

- ID: `hi-brazil-biblioteca-elfica--hi-brazil-biblioteca-elfica-clfistot9ia-80`
- Área: `criaturas_npcs`
- Fonte: `hi-brazil-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Clfistót9ia A Patagônia é wna região gelada e isolada do resto do con- tinente e que esconde muitos segredos. Os habitantes que vivem nas áreas mais afastadas do oeste são reclusos e não gostam de visitantes. Os argentos já tentaram invadir a Patagônia várias

### DEMÔNIOS (59-65)

- ID: `clube-de-caca-guia-do-jogador--clube-de-caca-guia-do-jogador-demonios-9-6`
- Área: `criaturas_npcs`
- Fonte: `clube-de-caca-guia-do-jogador` p. -
- Flags: `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: 59 Aranha), Garras (Unhas Longas, Garras). Fraquezas Comuns: Estaca, Fogo, Decapitação, Sol, Símbolos Religiosos. Raça de vampiros que remete até os tempos aztecas. Adoram Tlazolteotl, a deusa da lua. Os mais jovens são encontrados em favelas de grandes cidade

### Desentsu Senshi (1-10)

- ID: `desentsu--desentsu-desentsu-senshi-1-1`
- Área: `criaturas_npcs`
- Fonte: `desentsu` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Desentsu Senshi Desentsu Senshi - Guerreiros do Oriente Autor: Victor”Ramuel”Martins Desentsu Senshi Introdução A editora Daemon lançou o livro Anime RPG (na época que escrevi esse netbook ele acaba de ser lançado e por motivos pessoas não pude lança-lo,sendo

### Dragões: Reis Caídos

- ID: `dragoes-reis-caidos-sistema-daemon--dragoes-reis-caidos-sistema-daemon-dragoes-reis-caidos-16`
- Área: `criaturas_npcs`
- Fonte: `dragoes-reis-caidos-sistema-daemon` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Dragões: Reis Caídos enfrentou um poderoso Dragão de Esmeralda e, em vez de exterminá-lo, o converteu ao Cristianismo. Este evento foi simultâneo à dolorosa traição de Naki-ah à Cidade de Prata, quando o Dragão de Safira convertido assassinou quase todos os La

### E O MUNDO TEVE CORAGEM

- ID: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica--anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica-e-o-mundo-teve-coragem-11`
- Área: `criaturas_npcs`
- Fonte: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica` p. 11
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`, `starts_mid_sentence_possible_left_cut`, `unbalanced_parentheses`
- Amostra: E O MUNDO TEVE CORAGEM DE CHAMAR A MIM E MEINE HERRN DE ASSASSINOS, CRIMINOSOS! ui q Q Ú <x E a) S EN AARON — A =

### E nem querem.

- ID: `existe-uma-cidade-nos-distritos-cujo-unico-objetivo-e-a-satisfac-u00e3o--existe-uma-cidade-nos-distritos-cujo-unico-objetivo-e-a-satisfac-u00e3o-e-nem-querem-1`
- Área: `criaturas_npcs`
- Fonte: `existe-uma-cidade-nos-distritos-cujo-unico-objetivo-e-a-satisfac-u00e3o` p. 1
- Flags: `ends_with_connector_possible_cut`
- Amostra: Existe uma cidade nos distritos cujo único objetivo é a satisfação. É o ápice de tudo o que pode ser considerado felicidade para qualquer criatura do universo. E falar dessa generalidade não é uma mentira ou uma mera propaganda. Não é à toa que essa cidade não

### ESPÍRITOS

- ID: `dem-nio-o-pre-o-do-poder--dem-nio-o-pre-o-do-poder-espiritos-172`
- Área: `criaturas_npcs`
- Fonte: `dem-nio-o-pre-o-do-poder` p. 172
- Flags: `ends_with_connector_possible_cut`
- Amostra: 171 — Fé protege os homens dos Poderes Infernais. Homens de Fé são imunes à Violação. Além disso, resistem à Incorporação com maior facilidade (cada ponto de Fé conta como um sucesso automático para se resistir à possessão). Muitos outros poderes são inúteis c

### Experiência

- ID: `um-sussurro-nas-trevas--um-sussurro-nas-trevas-experiencia-32`
- Área: `criaturas_npcs`
- Fonte: `um-sussurro-nas-trevas` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Experiência Dos outros quatro Personagens da Campanha, dois foram destruídos pela Inquisição, um ficou louco e o último acabou aprisionado em Arkanun para sempre. Em um RPG de horror, sobreviver a uma Aventura muitas vezes já é um prêmio em si, mas para recomp

### FABULARE

- ID: `dem-nio-o-pre-o-do-poder--dem-nio-o-pre-o-do-poder-fabulare-12`
- Área: `criaturas_npcs`
- Fonte: `dem-nio-o-pre-o-do-poder` p. 12
- Flags: `ends_with_connector_possible_cut`
- Amostra: 11 FABULARE Fabulare é a língua falada no Inferno e no Éden. Tanto anjos como demônios conhecem o Fabulare e o falam fluentemente, como se fosse uma língua nativa. É totalmente instintivo para eles: ninguém sabe como demônios e anjos aprendem tal linguagem, to

### FORÇA DE VONTADE (112-117)

- ID: `trevas-campanha-epica--trevas-campanha-epica-forca-de-vontade-72-5`
- Área: `criaturas_npcs`
- Fonte: `trevas-campanha-epica` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: - 111 - Compulsivo, Perversão Sexual ou Sanguinário. Depois, deve fazer um teste de WILL vs. CON. Caso a vítima falhe, ela irá envelhecer 5 vezes mais rápido que o normal. Nível 7: Apodrecimento. A entidade pode lançar parte de sua própria essência numa vítima

### HayYyYeTH

- ID: `anjos-jyhad-guerra-santa-biblioteca-elfica--anjos-jyhad-guerra-santa-biblioteca-elfica-hayyyyeth-42`
- Área: `criaturas_npcs`
- Fonte: `anjos-jyhad-guerra-santa-biblioteca-elfica` p. 42
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: HayYyYeTH "Ouve, Senhor, e tem piedade de mim, Senhor; sê o meu atnéílio. " ALCUNHA: PiEDBSES A bondade está no coração de todos os Hayyoth. São as criaturas incapazes de cometer o mal e dispostas a sacri- ficarem tudo o que possuem para os atos de caridade pa

### Horror dos Túmulos

- ID: `guia-de-monstros-de-arton--guia-de-monstros-de-arton-horror-dos-tumulos-69`
- Área: `criaturas_npcs`
- Fonte: `guia-de-monstros-de-arton` p. 69
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Horror dos Túmulos “Se você pretende escapar, inplore ao grande Thyatis para nun- ca encontrar um desses demônios! — Magoor, sumo-sacerdote de Thyatis CON -, FR -, DEX -, AGI 10-12, INT 2-3, WILL 2-3, CARO, PER 12-18 HF Ataques [2], IP -, PVs 20-30 Gattas 35/3

### InquisiçãO + Anjos

- ID: `inquisicao-biblioteca-elfica--inquisicao-biblioteca-elfica-inquisicao-anjos-45`
- Área: `criaturas_npcs`
- Fonte: `inquisicao-biblioteca-elfica` p. 45
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`, `unbalanced_brackets`
- Amostra: InquisiçãO + Anjos Campanhas mistas podem incluir Inquisidores e seus Anjos Protetores, bem corno a política da Cidade de, Prata em relação ao al[!'tcJero. Nesse tipo de Campanha, podem ser acrescentados alguns santos, como São Ben- to, São Jorge e S3ão Patric

### Introdução

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-introducao-5`
- Área: `criaturas_npcs`
- Fonte: `demonios-a-divina-comedia` p. 5
- Flags: `ends_with_connector_possible_cut`
- Amostra: Introdução Embora tenha passado boa parte de minha vida estudando o ocultismo, o tema Demônios me fascinou desde a primeira vez que li “A Divina Comedia”. O texto original da Divina Comédia foi escrito no século XIII, mas de lá para cá, muitos novos pecados su

### Introdução

- ID: `metropolis-2--metropolis-2-introducao-3`
- Área: `criaturas_npcs`
- Fonte: `metropolis-2` p. 3
- Flags: `ends_with_connector_possible_cut`
- Amostra: Introdução Metrópolis surgiu em uma das primeiras matérias para Trevas da extinta revista de RPG Dragão Brasil. Atraiu o interesse do público como a mancha de corrupção, a válvula de escape dos deuses em pleno Céu. A ideia de Marcelo Del Debbio surgiu de diver

### LORDE SATANACHIA, SENHOR DA FÚRIA

- ID: `dem-nio-o-pre-o-do-poder--dem-nio-o-pre-o-do-poder-lorde-satanachia-senhor-da-furia-224`
- Área: `criaturas_npcs`
- Fonte: `dem-nio-o-pre-o-do-poder` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 223 LORDE SATANACHIA, SENHOR DA FÚRIA Satanachia, também chamado Verine, Gressil ou Verrier, é o Grande Lorde da fúria e, como todo Furioso, se deixa levar por suas emoções mais fortes. Satanachia sente prazer em ver caos e destruição, e seu Reino reflete isso

### Livro de Enoch

- ID: `guia-de-itens-magicos--guia-de-itens-magicos-livro-de-enoch-167`
- Área: `criaturas_npcs`
- Fonte: `guia-de-itens-magicos` p. 167
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Livro de Enoch Linguagem: grego (copias em latim e ingles). Tipo: manuscritos. Autor: atribuido ao profeta Enoch. Ano: seculo 1. Raridade: os manuscritos sao legendarios, mas muitas co- pias podem ser encontradas. Conteudo: Anjos, Demonios e pentagramas de pro

### Melhor que quado

- ID: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica--anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica-melhor-que-quado-32`
- Área: `criaturas_npcs`
- Fonte: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica` p. 32
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: Melhor que quado só mesmo RPG! _DRAGAO BRASIL é a maior, melhoré única — revista brasileira | ‘ especializada em a ; e card games, com. heróis, pls monstros, dicas, ca EA mundos inteiros para xocê explorar. Vá logo” conquistar a sua! ms ne O o

### Metrópolis

- ID: `spiritum--spiritum-metropolis-99`
- Área: `criaturas_npcs`
- Fonte: `spiritum` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Metrópolis A origem de Metrópolis está ligada à lenda da batalha celestial entre Bel Meridath e Leviatã. Após o terrível combate entre estes deuses, a Serpente Leviatã foi destruída no Plano Astral e materializou-se em Paradísia. Caindo dos céus, abriu com o i

### Ministros

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-ministros-96`
- Área: `criaturas_npcs`
- Fonte: `demonios-a-divina-comedia` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Ministros das Regiões Infernais: Segundo os demonologistas, estes ministros são: Adramelech (Grande Chanceler), Astaroth (Grande Tesoureiro), Nergal (Chefe da Polícia Secreta) e Baal (General Chefe dos Exércitos Infernais). Minos: Soberano mítico de Creta, fil

### NAONAO

- ID: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica--anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica-naonao-31`
- Área: `criaturas_npcs`
- Fonte: `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica` p. 31
- Flags: `does_not_end_like_complete_sentence`, `ends_with_connector_possible_cut`
- Amostra: NAONAO Es 7 SANDRINHO! | EU na ONE E ACHAR SUA NAONAONAO _ NAMORADA NAONAO DRUIDA! Enquanto Sdhilto e Niele tentam chegar até Galrasia, Lisandra retorna ao: continente a procura de Tork, o troglodita anão. “Juntos, eles partem em busca. do terceiro Rubi. - da

### NimBus

- ID: `anjos-a-cidade-de-prata--anjos-a-cidade-de-prata-nimbus-39`
- Área: `criaturas_npcs`
- Fonte: `anjos-a-cidade-de-prata` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: NimBus Os Nimbus são os políticos da Cidade de Prata. Se con- sideram os escolhidos de uma força superior, e por essa razão (ou por sabotagem dos Recíperes), são muito poucos. Os Nimbus compõem cerca de 5 a 10% do total dos anjos da Cidade de Prata, mas possue

### O Abismo

- ID: `spiritum--spiritum-o-abismo-105`
- Área: `criaturas_npcs`
- Fonte: `spiritum` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: O Abismo Considerada uma das regiões mais perigosas e desconhe- cidas da orbe terrestre, o Abismo é a terra dos demônios refugi- ados de Tenebras, temida até mesmo pelos mais poderosos de- mônios de Arkanun. A Origem Quando Tenebras foi definitivamente destruí

### O Reino dos Mortos

- ID: `spiritum--spiritum-o-reino-dos-mortos-13`
- Área: `criaturas_npcs`
- Fonte: `spiritum` p. 13
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: O Reino dos Mortos Esta é sua segunda lição sobre os Reinos Espirituais. Co- meçaremos a aula de hoje com uma breve explanação sobre o que vem a ser o conceito de forma-pensamento, sua aplicação e sua relação com o Plano Astral, Físico e Espiritual. Estas noçõ

### Os Pilares do Ocidente

- ID: `neter-khertet-a-cidade-dourada-de-ra-biblioteca-elfica--neter-khertet-a-cidade-dourada-de-ra-biblioteca-elfica-os-pilares-do-ocidente-57`
- Área: `criaturas_npcs`
- Fonte: `neter-khertet-a-cidade-dourada-de-ra-biblioteca-elfica` p. 57
- Flags: `ends_with_connector_possible_cut`
- Amostra: Os Pilares do Ocidente Caminhando para o oeste, Aah Iah da lugar há um súbito deserto de areias douradas que invade a cidade. Aquele que caminha através dele, nem ao menos sairá da Necrópole, mas atingirá os Pilares do Ocidente, erigidos por Osiris numa era pr

### Os q)emônios do qnferno

- ID: `arkanun--arkanun-os-q-emonios-do-qnferno-121`
- Área: `criaturas_npcs`
- Fonte: `arkanun` p. -
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: Os q)emônios do qnferno Ao contrário dos Magos de Arkanun, os Demônios que habitam os Nove Círculos do Inferno não estão inte­ ressados em auxiliar a humanidade e evitar uma catás­ trofe, muito pelo contrário. Exilados dos Céus, perdedores na Grande Batalha Có

### Outras Publicações

- ID: `guia-de-monstros-de-arton--guia-de-monstros-de-arton-outras-publicacoes-125`
- Área: `criaturas_npcs`
- Fonte: `guia-de-monstros-de-arton` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Outras Publicações Estes livros podem ser encontrados na www.lojaderpg.com.br Orevas (Módulo Básico) Infiltrados em nossa sociedade, Anjos e Demônios disputam palmo a palmo a vitória na Guerra entre o Céu go de xadrez celestial. Neste RPG, você está convidado

### PASSADO

- ID: `conan--conan-passado-4`
- Área: `criaturas_npcs`
- Fonte: `conan` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: 4 PASSADO Imagine o que aconteceu com seu Personagem desde o seu nascimento até a data do início da Campanha. Escreva a história primeiro, depois se preocupe com os detalhes numéricos. Núme- ros não são importantes, o importante é criar um Personagem coe- rent

### PODER DA MALDIÇÃO

- ID: `dem-nio-o-pre-o-do-poder--dem-nio-o-pre-o-do-poder-poder-da-maldicao-200`
- Área: `criaturas_npcs`
- Fonte: `dem-nio-o-pre-o-do-poder` p. -
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: 199 PODER DA MALDIÇÃO Os Poderes da Maldição são um caminho antigo e poderoso da Magia Negra. Com eles, o Infernalista é capaz de lançar maldições, atribuir propriedades infernais a objetos ou realizar feitiços poderosos. Criação de mortos-vivos, controle de p

### PRE MNA ARAMPN RREMNM +RAMPX

- ID: `vikings-biblioteca-elfica--vikings-biblioteca-elfica-pre-mna-arampn-rremnm-rampx-48`
- Área: `criaturas_npcs`
- Fonte: `vikings-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: PRE MNA ARAMPN RREMNM +RAMPX RA MI MS MID KIA ES XIV AI MID MIS UNIDAS so BRRMIMM AR AMB BRRMIMM ARAME FRAPIXA +RAMPX 48 Xi UMIVXIA DANIRIV DS MISS = BR&PIM ME ARAMBN BRRPMIXM RAMAN entender o que realmente ocorreu, porém Angrboda tornou-se uma mácula na histó
