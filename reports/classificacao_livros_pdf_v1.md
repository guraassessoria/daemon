# Classificação preliminar dos PDFs em `Livros/`

Data: 2026-05-15
Branch: `classificacao-livros-pdf`

## Escopo

Esta classificação cobre os PDFs atualmente detectados na pasta `Livros/` por meio de `.gitattributes` e ponteiros Git LFS.

Os arquivos PDF estão versionados via Git LFS. Nesta etapa, o conector GitHub retornou os ponteiros LFS, não o conteúdo binário completo dos PDFs. Portanto, a classificação abaixo é **preliminar**, baseada em nome do arquivo, caminho, tamanho e metadados LFS. A análise profunda de conteúdo, OCR, páginas, sumário, entidades e extração mecânica exigirá acesso ao binário real do PDF.

## PDFs detectados

| Arquivo | Caminho | Tamanho LFS | Classificação preliminar | Prioridade | Status |
|---|---|---:|---|---|---|
| Neokosmos-biblioteca-elfica.pdf | `Livros/Neokosmos-biblioteca-elfica.pdf` | 123.311.840 bytes | Livro/cenário ou suplemento temático; provável conteúdo de ambientação, povos, cultura, magia e/ou regras élficas | Alta | Precisa baixar binário LFS |
| Grimorio.pdf | `Livros/Grimorio.pdf` | 117.577.520 bytes | Grimório; provável catálogo de magias, rituais, poderes sobrenaturais, escolas, custos e efeitos | Alta | Precisa baixar binário LFS |
| Guia de Itens Mágicos.pdf | `Livros/Guia de Itens Mágicos.pdf` | 116.125.075 bytes | Catálogo de itens mágicos; provável lista de artefatos, propriedades, raridade, efeitos e requisitos | Alta | Precisa baixar binário LFS |

## Estratégia de extração recomendada

### 1. `Grimorio.pdf`

Provável melhor candidato para o primeiro schema mecânico.

Entidades esperadas:

```txt
magia
ritual
escola_magica
poder_sobrenatural
tabela_magica
regra_de_conjuracao
```

Campos prováveis:

```txt
nome
tipo
escola/categoria
custo
requisito
tempo_de_execucao
alcance
duracao
alvo/area
resistencia/teste
efeito
fonte_pagina
```

### 2. `Guia de Itens Mágicos.pdf`

Bom candidato para o schema de itens.

Entidades esperadas:

```txt
item_magico
artefato
arma_magica
armadura_magica
consumivel
reliquia
tabela_de_itens
```

Campos prováveis:

```txt
nome
tipo
categoria
raridade
preco/custo
requisito
ativacao
efeito
restricoes
fonte_pagina
```

### 3. `Neokosmos-biblioteca-elfica.pdf`

Provável suplemento de ambientação e/ou biblioteca temática.

Entidades esperadas:

```txt
lore
local
povo/cultura
npc
organização
regra_opcional
magia/item específico
```

Campos prováveis:

```txt
nome
tipo
categoria
descricao
relacoes
ganchos
conteudo_mecanico_relacionado
fonte_pagina
```

## Bloqueio técnico atual

Os arquivos são Git LFS. O ponteiro LFS contém `oid sha256` e `size`, mas não contém o PDF em si. Para classificar o conteúdo de verdade, é necessário uma das opções abaixo:

1. disponibilizar os PDFs diretamente no chat;
2. permitir download do conteúdo LFS bruto pelo conector;
3. adicionar ao repositório uma extração textual gerada localmente em `processed/text/`;
4. executar localmente um pipeline com `git lfs pull` e commitar apenas os textos extraídos e metadados, não necessariamente os PDFs.

## Próximo lote possível

Assim que o conteúdo PDF real estiver acessível, o processamento por lote deve seguir esta ordem:

```txt
1. detectar OCR/texto selecionável;
2. extrair texto página a página;
3. separar blocos por título/seção;
4. classificar blocos por tipo de entidade;
5. gerar JSON candidato;
6. validar por schema;
7. criar relatório de revisão.
```
