# Certified category gap triage

Triagem curta do pente fino feito sobre as categorias ja mapeadas: aprimoramentos, kits, classes, racas, linhagens, poderes e magias.

Relatorio bruto: `certified-category-gap-audit.md`.

## Resultado geral

- Nenhum item certificado apareceu publicado em area diferente da trava.
- As travas atuais continuam consistentes: aprimoramentos 453, kits 191, classes 12, racas 47, linhagens 70, poderes 358, magias 217.
- O pente fino encontrou candidatos fora das categorias, mas parte relevante e ruido de palavra-chave, secoes de livro ou itens que pertencem a categorias futuras, especialmente rituais.

## Prioridade alta

### Kits

Foram encontrados 122 rejeitados com sinal forte de revisao. A maioria foi rejeitada por `text_only_context_without_name_kit_evidence`, mesmo contendo estrutura mecanica de kit/profissao/arquetipo, como custo, pericias e aprimoramentos.

Fontes mais afetadas:

- `ark-a-nun-arquivos-de-bel-kalaa`: 34
- `pontos-heroicos`: 15
- `clube-de-caca-guia-do-jogador`: 11
- `guia-de-racas-de-arton-tormentarpg`: 9
- `arcanis`: 8
- `desentsu`: 8
- `racas`: 7

Acao recomendada: ajustar a certificacao de kits para aceitar entradas textuais completas quando houver sinais mecanicos suficientes, sem misturar com classes.

### Quarentena de aprimoramentos

Ha 11 itens legados em quarentena. Parte parece secao/resumo, nao aprimoramento granular. Possiveis itens reais precisam de leitura pontual no texto-fonte.

Fontes:

- `abismo-infinito-quick-start`: 5
- `animalidade`: 3
- `alastores-a-justica-infernal`: 2
- `alianca-daemon-01`: 1

Acao recomendada: promover apenas itens individuais reais, como aprimoramento com custo/efeito proprio; manter secoes fora.

### Quarentena de kits

Ha 2 itens legados em quarentena:

- `alastores-a-justica-infernal` / `Auxiliar dos Alastores`
- `alastores-a-justica-infernal` / `Legionario Alastor`

Acao recomendada: reler a fonte e promover apenas se forem kits/profissoes/arquetipos completos.

## Prioridade media

### Racas

O relatorio bruto mostra 38 rejeitados para revisar e 153 partes candidatas. A maior parte da fonte `racas` parece conteudo mecanico real, mas parte pode estar fora por duplicidade de conteudo ja certificado em outra fonte. Como a regra atual e nao duplicar canonicos, isso nao deve ser promovido automaticamente.

Acao recomendada: comparar os candidatos de `racas` com os 47 itens ja travados e promover somente o que nao for duplicado canonico.

### Linhagens

Ha 71 rejeitados para revisar e 110 partes candidatas. Muitos parecem narrativos ou secoes, mas alguns nomes tem cara de linhagem real.

Fontes mais afetadas:

- `youkai-kyuukai`: 17
- `lobisomem-a-maldicao-v2-biblioteca-elfica`: 10
- `dragoes-reis-caidos-sistema-daemon`: 6
- `neter-khertet-a-cidade-dourada-de-ra-biblioteca-elfica`: 5

Acao recomendada: fazer uma segunda passada especifica para linhagens narrativas, sem exigir custo mecanico de raca.

## Prioridade baixa

### Classes

Nao ha rejeitados relevantes nem quarentena. As 19 partes candidatas parecem majoritariamente ruido de termos como caminho/profissao em secoes de poder, magia ou texto narrativo.

Acao recomendada: manter sem alteracao por enquanto.

### Poderes e magias

Nao ha quarentena nem publicacao cruzada. Os rejeitados sao numerosos, mas muitos batem com rejeicoes esperadas: rituais, blocos de criatura, secoes, nomes quebrados ou ausencia de sinal mecanico.

Acao recomendada: nao mexer agora; separar os candidatos de ritual quando a etapa de rituais for retomada.
