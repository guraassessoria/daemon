# Cleanup Sources Page Audit

Page-by-page audit for sources explicitly marked as usable, plus good-source items demoted during the final page audit.

## Summary

- Usable/verification sources audited: 89
- Pages checked: 6425
- Sources ok after page audit: 10
- Easy sources: 56
- Medium sources: 5
- Hard sources: 18
- Ok pages: 4433
- Easy pages: 1785
- Medium pages: 167
- Hard pages: 40

## Difficulty Rules

- Easy: page-number/covers, note-only pages, repeated RPG stat labels, simple table/stat-block normalization, or long DOCX lines that remain coherent.
- Medium: localized encoding/control noise, layout blobs, dense table text, or pages that need manual spot correction but still preserve content.
- Hard: heavy OCR/symbol noise, low language signal, many control characters, or enough affected pages to require source comparison/re-extraction.

## Hard

### `trevas-3-0`

- Title: Trevas 3.0
- Pages: 230
- Affected pages: 219
- Hard pages: 9, 39, 55, 105, 163, 165, 166, 167, 177, 182, 187, 190, 209
- Medium pages: 90, 122, 161, 175, 179, 220, 223
- Easy pages: 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, ... (+149)
- Suggested actions: compare with source PDF/OCR or re-extract affected pages; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: empty_page - 
  - p. 3 [easy]: empty_page - 
  - p. 4 [easy]: empty_page - 
  - p. 5 [easy]: repeated_terms_or_stat_block - ~VA8
  - p. 8 [easy]: repeated_terms_or_stat_block - ~~~iiii:i~~~

### `dem-nio-o-pre-o-do-poder`

- Title: Dem_nio_-_O_Pre_o_do_Poder
- Pages: 234
- Affected pages: 148
- Hard pages: 3, 4, 5, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 234
- Medium pages: 1, 10, 24, 33, 161, 220
- Easy pages: 6, 7, 11, 12, 13, 15, 16, 18, 20, 21, 22, 26, 27, 28, 29, 31, 34, 37, 38, 40, 43, 44, 47, 48, 50, 51, 61, 63, 70, 71, 73, 76, 77, 80, 82, 83, 84, 85, 86, 88, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, ... (+78)
- Suggested actions: compare with source PDF/OCR or re-extract affected pages; run targeted encoding/control-character cleanup; treat repeated mechanical/stat labels as structured data

  - p. 1 [medium]: encoding_or_control_noise - 235(|2'232'(5
  - p. 3 [hard]: heavy_symbol_or_ocr_noise - TXHHXVRX6RXXPGHP{QLR0LQKDUDoDpWHPLGDHPOHQGDVH
  - p. 4 [hard]: heavy_symbol_or_ocr_noise - 3RU LVVR HVWRX DTXL YRFr TXLV UHVSRVWDV HX GHL H DJRUD
  - p. 5 [hard]: heavy_symbol_or_ocr_noise - (VSHURTXHWHQKDVRUWHVHWLYHUVHUiFRPRHXVHQmREHPR
  - p. 6 [easy]: repeated_terms_or_stat_block - $SUHVHQWDomR
  - p. 7 [easy]: repeated_terms_or_stat_block - inocente.

### `marvel`

- Title: marvel
- Pages: 158
- Affected pages: 87
- Hard pages: -
- Medium pages: 41, 43, 45, 47, 48, 49, 50, 51, 52
- Easy pages: 11, 14, 20, 23, 27, 30, 32, 33, 53, 56, 57, 62, 63, 64, 65, 66, 71, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 107, 108, 110, 111, ... (+28)
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data

  - p. 11 [easy]: repeated_terms_or_stat_block - uma vingança.
  - p. 14 [easy]: repeated_terms_or_stat_block - de tudo).
  - p. 20 [easy]: repeated_terms_or_stat_block - Cibernéticos
  - p. 23 [easy]: repeated_terms_or_stat_block - Poderes Psiônicos
  - p. 27 [easy]: repeated_terms_or_stat_block - tonam Difíceis.
  - p. 30 [easy]: repeated_terms_or_stat_block - Mentiroso Compulsivo

### `supers`

- Title: Supers
- Pages: 107
- Affected pages: 84
- Hard pages: 7, 10, 44, 50, 65, 76, 78, 80, 84, 101
- Medium pages: 6, 16, 19, 48, 49, 55, 60, 69, 77, 87, 88
- Easy pages: 1, 2, 3, 4, 5, 9, 11, 12, 14, 15, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 34, 35, 36, 38, 39, 40, 42, 43, 45, 46, 52, 54, 56, 58, 59, 62, 63, 66, 67, 68, 70, 75, 79, 82, 83, 85, 86, 89, ... (+13)
- Suggested actions: compare with source PDF/OCR or re-extract affected pages; normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: empty_page - 
  - p. 3 [easy]: tiny_page - j ...... _ ... ',oo
  - p. 4 [easy]: empty_page - 
  - p. 5 [easy]: empty_page - 
  - p. 6 [medium]: symbol_noise - ~

### `kits-orientais`

- Title: Kits Orientais
- Pages: 123
- Affected pages: 67
- Hard pages: -
- Medium pages: 5, 7, 16, 28, 29, 33, 34, 35, 37, 42, 43, 44, 45, 47, 49, 59, 60, 74, 86, 88, 90, 93, 94, 97, 98, 99, 100, 101, 102, 103, 104, 107, 110, 111, 112, 113, 114, 118, 119, 120, 121
- Easy pages: 19, 22, 25, 27, 30, 36, 40, 46, 50, 52, 53, 54, 55, 56, 58, 61, 64, 65, 70, 75, 76, 78, 89, 92, 95, 96
- Suggested actions: split long DOCX/layout lines into entries; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 5 [medium]: layout_blob_line - Os ninjas eram os guerreiros das sombras, mercenários pagos para fazerem os mais variados tipos de serviços furtivos, entre eles: sabotagem, assassinatos e especialmente o de espionagem. Eles não se importavam em utilizar-se de métodos covardes para alcançar s
  - p. 7 [medium]: layout_blob_line - Os artistas marciais lutam e aperfeiçoam seu corpo através de movimentos cuidadosamente elaborados, que exigem estudo, treino e disciplina. Magos conjuram magias através de movimentos cuidadosamente elaborados, que exigem estudo, treino e disciplina. No passad
  - p. 16 [medium]: layout_blob_line - Defesas Multiplas Assim como Ataques Múltiplos, o personagem está apto a controlar uma conjunto de ações menores, mas que não chegam a constituírem ações extras. Neste caso, ele torna-se capaz de aparar, proteger-se ou esquivar-se de uma seqüência de golpes rá
  - p. 19 [easy]: repeated_terms_or_stat_block - Treinamento Intenso
  - p. 22 [easy]: repeated_terms_or_stat_block - Exemplos:
  - p. 25 [easy]: repeated_terms_or_stat_block - Shishio Ryu

### `battlemage`

- Title: BattleMage
- Pages: 124
- Affected pages: 47
- Hard pages: -
- Medium pages: 37, 77, 84, 87, 97, 101, 103, 115, 121
- Easy pages: 2, 13, 17, 18, 20, 21, 22, 23, 24, 25, 27, 32, 33, 39, 41, 44, 47, 48, 51, 65, 69, 70, 71, 83, 85, 86, 89, 90, 92, 94, 95, 102, 105, 108, 116, 118, 122, 123
- Suggested actions: split long DOCX/layout lines into entries; treat repeated mechanical/stat labels as structured data

  - p. 2 [easy]: repeated_terms_or_stat_block - Ele rolou no chão, e a monstruosidade Eldrazi recolheu seus tentáculos volta para mais um ataque.Lá estava.Um momento.E nesse momento, Gideon já estava de pé.
  - p. 13 [easy]: repeated_terms_or_stat_block - Eu vou encontrá-la.”E no momento seguinte as lâminas do sural de Gideon voaram, agarrando a lança de Jori En que havia permanecido enterrada no lugar.
  - p. 17 [easy]: repeated_terms_or_stat_block - Ele suspirou.
  - p. 18 [easy]: repeated_terms_or_stat_block - “Eu ganhei.
  - p. 20 [easy]: repeated_terms_or_stat_block - clientes.
  - p. 21 [easy]: repeated_terms_or_stat_block - “Eu não achava que você faria isso por mim.”“Eu não fiz isso para você”, disse Jace.

### `corondor`

- Title: Corondor
- Pages: 77
- Affected pages: 41
- Hard pages: -
- Medium pages: 1, 2, 8, 14, 15, 16, 18, 32, 33, 36, 37, 38, 39, 40, 41, 43, 44, 48, 53, 54, 56, 67, 71, 76, 77
- Easy pages: 7, 23, 27, 28, 30, 31, 45, 49, 58, 62, 63, 64, 65, 66, 72, 73
- Suggested actions: split long DOCX/layout lines into entries; treat repeated mechanical/stat labels as structured data

  - p. 1 [medium]: layout_blob_line - ERA DOS DRAGÕES ANCESTRAISOs eventos a seguir aconteceram em um período muito antigo, perdido na história e muito além das datações conehcidas. ~ -20.000 AR - Os mais antigos e poderosos Dragões que governaram Dominária por séculos foram envolvidos na Guerra d
  - p. 2 [medium]: layout_blob_line - Madara por milênios.Data desconhecida - É criado o plano artifical de Phyrexia por um planinauta em forma de dragão, que posteriormente falece e o plano fica abandonado e completamente perdido nas Eternidades Cegas.Data desconhecida - Nascimento da planinauta 
  - p. 7 [easy]: repeated_terms_or_stat_block - Kirtar morre.
  - p. 8 [medium]: layout_blob_line - Corondor é uma grande ilha ao norte de Jamuraa, banhada pelo Mar Golthonor. Muitas histórias prerevisionist ocorreu em Corondor. Ele foi o cenário do enredo Guerra Planeswalker, que é contada nas histórias em quadrinhos (O Mago das Sombras) e do estilo arcade 
  - p. 14 [medium]: layout_blob_line - As aves no Magic são tipicamente caracterizadas por possuírem penas, ossos ocos e as asas. Elas normalmente são capazes de voar, podem ser de tamanhos grandes e bastante inteligentes, além de existirem diversos tipos antropomórficos e se subdividirem em difere
  - p. 15 [medium]: layout_blob_line - Alguns sábios discutem acerca dos avianos com aspecto de águia geralmente terem pré-disposição para guerrear e lidar com magias, enquanto aqueles com aparência de corujas pareçam menos militares e mais especializados em trabalhos de assistência e pesquisa. Qua

### `samurai-shodown`

- Title: Samurai Shodown
- Pages: 77
- Affected pages: 21
- Hard pages: -
- Medium pages: 2, 9, 10, 14, 17, 21, 23, 26, 27, 31, 36, 39, 43, 46, 52, 53, 58, 62
- Easy pages: 50, 68, 69
- Suggested actions: split long DOCX/layout lines into entries; treat repeated mechanical/stat labels as structured data

  - p. 2 [medium]: layout_blob_line - Meses depois, outro "demônio" aparece no Japão. Contudo, ele não tinha relação nem com Amakusa nem com Ambrosia. Ele era um homem chamado Zankuro Minazuki, um poderoso guerreiro que tinha obtido a reputação de "demônio" por ter assassinado pessoas a sangue fri
  - p. 9 [medium]: layout_blob_line - Os ninjas eram os guerreiros das sombras, mercenários pagos para fazerem os mais variados tipos de serviços furtivos, entre eles: sabotagem, assassinatos e especialmente o de espionagem. Eles não se importavam em utilizar-se de métodos covardes para alcançar s
  - p. 10 [medium]: layout_blob_line - Os artistas marciais lutam e aperfeiçoam seu corpo através de movimentos cuidadosamente elaborados, que exigem estudo, treino e disciplina. Magos conjuram magias através de movimentos cuidadosamente elaborados, que exigem estudo, treino e disciplina. No passad
  - p. 14 [medium]: layout_blob_line - Pericias: Manobras de Combate Defesas Múltiplas (150* Se personagem NÃO executa defesas extra em um oponente, mas caso esteja lutando com vários oponentes pode lutar com eles normalmente como se estivesse lutando um a um, normalmente para defesas múltiplas o p
  - p. 17 [medium]: layout_blob_line - Aprimoramentos: Kit Ninja Shinobi ((Pontos heroicos 3pts, Expert em combate corporal 1pt*, Coragem (2 Pontos), Patrono (2 Pontos, sua Escola), Deslocamento em Velocidade (1 Ponto), Manobras de Combate 1Pt*, Trespassar ( toda vez que um personagem cause mais da
  - p. 21 [medium]: layout_blob_line - Pericias: Meditação [WILL] 40%; Furtar (DEX) 40; Manobra de Combate (Andar Silencioso (30 O personagem é treinado para andar sem produzir qualquer tipo de som, costuma ser utilizada em conjunto com as perícias subterfúgio e furtividade. Alem disso o personagem

### `um-sussurro-nas-trevas`

- Title: Um Sussurro nas Trevas
- Pages: 113
- Affected pages: 20
- Hard pages: 112
- Medium pages: -
- Easy pages: 1, 21, 22, 23, 26, 28, 29, 32, 39, 41, 46, 47, 53, 54, 55, 65, 73, 109, 113
- Suggested actions: compare with source PDF/OCR or re-extract affected pages; normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 21 [easy]: repeated_terms_or_stat_block - Teste Fácil
  - p. 22 [easy]: table_or_stat_block - Atributo Somado.
  - p. 23 [easy]: repeated_terms_or_stat_block - missão.
  - p. 26 [easy]: repeated_terms_or_stat_block - de
  - p. 28 [easy]: repeated_terms_or_stat_block - Rajada

### `vantagens`

- Title: Vantagens
- Pages: 21
- Affected pages: 15
- Hard pages: -
- Medium pages: 1, 2, 4, 5, 6, 7, 8, 10, 12, 13, 15, 16, 19, 20, 21
- Easy pages: -
- Suggested actions: split long DOCX/layout lines into entries

  - p. 1 [medium]: layout_blob_line - Aceleração (1 pto): Você é mais ágil e pode correr mais rápido e saltar mais longe, sendo até mesmo capaz de permanecer no ar por alguns momentos (como se tivesse Levitação e Habilidade 1; veja Levitação mais adiante). Esta Vantagem acrescenta 1 ponto à Habili
  - p. 2 [medium]: layout_blob_line - Área de Batalha (2 ptos): Gastando 4 Pontos de Magia, você tem o poder de transportar a si mesmo e um ou mais oponentes (mas não colegas) temporariamente para uma "área de batalha", uma outra dimensão onde você leva vantagem em combate. Nenhum outro personagem
  - p. 4 [medium]: layout_blob_line - Bardo (2pts): São espécies de ladrões, só que sua maior habilidade é a arte. Em mundo medievais todas tavernas tem um bardo cantando e enchendo o saco dos outros. Bardos sempre usam uma flauta, trombone ou violinos, em outros casos outros instrumentos. Muitos 
  - p. 5 [medium]: layout_blob_line - Centauro élfico (4 ptos): Centauros élficos são criaturas meio cavalo e meio Elfo. Centauros élficos tem olhos maiores do que o normal (visão aguçada de sentidos especiais), ganham um bonus de f+1 em TODOS os testes de força que fizerem, h+1 em todos os testes
  - p. 6 [medium]: layout_blob_line - Controlar Máquinas (2 ptos): Pode operar os comando de uma máquina ou veículo apenas por contato visual.Caso outra pessoa esteja fisicamente operando os comandos decida o vencedor a partir de uma disputa de FA vs FA.Coragem (0 pto) : Você não sente qualquer fo
  - p. 7 [medium]: layout_blob_line - Domador de Feras (3pts): São os homens (muito raramente mulheres) mais corajosos, eles não sabem o que é a palavra medo. Mas a principal característica de um domador é usa empatia com animais perigosos, como leões, ursos, crocodilos, águias... em em mundos med

### `jutsu-e-um-termo-japones-para-tecnica`

- Title: Jutsu é um termo japonês para técnica
- Pages: 10
- Affected pages: 5
- Hard pages: -
- Medium pages: 1, 7, 9, 10
- Easy pages: 6
- Suggested actions: split long DOCX/layout lines into entries; treat repeated mechanical/stat labels as structured data

  - p. 1 [medium]: layout_blob_line - Jutsu na série (anime/mangá) Naruto são as combinações de movimentos para a criação de uma técnica ninja, ou seja, Jutsu é a mística arte que um ninja usa na batalha. Para usar um Jutsu um ninja precisa usar o Chakra. Chakra vem de dois lugares: da energia do 
  - p. 6 [easy]: repeated_terms_or_stat_block - A raposa de Nove-Caudas mencionou que os olhos e o chakra de Uchiha Sasuke lembravam os de Uchiha Madara, cujo poder chegava a ser até mais sinistro que o seu. Uchiha Sasuke disse que, se esses olhos lhe eram familiar, tal criatura deveria ser a Kyuubi. Se Uch
  - p. 7 [medium]: layout_blob_line - Pein (Rei - 零) - Muito pouco se sabe sobre este personagem mas estima-se que ele seja bastante poderoso. Pein possui a habilidade de criar cópias perfeitas de outros ninjas conservando até mesmo os poderes únicos da linhagem avançada de cada um. Pein também po
  - p. 9 [medium]: layout_blob_line - Uchiha Itachi (Shu - 朱) - O irmão mais velho de Uchiha Sasuke. Também possui um Sharingan, assim como Hatake Kakashi e Uchiha Sasuke. Para obter um Sharingan mais poderoso, o Mangekyou Sharingan, teve que matar o seu melhor amigo (Uchiha Shisui). Logo depois, 
  - p. 10 [medium]: layout_blob_line - Hidan (San - 三) - Um ninja extremamente religioso, que tem como habilidade especial a imortalidade. Não importa quanto dano sofra, ele continua a se levantar. Uma prova disso foi ter sido decapitado por Sarutobi Asuma, e permanecer com vida. Utiliza-se de uma 

### `pactos`

- Title: pactos
- Pages: 6
- Affected pages: 5
- Hard pages: 3
- Medium pages: 1, 5
- Easy pages: 4, 6
- Suggested actions: compare with source PDF/OCR or re-extract affected pages; run targeted encoding/control-character cleanup; treat repeated mechanical/stat labels as structured data

  - p. 1 [medium]: encoding_or_control_noise - 
  - p. 3 [hard]: many_encoding_or_control_chars - 
  - p. 4 [easy]: repeated_terms_or_stat_block - benefícios ou pagamentos em pactos, NÃO que irá
  - p. 5 [medium]: encoding_or_control_noise -     
  - p. 6 [easy]: repeated_terms_or_stat_block - ponto.

### `loucura`

- Title: Loucura
- Pages: 4
- Affected pages: 3
- Hard pages: -
- Medium pages: 1, 2, 4
- Easy pages: -
- Suggested actions: run targeted encoding/control-character cleanup

  - p. 1 [medium]: encoding_or_control_noise - $
  - p. 2 [medium]: encoding_or_control_noise - 7HVWHGH/RXFXUD
  - p. 4 [medium]: encoding_or_control_noise - 

### `arquimago2`

- Title: arquimago2
- Pages: 3
- Affected pages: 2
- Hard pages: -
- Medium pages: 1, 3
- Easy pages: -
- Suggested actions: run targeted encoding/control-character cleanup

  - p. 1 [medium]: encoding_or_control_noise - 
  - p. 3 [medium]: encoding_or_control_noise - 

### `supers01`

- Title: supers01
- Pages: 6
- Affected pages: 2
- Hard pages: 1
- Medium pages: -
- Easy pages: 6
- Suggested actions: compare with source PDF/OCR or re-extract affected pages; treat repeated mechanical/stat labels as structured data

  - p. 1 [hard]: many_encoding_or_control_chars - 
  - p. 6 [easy]: repeated_terms_or_stat_block - Super poder

### `cabala`

- Title: cabala
- Pages: 1
- Affected pages: 1
- Hard pages: -
- Medium pages: 1
- Easy pages: -
- Suggested actions: split long DOCX/layout lines into entries

  - p. 1 [medium]: layout_blob_line - Tp, o negócio do sangue por lava eu li num texto de uma carta (no momento não lembro qual) só não sei se era metaforicamente.Bom, pelo que eu sei, Aphetto era uma região de pântanos e ilhas, cuja parte pantanosa ficava meio que uma "base de operações" da Cabal

### `masmorras`

- Title: Masmorras
- Pages: 1
- Affected pages: 1
- Hard pages: -
- Medium pages: 1
- Easy pages: -
- Suggested actions: split long DOCX/layout lines into entries

  - p. 1 [medium]: layout_blob_line - Maravilha encontraram um baú cheio de bons tesouros magicos; um amuleto elemental da terra (permite ao usuario através de muita concentração atravessar as paredes como se fosse material gelatinoso, porém se perder a concentração ficara preso, e se o medalhão f

### `terras-natais`

- Title: Terras Natais
- Pages: 1
- Affected pages: 1
- Hard pages: -
- Medium pages: 1
- Easy pages: -
- Suggested actions: split long DOCX/layout lines into entries

  - p. 1 [medium]: layout_blob_line - Milhares de anos atrás, um planinauta nomeado Feroz tropeçou em um plano conhecido como as Terras Natais. Logo antes da chegada dele, o mundo tinha sido um plano bonito e sustentável, semelhante a Dominaria. Porém, quando ele chegou viu que as Terras Natais ti

## Medium

### `arkanun`

- Title: Arkanun
- Pages: 240
- Affected pages: 74
- Hard pages: -
- Medium pages: 227, 228, 230, 231, 232, 233, 234
- Easy pages: 1, 9, 10, 14, 17, 50, 53, 54, 65, 66, 75, 76, 77, 78, 79, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92, 96, 98, 100, 101, 102, 103, 104, 105, 107, 111, 114, 116, 119, 123, 125, 126, 134, 136, 142, 145, 148, 151, 154, 160, ... (+17)
- Suggested actions: run targeted encoding/control-character cleanup; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 9 [easy]: repeated_terms_or_stat_block - ·
  - p. 10 [easy]: repeated_terms_or_stat_block - ל.
  - p. 14 [easy]: empty_page - 
  - p. 17 [easy]: repeated_terms_or_stat_block - bem construído.
  - p. 50 [easy]: repeated_terms_or_stat_block - '•·

### `rpg-dragon-ball-oficial-l-by-fractius`

- Title: RPG Dragon Ball Oficial l By Fractius
- Pages: 39
- Affected pages: 35
- Hard pages: -
- Medium pages: 39
- Easy pages: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data

  - p. 4 [easy]: repeated_terms_or_stat_block - Vantagens Permetidas
  - p. 5 [easy]: repeated_terms_or_stat_block - <<Arena>>
  - p. 6 [easy]: repeated_terms_or_stat_block - << Boa Fama >>
  - p. 7 [easy]: repeated_terms_or_stat_block - << Membro Elastico >>
  - p. 8 [easy]: repeated_terms_or_stat_block - << Reflexão >>
  - p. 9 [easy]: repeated_terms_or_stat_block - << Separação >>

### `arcadia-nova-arcadia`

- Title: Arcádia - Nova Arcádia
- Pages: 16
- Affected pages: 3
- Hard pages: -
- Medium pages: 16
- Easy pages: 1, 14
- Suggested actions: run targeted encoding/control-character cleanup; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 14 [easy]: repeated_terms_or_stat_block - envelhecer.
  - p. 16 [medium]: encoding_or_control_noise - rnios

### `assassinos-orientais`

- Title: Assassinos Orientais
- Pages: 14
- Affected pages: 2
- Hard pages: -
- Medium pages: 1, 2
- Easy pages: -
- Suggested actions: run targeted encoding/control-character cleanup

  - p. 1 [medium]: encoding_or_control_noise - 
  - p. 2 [medium]: encoding_or_control_noise - ,QWURGXomR

### `cimeria`

- Title: Ciméria
- Pages: 10
- Affected pages: 1
- Hard pages: -
- Medium pages: 10
- Easy pages: -
- Suggested actions: split long DOCX/layout lines into entries

  - p. 10 [medium]: layout_blob_line - HyboriaClique Aqui para ver o MapaTortage[/align]Na costa de Hyboria, em uma das maiores ilhas do arquipelago Barachan, está um porto para contrabandistas, ladrões e piratas chamado Tortage.Construído na rocha negra de montes pedregosos, a cidade de Tortage é 

## Easy

### `marvel-rpg-7o-edicao`

- Title: MARVEL RPG 7º Edição
- Pages: 178
- Affected pages: 89
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 10, 12, 13, 15, 26, 30, 33, 36, 53, 64, 65, 66, 67, 68, 70, 75, 77, 78, 79, 80, 81, 82, 84, 86, 87, 88, 89, 99, 100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, ... (+39)
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 10 [easy]: repeated_terms_or_stat_block - ATIVIDADE ILEGAL
  - p. 12 [easy]: repeated_terms_or_stat_block - CONCEITOS BÁSICOS
  - p. 13 [easy]: repeated_terms_or_stat_block - Rodada:
  - p. 15 [easy]: repeated_terms_or_stat_block - História
  - p. 26 [easy]: repeated_terms_or_stat_block - Pontos Heróicos

### `santa-cruz-biblioteca-elfica`

- Title: Santa-cruz-biblioteca-elfica
- Pages: 202
- Affected pages: 75
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 3, 4, 7, 9, 10, 13, 14, 16, 17, 21, 34, 35, 36, 42, 43, 46, 47, 49, 52, 57, 60, 62, 63, 65, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 87, 89, 91, 94, 95, 97, 98, 100, 104, ... (+25)
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 3 [easy]: empty_page - 
  - p. 4 [easy]: empty_page - 
  - p. 7 [easy]: empty_page - 
  - p. 9 [easy]: repeated_terms_or_stat_block - golpe”....
  - p. 10 [easy]: repeated_terms_or_stat_block - jogo.

### `tagmar-daemon-versao-completa`

- Title: Tagmar-Daemon-Versao-Completa
- Pages: 111
- Affected pages: 60
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 2, 7, 8, 9, 10, 11, 13, 16, 18, 20, 22, 24, 25, 34, 36, 37, 38, 39, 41, 42, 45, 46, 49, 56, 57, 58, 62, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 84, 85, 86, 87, 88, ... (+10)
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: empty_page - 
  - p. 7 [easy]: repeated_terms_or_stat_block - 9oooooo
  - p. 8 [easy]: repeated_terms_or_stat_block - 9oooooo
  - p. 9 [easy]: repeated_terms_or_stat_block - 9oooooo
  - p. 10 [easy]: repeated_terms_or_stat_block - 9oooooo

### `tagmar-daemon`

- Title: Tagmar Daemon
- Pages: 89
- Affected pages: 57
- Hard pages: -
- Medium pages: -
- Easy pages: 3, 4, 5, 6, 7, 10, 14, 15, 17, 18, 19, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 38, 39, 41, 43, 45, 46, 48, 50, 51, 52, 53, 54, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, ... (+7)
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 3 [easy]: repeated_terms_or_stat_block - Introdução
  - p. 4 [easy]: repeated_terms_or_stat_block - colecionadores!).
  - p. 5 [easy]: repeated_terms_or_stat_block - Capítulo 1:
  - p. 6 [easy]: repeated_terms_or_stat_block - gosta.
  - p. 7 [easy]: repeated_terms_or_stat_block - Capítulo 2
  - p. 10 [easy]: repeated_terms_or_stat_block - 37/37

### `daemon-tormenta`

- Title: Daemon Tormenta
- Pages: 181
- Affected pages: 56
- Hard pages: -
- Medium pages: -
- Easy pages: 8, 11, 13, 14, 18, 25, 28, 29, 33, 34, 36, 56, 59, 69, 92, 95, 96, 99, 101, 102, 103, 106, 113, 115, 117, 118, 119, 126, 129, 130, 131, 132, 140, 141, 142, 145, 146, 147, 148, 149, 155, 156, 157, 158, 161, 162, 163, 164, 167, 168, ... (+6)
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 8 [easy]: repeated_terms_or_stat_block - especialistas.
  - p. 11 [easy]: repeated_terms_or_stat_block - História
  - p. 13 [easy]: repeated_terms_or_stat_block - FOR 08
  - p. 14 [easy]: repeated_terms_or_stat_block - Perícia
  - p. 18 [easy]: repeated_terms_or_stat_block - personagem.
  - p. 25 [easy]: repeated_terms_or_stat_block - Humanos

### `anjos-jyhad-guerra-santa-biblioteca-elfica`

- Title: Anjos Jyhad-guerra-santa-biblioteca-elfica
- Pages: 96
- Affected pages: 52
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 5, 7, 8, 10, 13, 15, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30, 31, 32, 34, 35, 36, 44, 50, 51, 55, 56, 58, 61, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 82, 85, 86, 88, 90, ... (+2)
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - E!
  - p. 5 [easy]: repeated_terms_or_stat_block - CenceitTes BÁSICOS
  - p. 7 [easy]: repeated_terms_or_stat_block - GUERRA SANTA
  - p. 8 [easy]: empty_page - 
  - p. 10 [easy]: repeated_terms_or_stat_block - nos belicosos.
  - p. 13 [easy]: repeated_terms_or_stat_block - PROFETAS

### `sistema-daemon-2-x`

- Title: Sistema-Daemon-2-X
- Pages: 98
- Affected pages: 43
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 5, 6, 8, 11, 13, 14, 16, 22, 23, 24, 37, 38, 44, 45, 47, 48, 55, 57, 58, 62, 63, 64, 66, 67, 70, 71, 75, 76, 78, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 96
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 5 [easy]: repeated_terms_or_stat_block - Conceitos Básicos
  - p. 6 [easy]: repeated_terms_or_stat_block - características.
  - p. 8 [easy]: repeated_terms_or_stat_block - Para
  - p. 11 [easy]: repeated_terms_or_stat_block - Atributos
  - p. 13 [easy]: table_or_stat_block - FR

### `spiritum`

- Title: Spiritum
- Pages: 114
- Affected pages: 42
- Hard pages: -
- Medium pages: -
- Easy pages: 5, 6, 8, 13, 15, 22, 25, 29, 31, 45, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 66, 67, 69, 71, 73, 74, 77, 79, 80, 84, 87, 88, 89, 90, 93, 94, 100, 107, 108, 110, 112
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 5 [easy]: repeated_terms_or_stat_block - Conceitos Básicos
  - p. 6 [easy]: repeated_terms_or_stat_block - Caminhos de Magia: São divisões da Magia que um fei-
  - p. 8 [easy]: empty_page - 
  - p. 13 [easy]: repeated_terms_or_stat_block - Forma-Pensamento
  - p. 15 [easy]: repeated_terms_or_stat_block - Vales Espirituais
  - p. 22 [easy]: repeated_terms_or_stat_block - Glock 24

### `neokosmos-biblioteca-elfica`

- Title: Neokosmos-biblioteca-elfica
- Pages: 197
- Affected pages: 41
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 10, 13, 16, 18, 20, 22, 27, 44, 58, 72, 90, 91, 95, 97, 100, 101, 102, 121, 123, 148, 154, 156, 158, 159, 160, 165, 169, 170, 172, 173, 174, 177, 179, 181, 182, 183, 184, 185, 190, 193
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 10 [easy]: repeated_terms_or_stat_block - ~
  - p. 13 [easy]: empty_page - 
  - p. 16 [easy]: repeated_terms_or_stat_block - ~
  - p. 18 [easy]: repeated_terms_or_stat_block - ~
  - p. 20 [easy]: repeated_terms_or_stat_block - ~~~~~~~~~~~~~~~~~

### `anjos-a-cidade-de-prata`

- Title: Anjos_-_A_Cidade_de_Prata
- Pages: 75
- Affected pages: 35
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 5, 7, 8, 9, 11, 12, 19, 22, 24, 26, 29, 35, 37, 39, 45, 47, 48, 49, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 65, 67, 69, 70, 71, 72
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - M
  - p. 5 [easy]: repeated_terms_or_stat_block - , _
  - p. 7 [easy]: repeated_terms_or_stat_block - ._
  - p. 8 [easy]: tiny_page - > )
  - p. 9 [easy]: repeated_terms_or_stat_block - Copérnico,
  - p. 11 [easy]: repeated_terms_or_stat_block - 0 cetnec®

### `sistema-daemon-3-0`

- Title: Sistema-Daemon-3-0
- Pages: 82
- Affected pages: 32
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 5, 6, 8, 11, 13, 14, 16, 24, 30, 38, 39, 43, 45, 46, 49, 57, 59, 60, 64, 65, 66, 68, 69, 71, 72, 73, 74, 78, 79, 80, 81
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 5 [easy]: repeated_terms_or_stat_block - Conceitos Básicos
  - p. 6 [easy]: repeated_terms_or_stat_block - características.
  - p. 8 [easy]: repeated_terms_or_stat_block - Para
  - p. 11 [easy]: repeated_terms_or_stat_block - Atributos
  - p. 13 [easy]: table_or_stat_block - FR

### `vampiros-mitologicos`

- Title: Vampiros Mitológicos
- Pages: 137
- Affected pages: 32
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 5, 8, 11, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 61, 66, 71, 76, 87, 95, 97, 99, 102, 108, 109, 110, 111, 137
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 5 [easy]: empty_page - 
  - p. 8 [easy]: empty_page - 
  - p. 11 [easy]: repeated_terms_or_stat_block - Conceitos Básicos
  - p. 17 [easy]: empty_page - 
  - p. 20 [easy]: empty_page - 

### `vikings-biblioteca-elfica`

- Title: Vikings-biblioteca-elfica
- Pages: 138
- Affected pages: 32
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 14, 16, 17, 19, 20, 23, 27, 32, 33, 51, 57, 60, 62, 63, 65, 67, 79, 82, 95, 98, 99, 101, 102, 103, 104, 105, 106, 113, 122, 130, 131
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - ANTÔNIO AUGUSTO SHAFTIEL
  - p. 14 [easy]: repeated_terms_or_stat_block - E
  - p. 16 [easy]: repeated_terms_or_stat_block - daquela aposta;
  - p. 17 [easy]: repeated_terms_or_stat_block - »
  - p. 19 [easy]: repeated_terms_or_stat_block - lhando veneno.
  - p. 20 [easy]: repeated_terms_or_stat_block - O deus foi levado até Geirródr « reconheceu que por trás

### `dragao-brasil-especial-06-trevas`

- Title: Dragão Brasil especial 06 - Trevas
- Pages: 84
- Affected pages: 31
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 2, 6, 7, 12, 18, 20, 23, 26, 29, 30, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 50, 62, 67, 68, 71, 84
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: empty_page - 
  - p. 6 [easy]: repeated_terms_or_stat_block - , ~
  - p. 7 [easy]: repeated_terms_or_stat_block - ,
  - p. 12 [easy]: repeated_terms_or_stat_block - ~
  - p. 18 [easy]: repeated_terms_or_stat_block - T

### `guia-de-classes-de-prestigio-biblioteca-elfica`

- Title: Guia-de-classes-de-prestigio-biblioteca-elfica
- Pages: 130
- Affected pages: 31
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 5, 7, 18, 24, 29, 31, 35, 36, 37, 42, 43, 45, 46, 48, 49, 61, 66, 78, 84, 90, 92, 96, 100, 102, 105, 106, 108, 114, 116, 120
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 5 [easy]: repeated_terms_or_stat_block - anteriormente.
  - p. 7 [easy]: repeated_terms_or_stat_block - + 1 nív~l
  - p. 18 [easy]: empty_page - 
  - p. 24 [easy]: tiny_page - llustraçã o por Fred
  - p. 29 [easy]: repeated_terms_or_stat_block - Daemon

### `modulo-basico-expandido-e-modificado`

- Title: Módulo Básico - Expandido e Modificado
- Pages: 106
- Affected pages: 30
- Hard pages: -
- Medium pages: -
- Easy pages: 5, 6, 16, 17, 40, 41, 43, 48, 51, 59, 61, 67, 68, 70, 71, 81, 84, 85, 86, 87, 88, 90, 91, 92, 95, 97, 99, 103, 104, 105
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data

  - p. 5 [easy]: repeated_terms_or_stat_block - centagem.
  - p. 6 [easy]: repeated_terms_or_stat_block - Caminhos de Magia: São divisões da Magia que um feiticeiro pode escolher para aprender. Existem 6 Cami-
  - p. 16 [easy]: table_or_stat_block - 3D
  - p. 17 [easy]: repeated_terms_or_stat_block - Aprimoramentos
  - p. 40 [easy]: repeated_terms_or_stat_block - Animais*
  - p. 41 [easy]: repeated_terms_or_stat_block - barras.

### `sda-rpg`

- Title: sda_rpg
- Pages: 48
- Affected pages: 30
- Hard pages: -
- Medium pages: -
- Easy pages: 4, 6, 7, 8, 9, 10, 11, 14, 16, 17, 18, 19, 20, 25, 27, 28, 29, 30, 31, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 4 [easy]: repeated_terms_or_stat_block - Como em qualquer jogo, é preciso conhecer as regras e os
  - p. 6 [easy]: repeated_terms_or_stat_block - Os Elfos ou Primogênitos de Ilúvatar despertaram nos Dias da
  - p. 7 [easy]: repeated_terms_or_stat_block - A Segunda era
  - p. 8 [easy]: repeated_terms_or_stat_block - A Terceira era
  - p. 9 [easy]: repeated_terms_or_stat_block - za em Insengar destruída e cercada pelos misteriosos Ents.
  - p. 10 [easy]: repeated_terms_or_stat_block - Fastred e Elanor se origina os Lindofilhos das Torres, das coli-

### `hi-brazil-biblioteca-elfica`

- Title: Hi-brazil-biblioteca-elfica
- Pages: 102
- Affected pages: 24
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 4, 6, 27, 28, 30, 34, 37, 38, 40, 43, 54, 57, 59, 60, 61, 65, 71, 73, 74, 76, 78, 83, 84
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 4 [easy]: repeated_terms_or_stat_block - Os Areentos
  - p. 6 [easy]: repeated_terms_or_stat_block - ~ino dos CJ\e;na-ymas
  - p. 27 [easy]: repeated_terms_or_stat_block - 6 o
  - p. 28 [easy]: empty_page - 
  - p. 30 [easy]: empty_page - 

### `o-corvo`

- Title: O Corvo
- Pages: 40
- Affected pages: 23
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 2, 3, 6, 7, 8, 9, 10, 14, 18, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 37, 38
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: empty_page - 
  - p. 3 [easy]: tiny_page - O Corvo
  - p. 6 [easy]: repeated_terms_or_stat_block - Estou morto…
  - p. 7 [easy]: empty_page - 
  - p. 8 [easy]: repeated_terms_or_stat_block - CONCEITOS BÐSICOS

### `grimorio`

- Title: Grimorio
- Pages: 180
- Affected pages: 22
- Hard pages: -
- Medium pages: -
- Easy pages: 2, 3, 11, 13, 14, 15, 17, 18, 32, 33, 47, 52, 96, 97, 107, 117, 128, 137, 140, 160, 169, 179
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 2 [easy]: empty_page - 
  - p. 3 [easy]: empty_page - 
  - p. 11 [easy]: repeated_terms_or_stat_block - Nomenclatura
  - p. 13 [easy]: repeated_terms_or_stat_block - natureza (Ritual).
  - p. 14 [easy]: repeated_terms_or_stat_block - Efeito
  - p. 15 [easy]: repeated_terms_or_stat_block - proteções.

### `arkanun-1e-ultra-raro`

- Title: Arkanun-1e-ultra-raro
- Pages: 80
- Affected pages: 21
- Hard pages: -
- Medium pages: -
- Easy pages: 8, 12, 19, 31, 33, 34, 37, 38, 40, 44, 48, 50, 53, 56, 58, 60, 62, 64, 72, 77, 79
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 8 [easy]: repeated_terms_or_stat_block - — Sim, Meggie.
  - p. 12 [easy]: repeated_terms_or_stat_block - aventura de-
  - p. 19 [easy]: empty_page - 
  - p. 31 [easy]: repeated_terms_or_stat_block - Fogo
  - p. 33 [easy]: repeated_terms_or_stat_block - Luz
  - p. 34 [easy]: repeated_terms_or_stat_block - DRAGÃO ESPECIAL

### `daemon-anime-rpg`

- Title: Daemon - Anime RPG
- Pages: 126
- Affected pages: 19
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 7, 8, 19, 61, 66, 79, 80, 84, 85, 90, 91, 95, 96, 101, 106, 107, 111, 126
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 7 [easy]: repeated_terms_or_stat_block - }
  - p. 8 [easy]: repeated_terms_or_stat_block - Dados de Comparação: É uma for­
  - p. 19 [easy]: repeated_terms_or_stat_block - Imobilização, Quebramento).
  - p. 61 [easy]: repeated_terms_or_stat_block - Co1no Funciona1n ?
  - p. 66 [easy]: repeated_terms_or_stat_block - Munição: 9mm

### `trevas-diego`

- Title: trevas_DIEGO
- Pages: 71
- Affected pages: 19
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 5, 8, 10, 12, 16, 29, 34, 37, 39, 41, 47, 53, 56, 57, 58, 63, 67, 69
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - Trevas
  - p. 5 [easy]: empty_page - 
  - p. 8 [easy]: tiny_page - atributos
  - p. 10 [easy]: repeated_terms_or_stat_block - Significado dos
  - p. 12 [easy]: repeated_terms_or_stat_block - 24-27
  - p. 16 [easy]: repeated_terms_or_stat_block - Faqueiro Spetsnaz

### `guia-de-itens-magicos`

- Title: Guia de Itens Mágicos
- Pages: 288
- Affected pages: 18
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 5, 6, 7, 9, 10, 17, 31, 51, 120, 253, 268, 274, 275, 278, 279, 287, 288
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 5 [easy]: repeated_terms_or_stat_block - Sumario
  - p. 6 [easy]: repeated_terms_or_stat_block - Asas Magicas
  - p. 7 [easy]: repeated_terms_or_stat_block - Contrato Magko
  - p. 9 [easy]: repeated_terms_or_stat_block - Ovoda Fenix
  - p. 10 [easy]: repeated_terms_or_stat_block - Robe Astral

### `mutacao`

- Title: Mutação
- Pages: 129
- Affected pages: 18
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 12, 38, 42, 43, 44, 45, 49, 50, 52, 56, 76, 77, 81, 82, 113, 114, 129
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - mutação
  - p. 12 [easy]: repeated_terms_or_stat_block - Força (FOR)
  - p. 38 [easy]: repeated_terms_or_stat_block - Todas
  - p. 42 [easy]: repeated_terms_or_stat_block - Recursos
  - p. 43 [easy]: repeated_terms_or_stat_block - armas brancas
  - p. 44 [easy]: repeated_terms_or_stat_block - Armas

### `sistema-daemon-modulo-basico-dragonslayer-01-e-02`

- Title: Sistema-Daemon-Modulo-Basico-DragonSlayer-01-e-02
- Pages: 36
- Affected pages: 17
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 2, 6, 7, 8, 12, 16, 18, 22, 24, 25, 27, 28, 30, 31, 32, 33
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: empty_page - 
  - p. 6 [easy]: repeated_terms_or_stat_block - |
  - p. 7 [easy]: repeated_terms_or_stat_block - Caminhos de Magia: São divisões da Magia que um
  - p. 8 [easy]: repeated_terms_or_stat_block - qualquer período.
  - p. 12 [easy]: repeated_terms_or_stat_block - ATRIBUTOS Físicos

### `jedi`

- Title: jedi
- Pages: 36
- Affected pages: 15
- Hard pages: -
- Medium pages: -
- Easy pages: 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 17, 21, 22, 23, 25
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 3 [easy]: repeated_terms_or_stat_block - pelo mal.
  - p. 4 [easy]: repeated_terms_or_stat_block - Mestre Yoda!”
  - p. 5 [easy]: repeated_terms_or_stat_block - mento proibido.
  - p. 7 [easy]: repeated_terms_or_stat_block - Novas Pericias
  - p. 8 [easy]: repeated_terms_or_stat_block - Novos Kits
  - p. 9 [easy]: repeated_terms_or_stat_block - Trapaceiro

### `psi`

- Title: psi
- Pages: 27
- Affected pages: 14
- Hard pages: -
- Medium pages: -
- Easy pages: 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 5 [easy]: repeated_terms_or_stat_block - Poderes Psíquicos
  - p. 8 [easy]: repeated_terms_or_stat_block - Assombro
  - p. 9 [easy]: repeated_terms_or_stat_block - Cancelar Poder
  - p. 10 [easy]: repeated_terms_or_stat_block - Custo: Padrão
  - p. 11 [easy]: repeated_terms_or_stat_block - Derreter
  - p. 12 [easy]: repeated_terms_or_stat_block - Eletrostática

### `one-punch-man-rpg`

- Title: One Punch Man RPG
- Pages: 49
- Affected pages: 13
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 4, 5, 10, 21, 22, 24, 26, 28, 29, 30, 32, 36
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - 1ª Edição
  - p. 4 [easy]: repeated_terms_or_stat_block - Conceitos Básicos
  - p. 5 [easy]: repeated_terms_or_stat_block - pelo mago.
  - p. 10 [easy]: repeated_terms_or_stat_block - Atributos
  - p. 21 [easy]: repeated_terms_or_stat_block - Pontos Heróicos
  - p. 22 [easy]: repeated_terms_or_stat_block - e Testes.

### `varna-chamado-da-guerra`

- Title: Varna - Chamado da Guerra
- Pages: 38
- Affected pages: 12
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 3, 5, 11, 12, 13, 16, 19, 24, 26, 31, 38
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 3 [easy]: repeated_terms_or_stat_block - Dedicatória:
  - p. 5 [easy]: repeated_terms_or_stat_block - t
  - p. 11 [easy]: repeated_terms_or_stat_block - da a
  - p. 12 [easy]: repeated_terms_or_stat_block - uma
  - p. 13 [easy]: repeated_terms_or_stat_block - impressionantes.

### `anime-rpg-powers`

- Title: Anime RPG - Powers
- Pages: 45
- Affected pages: 10
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 2, 5, 11, 15, 18, 34, 42, 44, 45
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: tiny_page - POWERS
  - p. 5 [easy]: empty_page - 
  - p. 11 [easy]: repeated_terms_or_stat_block - encorajamento.
  - p. 15 [easy]: repeated_terms_or_stat_block - aprimoramento Equipamento.
  - p. 18 [easy]: repeated_terms_or_stat_block - Aumento

### `luz-e-sombra-rpg-livro-de-regras-portugues-do-brasil-br`

- Title: Luz_e_Sombra_RPG_-_Livro_de_Regras_(Português_do_Brasil)(BR)
- Pages: 126
- Affected pages: 9
- Hard pages: -
- Medium pages: -
- Easy pages: 79, 101, 104, 106, 116, 117, 118, 123, 124
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 79 [easy]: repeated_terms_or_stat_block - Magia.
  - p. 101 [easy]: repeated_terms_or_stat_block - Custo:
  - p. 104 [easy]: repeated_terms_or_stat_block - portador.
  - p. 106 [easy]: repeated_terms_or_stat_block - outros locais.
  - p. 116 [easy]: repeated_terms_or_stat_block - Vamos
  - p. 117 [easy]: repeated_terms_or_stat_block - Kelther

### `naruto-daemon-2a-ed`

- Title: Naruto-daemon-2ª-Ed
- Pages: 93
- Affected pages: 9
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 6, 9, 10, 13, 38, 50, 51, 72
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - Por Luan Quintella
  - p. 6 [easy]: repeated_terms_or_stat_block - Suijinheki, enfim.
  - p. 9 [easy]: repeated_terms_or_stat_block - conseguir
  - p. 10 [easy]: repeated_terms_or_stat_block - Internos:
  - p. 13 [easy]: repeated_terms_or_stat_block - Kawarimi:
  - p. 38 [easy]: repeated_terms_or_stat_block - qualquer

### `metropolis-2`

- Title: Metropolis (2)
- Pages: 92
- Affected pages: 8
- Hard pages: -
- Medium pages: -
- Easy pages: 6, 16, 35, 76, 77, 78, 81, 91
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 6 [easy]: repeated_terms_or_stat_block - Metrópolis
  - p. 16 [easy]: repeated_terms_or_stat_block - Metrópolis
  - p. 35 [easy]: repeated_terms_or_stat_block - filhos,
  - p. 76 [easy]: repeated_terms_or_stat_block - Bel´Cah
  - p. 77 [easy]: repeated_terms_or_stat_block - Chezii
  - p. 78 [easy]: repeated_terms_or_stat_block - Metrópolis

### `veiculos`

- Title: Veiculos
- Pages: 35
- Affected pages: 8
- Hard pages: -
- Medium pages: -
- Easy pages: 5, 8, 10, 11, 12, 14, 16, 21
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 5 [easy]: repeated_terms_or_stat_block - detalhes.
  - p. 8 [easy]: repeated_terms_or_stat_block - Primeiro passo
  - p. 10 [easy]: repeated_terms_or_stat_block - Acessórios
  - p. 11 [easy]: repeated_terms_or_stat_block - que:
  - p. 12 [easy]: repeated_terms_or_stat_block - Novos Aprimoramentos
  - p. 14 [easy]: repeated_terms_or_stat_block - Regras especiais

### `templarios-biblioteca-elfica`

- Title: Templarios-biblioteca-elfica
- Pages: 50
- Affected pages: 7
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 2, 7, 8, 9, 12, 39
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - MARCELO DEL DEBBIO
  - p. 2 [easy]: empty_page - 
  - p. 7 [easy]: repeated_terms_or_stat_block - nos sacramentos;
  - p. 8 [easy]: repeated_terms_or_stat_block - “Historiado
  - p. 9 [easy]: repeated_terms_or_stat_block - Distória :
  - p. 12 [easy]: repeated_terms_or_stat_block - Personagens de TEMPLÁRIOS começam ojogo com

### `guia-de-armas-de-fogo-3a-edicao`

- Title: Guia de Armas de Fogo - 3a Edição
- Pages: 141
- Affected pages: 6
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 2, 138, 139, 140, 141
- Suggested actions: normalize tables/stat blocks before entity extraction; treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: empty_page - 
  - p. 138 [easy]: repeated_terms_or_stat_block, table_or_stat_block - 44 $W
  - p. 139 [easy]: repeated_terms_or_stat_block - ~
  - p. 140 [easy]: repeated_terms_or_stat_block - ~
  - p. 141 [easy]: empty_page - 

### `guia-de-monstros-de-arton`

- Title: Guia de Monstros de Arton
- Pages: 130
- Affected pages: 5
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 41, 86, 124, 130
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 41 [easy]: repeated_terms_or_stat_block - Resistência com um redutor de -1. Isso não tem efeito sobre
  - p. 86 [easy]: empty_page - 
  - p. 124 [easy]: empty_page - 
  - p. 130 [easy]: empty_page - 

### `santa-cruz-inferno-verde-biblioteca-elfica`

- Title: Santa-cruz-inferno-verde-biblioteca-elfica
- Pages: 51
- Affected pages: 5
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 2, 31, 42, 43
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 2 [easy]: empty_page - 
  - p. 31 [easy]: repeated_terms_or_stat_block - Inspirar Terror
  - p. 42 [easy]: repeated_terms_or_stat_block - Criar ilusão
  - p. 43 [easy]: repeated_terms_or_stat_block - de

### `anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica`

- Title: Anjos-caidos-dragao-brasil-especial-16-biblioteca-elfica
- Pages: 32
- Affected pages: 4
- Hard pages: -
- Medium pages: -
- Easy pages: 3, 5, 13, 16
- Suggested actions: drop or mark cover/page-number-only pages

  - p. 3 [easy]: empty_page - 
  - p. 5 [easy]: tiny_page - |
  - p. 13 [easy]: tiny_page - —
  - p. 16 [easy]: tiny_page - a

### `inquisicao-biblioteca-elfica`

- Title: Inquisicao-biblioteca-elfica
- Pages: 50
- Affected pages: 4
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 6, 29, 50
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 6 [easy]: empty_page - 
  - p. 29 [easy]: repeated_terms_or_stat_block - Pontos Heróicos
  - p. 50 [easy]: empty_page - 

### `mortos-vivos-2`

- Title: Mortos vivos 2
- Pages: 27
- Affected pages: 4
- Hard pages: -
- Medium pages: -
- Easy pages: 19, 22, 25, 26
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 19 [easy]: repeated_terms_or_stat_block - 1o Círculo
  - p. 22 [easy]: repeated_terms_or_stat_block - poderes individualmente.
  - p. 25 [easy]: repeated_terms_or_stat_block - Impureza
  - p. 26 [easy]: repeated_terms_or_stat_block - riam normalmente.

### `sobrenatural`

- Title: Sobrenatural
- Pages: 11
- Affected pages: 4
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 3, 8, 9
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 1 [easy]: repeated_terms_or_stat_block - REDERPG
  - p. 3 [easy]: repeated_terms_or_stat_block - REDERPG
  - p. 8 [easy]: repeated_terms_or_stat_block - REDERPG
  - p. 9 [easy]: repeated_terms_or_stat_block - REDERPG

### `anime-rpg-supers-powers`

- Title: Anime RPG - Supers - Powers
- Pages: 10
- Affected pages: 3
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 4, 10
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: tiny_page - POWERS
  - p. 4 [easy]: empty_page - 
  - p. 10 [easy]: repeated_terms_or_stat_block - encorajamento.

### `kits-arton`

- Title: Kits Arton
- Pages: 51
- Affected pages: 3
- Hard pages: -
- Medium pages: -
- Easy pages: 11, 19, 51
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 11 [easy]: repeated_terms_or_stat_block - grande
  - p. 19 [easy]: repeated_terms_or_stat_block - Keenn
  - p. 51 [easy]: repeated_terms_or_stat_block - NOVAS REGRAS

### `anjos-a-cidade-de-prata-angelicos-sicarios`

- Title: Anjos - A Cidade de Prata - Angélicos Sicários
- Pages: 33
- Affected pages: 2
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 33
- Suggested actions: drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 33 [easy]: empty_page - 

### `daiphir-legado-de-sangue`

- Title: Daiphir - Legado de Sangue
- Pages: 21
- Affected pages: 2
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 10
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 10 [easy]: repeated_terms_or_stat_block - Caracter¤sticas

### `metropolis`

- Title: metropolis
- Pages: 8
- Affected pages: 2
- Hard pages: -
- Medium pages: -
- Easy pages: 1, 4
- Suggested actions: treat repeated mechanical/stat labels as structured data; drop or mark cover/page-number-only pages

  - p. 1 [easy]: empty_page - 
  - p. 4 [easy]: repeated_terms_or_stat_block - puder conceber...

### `naruto-rpg-daemon-2a-edicao`

- Title: Naruto RPG Daemon - 2ª Edição
- Pages: 23
- Affected pages: 2
- Hard pages: -
- Medium pages: -
- Easy pages: 9, 13
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 9 [easy]: repeated_terms_or_stat_block - -- HIREARQUIA NINJA --
  - p. 13 [easy]: repeated_terms_or_stat_block - Selamento)

### `origem-e-descendencia-racial-v-teste`

- Title: Origem e Descendência Racial (v. teste)
- Pages: 16
- Affected pages: 2
- Hard pages: -
- Medium pages: -
- Easy pages: 2, 3
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 2 [easy]: repeated_terms_or_stat_block - Em termos de jogo, ao invés de possuir uma Origem Racial o Personagem
  - p. 3 [easy]: repeated_terms_or_stat_block - Tamanho

### `existe-uma-cidade-nos-distritos-cujo-unico-objetivo-e-a-satisfac-u00e3o`

- Title: Existe uma cidade nos distritos cujo único objetivo é a satisfaç_U00E3o
- Pages: 1
- Affected pages: 1
- Hard pages: -
- Medium pages: -
- Easy pages: 1
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 1 [easy]: repeated_terms_or_stat_block - Fundação

### `guia-de-armas-medievais-3a-edicao`

- Title: Guia de Armas Medievais - 3ª Edição
- Pages: 146
- Affected pages: 1
- Hard pages: -
- Medium pages: -
- Easy pages: 145
- Suggested actions: drop or mark cover/page-number-only pages

  - p. 145 [easy]: empty_page - 

### `masmorra-goblin`

- Title: Masmorra  Goblin
- Pages: 1
- Affected pages: 1
- Hard pages: -
- Medium pages: -
- Easy pages: 1
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 1 [easy]: repeated_terms_or_stat_block - Masmorra Goblin

### `naruto`

- Title: naruto
- Pages: 24
- Affected pages: 1
- Hard pages: -
- Medium pages: -
- Easy pages: 18
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 18 [easy]: repeated_terms_or_stat_block - seu sucessor.

### `novo-aeon-guia-basico`

- Title: Novo Aeon - Guia Básico
- Pages: 185
- Affected pages: 1
- Hard pages: -
- Medium pages: -
- Easy pages: 2
- Suggested actions: drop or mark cover/page-number-only pages

  - p. 2 [easy]: tiny_page - Suplemento para o jogo

### `regra-opcional-ataques-a-objetos`

- Title: Regra Opcional Ataques a Objetos
- Pages: 1
- Affected pages: 1
- Hard pages: -
- Medium pages: -
- Easy pages: 1
- Suggested actions: treat repeated mechanical/stat labels as structured data

  - p. 1 [easy]: repeated_terms_or_stat_block - ObjetoIPPVsArma

## Ok After Audit

### `ficha-mago-trevas`

- Title: ficha_mago_trevas
- Pages: 1
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `fusd-r6`

- Title: FUSD-R6
- Pages: 4
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `juppongatana`

- Title: juppongatana
- Pages: 10
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `livrodomal`

- Title: livrodomal
- Pages: 26
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `os-invocadores-de-demencia`

- Title: Os Invocadores de demência
- Pages: 2
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `phage`

- Title: Phage
- Pages: 8
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `samurai-shodown-v-move-list`

- Title: Samurai Shodown V Move List
- Pages: 41
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `samurai-x`

- Title: Samurai X
- Pages: 11
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `talentos`

- Title: talentos
- Pages: 9
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction


### `trevas-do-oriente-28-palacios`

- Title: Trevas do oriente - 28 Palácios
- Pages: 27
- Affected pages: 0
- Hard pages: -
- Medium pages: -
- Easy pages: -
- Suggested actions: manual spot check before final extraction

