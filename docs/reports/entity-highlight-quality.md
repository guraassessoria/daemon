# Auditoria semântica inicial dos destaques

Este relatório identifica trechos publicados que parecem cortados, colados, duplicados, incompletos ou contaminados por artefatos de extração.
Ele não substitui conferência com o PDF/texto oficial; serve para priorizar revisão profissional.

## Resumo

- Registros sinalizados: 1387

### Flags

- `aprimoramento_without_cost_marker`: 26
- `critical_ocr_gibberish`: 12
- `does_not_end_like_complete_sentence`: 984
- `encoding_or_ocr_artifact`: 45
- `ends_with_connector_possible_cut`: 103
- `front_matter_or_index_block`: 5
- `hyphenated_word_split`: 524
- `invalid_title_or_ocr_header`: 4
- `lowercase_sentence_after_section_possible_leak`: 313
- `many_cost_markers_possible_merged_aprimoramentos`: 9
- `page_number_inside_text`: 160
- `repeated_fragment_possible_duplication`: 29
- `starts_mid_sentence_possible_left_cut`: 8
- `symbol_noise_ocr`: 4
- `too_long_possible_merged_blocks`: 21
- `too_short_possible_cut`: 56
- `unbalanced_brackets`: 1
- `unbalanced_parentheses`: 81

### Por área

- `aprimoramentos`: 211
- `atributos_pericias`: 46
- `aventuras`: 12
- `cenarios_lore`: 1
- `classes`: 12
- `combate`: 50
- `criaturas_npcs`: 71
- `itens_equipamentos`: 31
- `kits`: 186
- `linhagens`: 70
- `magias`: 217
- `poderes`: 358
- `racas`: 47
- `regras_base`: 20
- `rituais`: 53
- `tabelas`: 2

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

### Atributos

- ID: `atributos--atributos-atributos-1`
- Área: `atributos_pericias`
- Fonte: `atributos` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Atributos Por Lobo

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

### Pagina inicial

- ID: `trevas-de-marte--trevas-de-marte-pagina-inicial-1`
- Área: `cenarios_lore`
- Fonte: `trevas-de-marte` p. 1
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: T

### Capítulo 8 – Armas e Equipamentos

- ID: `daemon-medieval--daemon-medieval-capitulo-8-armas-e-equipamentos-52`
- Área: `combate`
- Fonte: `daemon-medieval` p. 52
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Capítulo 8 – Armas e Equipamentos 52

### Capítulo 8 – Armas e Equipamentos

- ID: `daemon-medieval--daemon-medieval-capitulo-8-armas-e-equipamentos-54`
- Área: `combate`
- Fonte: `daemon-medieval` p. 54
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Capítulo 8 – Armas e Equipamentos 54

### Pagina inicial

- ID: `modulo-combate--modulo-combate-pagina-inicial-1`
- Área: `combate`
- Fonte: `modulo-combate` p. 1
- Flags: `too_short_possible_cut`
- Amostra: Pagina sem texto extraido relevante.

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

### Mortos Vivos

- ID: `mortos-vivos--mortos-vivos-mortos-vivos-2`
- Área: `criaturas_npcs`
- Fonte: `mortos-vivos` p. 2
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Mortos Vivos 2ª edição

### Pagina inicial

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-pagina-inicial-1`
- Área: `criaturas_npcs`
- Fonte: `demonios-a-divina-comedia` p. 1
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

### Sistema Daemon

- ID: `mago-sistema-daemon--mago-sistema-daemon-sistema-daemon-2`
- Área: `regras_base`
- Fonte: `mago-sistema-daemon` p. 2
- Flags: `does_not_end_like_complete_sentence`, `too_short_possible_cut`
- Amostra: Sistema Daemon 1ª edição

### Rituais

- ID: `alastores-a-justica-infernal--alastores-rituais`
- Área: `rituais`
- Fonte: `alastores-a-justica-infernal` p. -
- Flags: `too_short_possible_cut`
- Amostra: Rituais como Convocar Lukhavim, Sellas locum e Ipsa Nomina.

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

### ATRIBUTO BASE

- ID: `evolucao-alternativa--evolucao-alternativa-atributo-base-11`
- Área: `atributos_pericias`
- Fonte: `evolucao-alternativa` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Custo em Pontos de Treino de 1 Ponto de Atributo ATRIBUTO BASE 24 21 18 15 12 9 6 3 10 5 10 15 20 25 30 35 40 15 10 15 20 25 30 35 40 45 20 15 20 25 30 35 40 45 50 25 20 25 30 35 40 45 50 55 30 25 30 35 40 45 50 55 60 35 30 35 40 45 50 55 60 65 40 35 40 45 50 

### Atenção!

- ID: `atributos--atributos-atencao-2`
- Área: `atributos_pericias`
- Fonte: `atributos` p. 2
- Flags: `ends_with_connector_possible_cut`
- Amostra: Atenção! Esse net-book é gratuito, a venda do mesmo é proibida, pois ele foi feito para livre download. Tudo relatado aqui é ficcional, trate isto como objeto de entretenimento. Importante! Procurei me concentrar naquilo que auxilia mestres e jogadores para um

### Capítulo 7 – Perícias

- ID: `daemon-medieval--daemon-medieval-capitulo-7-pericias-36`
- Área: `atributos_pericias`
- Fonte: `daemon-medieval` p. 36
- Flags: `ends_with_connector_possible_cut`
- Amostra: Capítulo 7 – Perícias 36 Filosofia: Apesar de não ser uma ciência no sentido estrito da palavra, a filosofia é o estudo do pensamento humano. O Personagem conhece os métodos científicos e é capaz de criticar um raciocínio com clareza e objetividade – por isso 

### Capítulo 7 – Perícias

- ID: `daemon-medieval--daemon-medieval-capitulo-7-pericias-40`
- Área: `atributos_pericias`
- Fonte: `daemon-medieval` p. 40
- Flags: `ends_with_connector_possible_cut`
- Amostra: Capítulo 7 – Perícias 40 Este grupo de Perícias permite ao Personagem sair-se bem no mundo das finanças e evita que faça maus negócios – seja no momento de pechinchar um preço melhor quando compra uma mercadoria, seja para evitar que seu negócio vá à falência.

### Características Táuricas

- ID: `guia-dos-dragoes-1-biblioteca-elfica--guia-dos-dragoes-1-biblioteca-elfica-caracteristicas-tauricas-43`
- Área: `atributos_pericias`
- Fonte: `guia-dos-dragoes-1-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Características Táuricas Todos os tauros compartilham de algumas características em comum, que também são comparti0lhadas pelos centauros. Tauros recebem +2 de FR para qualquer tarefa envolvendo sua metade inferior do corpo, incluindo ataque com as patas. Taur

### Daemon Medieval

- ID: `daemon-medieval--daemon-medieval-daemon-medieval-37`
- Área: `atributos_pericias`
- Fonte: `daemon-medieval` p. 37
- Flags: `ends_with_connector_possible_cut`
- Amostra: Daemon Medieval 37 Um Teste de Conhecimento deve ser realizado toda vez que o Personagem deseja obter alguma informação sobre o conhecimento em questão. Geralmente o Teste será Normal, mas para lembrar-se de uma informação mais profunda e obscura o Mestre pode

### ELEMENTOS SECUNDÁRIOS

- ID: `gerador-de-criaturas--gerador-de-criaturas-elementos-secundarios-72`
- Área: `atributos_pericias`
- Fonte: `gerador-de-criaturas` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 72 Nível 3 – 1,5 pontos – o manto de sombras tem área igual ao atributo base x2 em metros, os alvos dentro dessa área recebem um redutor em sua percepção igual ao atributo base, e uma penalidade em seus testes igual ao atributo base x3. Nível 4 – 2 pontos – o 

### ESPORTES*

- ID: `guia-pericias--guia-pericias-esportes-11`
- Área: `atributos_pericias`
- Fonte: `guia-pericias` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: ESPORTES* Existem vários tipos de Esportes que podem ser selecionados pelo Personagem. A seguir existem alguns exemplos. Acrobacia (AGI): Dá ao Personagem a habilidade de equilibrar-se em pequenas superfícies, andar sobre cordas, fazer malabarismo e coisas do 

### FACILIDADE, LAMIA (279-288)

- ID: `trevas-campanha-epica--trevas-campanha-epica-facilidade-lamia-229-6`
- Área: `atributos_pericias`
- Fonte: `trevas-campanha-epica` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: - 273 - teste de CON Difícil. Caso tenha sucesso, o personagem não adquire a doença sobrenatural. Caso falhe, a criatura perderá 1 ponto de atributo físico por mês. Após o primeiro teste, o personagem pode ainda fazer testes de CON Difícil à cada mês subsequen

### Idade

- ID: `atributos--atributos-idade-13`
- Área: `atributos_pericias`
- Fonte: `atributos` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Idade Os atributos não permanecem os mesmos ao longo do tempo. Eles vem, ficam e vão. Todas as criaturas nascem com o mínimo possível para a sua espécie e, de acordo com seu metabolismo, vão ganhando mais atributos até atingirem a fase adulta. Note que essa re

### MATEMÁTICA DE JOGO

- ID: `kidous-arte-das-trevas--kidous-arte-das-trevas-matematica-de-jogo-21`
- Área: `atributos_pericias`
- Fonte: `kidous-arte-das-trevas` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 21 MATEMÁTICA DE JOGO Recitação e iniciativa Em termos de regras, a recitação invocadora de um kidou implica um redutor de 10 pontos na iniciativa do artífice, caso opte por pular a recitação da técnica, o artífice não terá redutor algum na iniciativa, porem f

### Passo 3: Atributos

- ID: `dbz-rpg--dbz-rpg-passo-3-atributos-7`
- Área: `atributos_pericias`
- Fonte: `dbz-rpg` p. 7
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Passo 3: Atributos Como estamos trabalhando com DBZ, os Personagens pos- suirão 150 pontos para distribuir em seus oito Atributos. Os Atributos devem ser distribuídos de acordo com a sua concepção do Personagem. Como você imagina que ele é? For- te como um tou

### QUINAMETZIN HUETLACAME

- ID: `gigantes-mitologicos--gigantes-mitologicos-quinametzin-huetlacame-19`
- Área: `atributos_pericias`
- Fonte: `gigantes-mitologicos` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: QUINAMETZIN HUETLACAME “Homens Grandes e Deformados” História Os Quinametzin são Gigantes que viviam na América central no período do Terceiro Sol, e vieram de Arkanun em grande número. Arrogantes, eram muito odiados pelos povos Nahuals(quase todos os povos da

### Valor Médio

- ID: `atributos--atributos-valor-medio-4`
- Área: `atributos_pericias`
- Fonte: `atributos` p. 4
- Flags: `ends_with_connector_possible_cut`
- Amostra: Valor Médio Devido às leis da probabilidade, ao rolar dois valores aleatórios como os dados e somá-los, alguns valores passam a ter mais chances de saírem que outros. Rolando um 3D, o valor 10 e 11 tem 12,15% de chances de sair cada, enquanto 3 e 18 possuem 0,

### arremessar

- ID: `poderes-de-fe-02--poderes-de-fe-02-arremessar-6`
- Área: `atributos_pericias`
- Fonte: `poderes-de-fe-02` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: arremessar uma arma que esteja empunhando a até 5 metros de distância e fazer ela retornar às suas mãos, ao gasto de 1 Ponto de Fé. Distâncias maiores podem ser alcançadas mediante o gasto de mais Pontos de Fé. Para acertar seu alvo, o personagem deve fazer um

### CAMPANHA

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-campanha-106`
- Área: `aventuras`
- Fonte: `demonios-a-divina-comedia` p. 106
- Flags: `ends_with_connector_possible_cut`
- Amostra: CAMPANHA Seu personagem foi o único sobrevivente de uma aventura? Dos outros quatro personagens, 2 foram destruídos pelos Templários, um ficou louco, e o ultimo acabou aprisionado em Arkanun para sempre. Em um RPG de horror, sobreviver a uma aventura muitas ve

### EVOLUÇÃO ALTERNATIVA

- ID: `evolucao-alternativa--evolucao-alternativa-evolucao-alternativa-3`
- Área: `aventuras`
- Fonte: `evolucao-alternativa` p. -
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: EVOLUÇÃO ALTERNATIVA Originalmente no sistema Daemon, o tipo de campanha é o fator que determina o potencial inicial de um personagem. Em campanhas épicas um personagem inicial equivale a um personagem de alto nível de uma campanha mais realista. Porém essa di

### PASSADO

- ID: `conan--conan-passado-4`
- Área: `aventuras`
- Fonte: `conan` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: 4 PASSADO Imagine o que aconteceu com seu Personagem desde o seu nascimento até a data do início da Campanha. Escreva a história primeiro, depois se preocupe com os detalhes numéricos. Núme- ros não são importantes, o importante é criar um Personagem coe- rent

### ATIVAÇÃO DE ITENS MÁGICOS

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-ativacao-de-itens-magicos-121`
- Área: `combate`
- Fonte: `demonios-a-divina-comedia` p. 121
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: ATIVAÇÃO DE ITENS MÁGICOS Alguns itens mágicos (em especial aqueles criados pelos seres da Cidade de Prata) requerem Pontos de Fé para serem ativados ou utilizados. Somente pessoas com Fé podem utilizar tais artefatos. BÊNÇÃO O Inquisidor pode abençoar um grup

### Capítulo 03- Cabalas dos Arcanis

- ID: `arcanis--arcanis-capitulo-03-cabalas-dos-arcanis-8`
- Área: `combate`
- Fonte: `arcanis` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 8 Kansarianos que usem a lágrima do sangue do ódio, recebem sendo Arcanis um bônus de +15% em todos os testes seguintes seja ataque/defesa/evasiva além de uma ação extra convencional (pois se locomove mais rápido que os outros), além de um bônus temporário de 

### Capítulo 10

- ID: `daemon-medieval--daemon-medieval-capitulo-10-60`
- Área: `combate`
- Fonte: `daemon-medieval` p. 60
- Flags: `ends_with_connector_possible_cut`
- Amostra: Capítulo 10 – Regras de testes e combate 60 Capítulo 10 Regras de Testes e Combate or mais cautelosos que os Personagens sejam, por maiores os cuidados que eles tenham, em algum momento da Aventura eles serão obrigados a enfrentar algo ou alguém. Para isso, é 

### Capítulo 2

- ID: `anjos-jyhad-faces-da-fe--anjos-jyhad-faces-da-fe-capitulo-2-9`
- Área: `combate`
- Fonte: `anjos-jyhad-faces-da-fe` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Capítulo 2 Seitas, Sociedades e Ordens Angelicais A H o s t e de Miguel As falanges do anjo Miguel sempre foram a principal divisão do exército celestial. São tropas de choque e de defesa ao mesmo tempo. Anjos treinados por pelo menos cem anos são selecionados

### Daemon Medieval

- ID: `daemon-medieval--daemon-medieval-daemon-medieval-69`
- Área: `combate`
- Fonte: `daemon-medieval` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Daemon Medieval 69 Quedas Existem duas maneiras de um Personagem sofrer uma queda: intencional ou acidental. Em casos de queda acidental, o Personagem não espera sofrer a queda e seus músculos não estavam preparados para absorver o impacto. O dano é 1d6 a cada

### Daemon Medieval

- ID: `daemon-medieval--daemon-medieval-daemon-medieval-29`
- Área: `combate`
- Fonte: `daemon-medieval` p. 29
- Flags: `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: Daemon Medieval 29 subordinados relutem quando não concordarem com a ordem (como atacar um exército visivelmente superior ou cometer qualquer ato que pareça suicídio). Um personagem com Voz de Comando faz um Teste de Liderança (sem precisar disputar contra a W

### GANESHAMAN

- ID: `avatar-volume-1--avatar-volume-1-ganeshaman-26`
- Área: `combate`
- Fonte: `avatar-volume-1` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 26 GANESHAMAN Arte: Nitro GANESHAMAN CON 16(80), FR 20(100), DEX 13(30), AGI 11 (30), INT 10, WILL 25, CAR 10 (8), PER 14 Guerreiro do 12° Nível #ataques [3], IP 1, PVs 18 (90) + 30 Ataques: Briga 80/80, dano 1d6+3 na forma humana e 3d6+45 na forma de Avatar. 

### GLAAKS (SOLDADO MÉDIO)

- ID: `avatars-vol-2--avatars-vol-2-glaaks-soldado-medio-20`
- Área: `combate`
- Fonte: `avatars-vol-2` p. -
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: 20 GLAAKS (SOLDADO MÉDIO) CON 35 (8), FR 35 (10), DEX 20 (16), AGI 25 (14), INT 16, WILL 14, CAR 9, PER 30 (18) Guerreiro do 7° Nível #ataques [1], IP 10 PVs 50 (9) * O que estiver entre parêntesis refere-se ao Glaak fora do mecha que ele usa. GLAAKS (CAPITÃO)

### HECATOMBE

- ID: `avatars-vol-2--avatars-vol-2-hecatombe-15`
- Área: `combate`
- Fonte: `avatars-vol-2` p. -
- Flags: `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: 15 HECATOMBE Arte: Nitro HECATOMBE CON 11(90), FR 12 (95), DEX 10(20), AGI 11 (25), INT 10, WILL 20, CAR 8, PER 10 Guerreiro do 8° Nível #ataques [2], IP 40 PVs 185 + 30 PHs. Ataques: Briga: 75/75, dano 3d6 +38 Explosão Atômica: 15d6 (Hecatombe pode explodir o

### Introdução

- ID: `ceifadores--ceifadores-introducao-3`
- Área: `combate`
- Fonte: `ceifadores` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Introdução Em Arton, existem diversas ordens religiosas conhecidas. A maioria delas é fundada em nome de deuses com boa índole e com ideais louváveis (justiça, amor, vida, nobreza etc). O mais cultuado destes é Khalmyr, o deus da justiça e da maioria dos palad

### Investigador

- ID: `anjos-jyhad-faces-da-fe--anjos-jyhad-faces-da-fe-investigador-39`
- Área: `combate`
- Fonte: `anjos-jyhad-faces-da-fe` p. 39
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Investigador CON 14, FR 12, DEX 16, AGI 13, INT 20, WILL 22, CAR 13, PER 26 Lança 40 dano 1d6 Espada 40/60 dano 1d10 # Ataques [1], IP 2, PVs 20 Perícias: Barganha 40%, Briga 30%, Esquiva 50%, Furtividade 40%, Impressionar 40%, Inter- rogatório 50%, Intimidaçã

### JIRAYA O INCRIVEL NINJA

- ID: `jiraya--jiraya-jiraya-o-incrivel-ninja-1`
- Área: `combate`
- Fonte: `jiraya` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: JIRAYA O INCRIVEL NINJA 1 SUCESSOR DOS TOGAKURI JIRAYA Capitulo ± Introdução Na era do Japão Medieval uma fabulosa cápsula miraculosa de nome Pako foi enviada a Terra por uma civilização alienígena muito mais avançada tecnológica e cientificamente Junto com el

### MANOBRAS DE COMBATE

- ID: `manobras-de-combate--manobras-de-combate-manobras-de-combate-1`
- Área: `combate`
- Fonte: `manobras-de-combate` p. 1
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: MANOBRAS DE COMBATE Esta categoria de perícia é um caso excepcional. São apresentadas aqui algumas manobras de combate. Elas não são utilizadas como perícias, na medida em que NÃO existe um teste de manobras de combate. O Personagem simplesmente sabe realizá-l

### Personalidades: Vandana, Mahatma Ghandi,

- ID: `trevas-do-oriente-28-palacios--trevas-do-oriente-28-palacios-personalidades-vandana-mahatma-ghandi-16`
- Área: `combate`
- Fonte: `trevas-do-oriente-28-palacios` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Personalidades: Vandana, Mahatma Ghandi, Dr. Rajenda Prasad, Narasimha Rao. Background: Uma Sociedade Secreta relativamente recente, a ordem das Grandes Espadas é formada pelos principais pensadores e sábios orientais, todos eles desejosos por uma Terra pacífi

### Primeiro Círculo

- ID: `caminhos2--caminhos2-primeiro-circulo-13`
- Área: `combate`
- Fonte: `caminhos2` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Primeiro Círculo Entender-Os olhos do mago não se incomodam com a lama.O mago pode andar na lama sem sujar os pés ou deixar pegadas.Pode sentir propriedades da lama apenas tocando-a. Criar-Enche um pequeno balde de lama,que pode ter uma temperatura baixa ou al

### Primeiro Círculo

- ID: `os-caminhos-secundarios--os-caminhos-secundarios-primeiro-circulo-13`
- Área: `combate`
- Fonte: `os-caminhos-secundarios` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Primeiro Círculo Entender-Os olhos do mago não se incomodam com a lama.O mago pode andar na lama sem sujar os pés ou deixar pegadas.Pode sentir propriedades da lama apenas tocando-a. Criar-Enche um pequeno balde de lama,que pode ter uma temperatura baixa ou al

### REGRAS : DANO

- ID: `arte-da-guerra--arte-da-guerra-regras-dano-17`
- Área: `combate`
- Fonte: `arte-da-guerra` p. 17
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`, `unbalanced_parentheses`
- Amostra: REGRAS : DANO Dano Simples Em caso de acerto critico o personagem obriga o oponente a fazer um teste de constituição fácil, se passa ele leva o dano correspondente a acerto critico, mas em caso de falha além do dano critico o oponente é penalizado dependendo d

### REGRAS E TESTES

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-regras-e-testes-110`
- Área: `combate`
- Fonte: `demonios-a-divina-comedia` p. 110
- Flags: `ends_with_connector_possible_cut`
- Amostra: REGRAS E TESTES Por mais cautelosos que os Personagens sejam, por maiores os cuidados que eles tenham, em algum momento da Aventura eles serão obrigados a enfrentar algo ou alguém. Para isso, e necessário definir com bastante cuidado as regras para Combates e 

### Super Ataques Especiais

- ID: `modulo-combate--modulo-combate-super-ataques-especiais-16`
- Área: `combate`
- Fonte: `modulo-combate` p. 16
- Flags: `ends_with_connector_possible_cut`
- Amostra: Super Ataques Especiais Como regra opcional, você pode customizar os Ataques Especiais também, conferindo efeitos extras. Um Ataque Especial comum, funciona da seguinte maneira: você gasta 2 Pontos de Magia e seu Personagem recebe +2d de bônus para o dano do s

### -kkkkkkkkkkkkkkkk.

- ID: `anjossombras04--anjossombras04-kkkkkkkkkkkkkkkk-6`
- Área: `criaturas_npcs`
- Fonte: `anjossombras04` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: -kkkkkkkkkkkkkkkk. -Tu ri né peste? Tu ri porque não era você que tinha que passar a noite todinha acordado ouvindo as besteiras que vocês falam dormindo. -rsrsrsrsrsrsrs. -Agora que a gente ta aqui me diz uma coisa. -Que é Biel? -Alguém sabe como a Lilith foi

### ALGUNS DIALETOS ROMANIS

- ID: `ciganos--ciganos-alguns-dialetos-romanis-3`
- Área: `criaturas_npcs`
- Fonte: `ciganos` p. -
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: 3 ALGUNS DIALETOS ROMANIS A língua dos ciganos é conhecida como romani, bastante pró- xima dos idiomas indo-arianos. Tanto o sistema fonológico como a morfologia podem ter sua evolução facilmente reconstruída a partir do sânscrito. O sistema numeral também ref

### ATIVAÇÃO DE CARACTERÍSTICAS

- ID: `gerador-de-criaturas--gerador-de-criaturas-ativacao-de-caracteristicas-22`
- Área: `criaturas_npcs`
- Fonte: `gerador-de-criaturas` p. -
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: 22 ATIVAÇÃO DE CARACTERÍSTICAS Algumas das características apresentadas nesse netbook, não tem seus efeitos ativos durante todo o tempo, sendo necessário que elas sejam ativadas para que a criatura possa utilizá-las. Essa ativação é feita inicialmente através 

### Agilidade (AGI)

- ID: `guerreiros-orientais--guerreiros-orientais-agilidade-agi-29`
- Área: `criaturas_npcs`
- Fonte: `guerreiros-orientais` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Agilidade (AGI) Atributos são números que transportam para o jogo as características de um personagem. Esses números dizem como o personagem é, se comparado a outros personagens e criaturas. A contrário da Destreza, a Agilidade é válida para o corpo todo. Com 

### CAPÍTULO 3: DRAGÕES CROMÁTICOS

- ID: `guia-dos-dragoes-1-biblioteca-elfica--guia-dos-dragoes-1-biblioteca-elfica-capitulo-3-dragoes-cromaticos-15`
- Área: `criaturas_npcs`
- Fonte: `guia-dos-dragoes-1-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: CAPÍTULO 3: DRAGÕES CROMÁTICOS Todos os dragões estão divididos em diferentes classificações. Os dragões cromáticos são os mais numerosos de todos, e dividem-se em 5 espécies principais: vermelho, verde, azul, negro e branco. Em geral, todos os dragões cromáti

### CON[6D+26],FR[6D+30],DEX[0],AGI[3],INT[2],WILL[4],PER[1D+1],CAR[0]. (11-20)

- ID: `ark-a-nun-arquivos-de-bel-kalaa--ark-a-nun-arquivos-de-bel-kalaa-con-6d-26-fr-6d-30-dex-0-agi-3-int-2-will-4-per-1d-1-car-0-11-1`
- Área: `criaturas_npcs`
- Fonte: `ark-a-nun-arquivos-de-bel-kalaa` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 11 dentes e sim,um bico córneo, usado para triturar as duras raízes das quais alimenta-se.Colocam em média de 6 a 9 ovos de 1,50m de comprimento,enterrados em covas profundas.A postura ocorre nas épocas em que o sol brilha mais intensamente nos céus de Ark-a-n

### CRIAÇÃO DE PERSONAGEM

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-criacao-de-personagem-36`
- Área: `criaturas_npcs`
- Fonte: `demonios-a-divina-comedia` p. -
- Flags: `encoding_or_ocr_artifact`, `ends_with_connector_possible_cut`
- Amostra: CRIAÇÃO DE PERSONAGEM Em DEMONIOS, a criação de um personagem e algo bastante simples de se fazer. Normalmente existem muitas coisas a se decidir, que serão vitais para a sobrevivência do personagem no futuro. Existem também fatores relacionados com o backgrou

### Capítulo 4

- ID: `anjos-jyhad-faces-da-fe--anjos-jyhad-faces-da-fe-capitulo-4-28`
- Área: `criaturas_npcs`
- Fonte: `anjos-jyhad-faces-da-fe` p. 28
- Flags: `ends_with_connector_possible_cut`, `hyphenated_word_split`
- Amostra: Capítulo 4 Antagonistas As religiões possuem grandes pro- blemas com a fragmentação e as próprias divergências internas, que quase sempre acabam em brigas e disputas violentas. Para piorar a situação, ainda existem grupos que batalham para deturpar os va- lore

### Capítulo Sete: Os Filhos de Deus

- ID: `domini-urbs-biblioteca-elfica--domini-urbs-biblioteca-elfica-capitulo-sete-os-filhos-de-deus-143`
- Área: `criaturas_npcs`
- Fonte: `domini-urbs-biblioteca-elfica` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: 142 Capítulo Sete: Os Filhos de Deus Os anjos não conhecem Pai a não ser aquele a quem chamam de Deus, Senhor e Mestre. Suas vidas consistem em servir e conviver com a fé que devem propagar e o desespero que sentem ecoar dos mundos inferiores. Vivendo em uma c

### Desentsu Senshi (1-10)

- ID: `desentsu--desentsu-desentsu-senshi-1-1`
- Área: `criaturas_npcs`
- Fonte: `desentsu` p. -
- Flags: `ends_with_connector_possible_cut`
- Amostra: Desentsu Senshi Desentsu Senshi - Guerreiros do Oriente Autor: Victor”Ramuel”Martins Desentsu Senshi Introdução A editora Daemon lançou o livro Anime RPG (na época que escrevi esse netbook ele acaba de ser lançado e por motivos pessoas não pude lança-lo,sendo 

### E md

- ID: `universo-daemon-01--universo-daemon-01-e-md-5`
- Área: `criaturas_npcs`
- Fonte: `universo-daemon-01` p. -
- Flags: `ends_with_connector_possible_cut`, `starts_mid_sentence_possible_left_cut`
- Amostra: E md Ade ay od ae og edi as in e E, nm pan rat > tm, x iB de = Va =" uu ve uu a E yy "iad P P k A \ O que eu faço quando os jogadores não estão afim de "encarnarem" nos seus personagens de Trevas/Arkanun, e, mesmo sabendo que só com um piscar de olhos, aquele 

### Introdução

- ID: `demonios-a-divina-comedia--demonios-a-divina-comedia-introducao-5`
- Área: `criaturas_npcs`
- Fonte: `demonios-a-divina-comedia` p. 5
- Flags: `ends_with_connector_possible_cut`
- Amostra: Introdução Embora tenha passado boa parte de minha vida estudando o ocultismo, o tema Demônios me fascinou desde a primeira vez que li “A Divina Comedia”. O texto original da Divina Comédia foi escrito no século XIII, mas de lá para cá, muitos novos pecados su

### Ismails

- ID: `ismails-anjos-islamicos--ismails-anjos-islamicos-ismails-1`
- Área: `criaturas_npcs`
- Fonte: `ismails-anjos-islamicos` p. 1
- Flags: `ends_with_connector_possible_cut`
- Amostra: Ismails Os anjos Islâmicos. Durante os últimos tempos, Al-Dyniha permaneceu em Ark-a-nun como o Venerável Mestre da Ordem do Mármore depois que Magnus Petraak decidiu se estabelecer na Terra definitivamente. A sua jurisdição perdurou até 209 AC (data mundana),
