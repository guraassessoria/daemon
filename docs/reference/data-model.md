# Modelo De Dados

## Fonte

Cada arquivo em `Livros/` vira uma fonte em `data/index/sources.json`.

Campos principais:

- `id`: identificador estavel derivado do nome do arquivo.
- `title`: titulo inferido do nome.
- `path`: caminho relativo do arquivo original.
- `extension`: `.pdf` ou `.docx`.
- `sizeBytes`: tamanho do arquivo.
- `sha256`: hash para detectar alteracoes.
- `categoryHints`: categorias provaveis pelo nome e pelo texto.
- `textStatus`: `pending`, `ok`, `failed` ou `partial`.

## Entidade

Entidades extraidas ficam em `data/entities/<category>.json`.

Campos comuns:

- `id`
- `name`
- `category`
- `source`
- `page`
- `entries`
- `tags`
- `confidence`
- `extractionMethod`

## Areas

Areas ficam em `data/areas/<area>.json` e funcionam como a camada de navegacao inspirada no 5e.tools, mas adaptada ao Daemon/Trevas.

Cada area contem:

- `entities`: itens ja curados em `data/entities`.
- `sourceParts`: blocos e secoes dos livros prontos para seguir.
- `readySourceCount`: quantidade de fontes boas usadas na montagem.

O resumo geral fica em `data/index/area-summary.json`.

Areas atuais:

- `fontes`
- `regras_base`
- `atributos_pericias`
- `combate`
- `aprimoramentos`
- `kits`
- `classes`
- `racas`
- `linhagens`
- `poderes`
- `magias`
- `rituais`
- `itens_equipamentos`
- `criaturas_npcs`
- `cenarios_lore`
- `aventuras`
- `tabelas`

## Categorias

- `core_rule`
- `attribute_skill`
- `combat`
- `character_option`
- `kit_class`
- `race_lineage`
- `power_magic`
- `ritual_spell`
- `item_equipment`
- `creature_npc`
- `setting_lore`
- `adventure`
- `table_generator`
- `source`

## Estrategia De Extracao

1. Inventario dos arquivos.
2. Extracao de texto bruto.
3. Segmentacao por pagina/secao.
4. Deteccao de candidatos por padroes de titulo e palavras-chave.
5. Normalizacao em JSON.
6. Revisao humana dos itens de baixa confianca.

Esse fluxo evita tratar PDFs escaneados, DOCX e livros diagramados como se fossem todos iguais.
