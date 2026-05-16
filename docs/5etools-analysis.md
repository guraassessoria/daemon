# Analise Do 5e.tools

Fontes consultadas:

- https://5e.tools/
- https://5e.tools/bestiary.html
- https://5e.tools/spells.html
- https://5e.tools/items.html
- https://github.com/5etools-mirror-3/5etools-src/blob/main/CONTRIBUTING.md

## Principios observados

O 5e.tools funciona como uma suite de referencia, nao como uma biblioteca linear. A pagina inicial separa o conteudo por publico e uso: jogadores, regras e mestres. As secoes principais de D&D 5e incluem especies, classes, talentos, opcoes, backgrounds, itens, magias, gerador de atributos, aventuras, livros, glossario de regras, condicoes, bestiario, tela do mestre, gerador de tesouro e calculadora de desafio.

As paginas de entidade seguem um padrao recorrente:

- lista pesquisavel a esquerda;
- painel de detalhes a direita;
- filtros por campos importantes;
- coluna de fonte;
- modo tabela/impressao quando aplicavel;
- dados separados da interface;
- conteudo referenciado por fonte abreviada.

## Adaptacao Para Daemon/Trevas

As categorias de D&D 5e nao devem ser copiadas. A adaptacao correta e manter o padrao de experiencia do 5e.tools e trocar a ontologia para o vocabulario Daemon:

- `Livros`: todos os PDFs/DOCX como fontes.
- `Regras centrais`: sistema basico, testes, dano, evolucao e mecanicas gerais.
- `Atributos e pericias`: atributos, pericias, especializacoes e aplicacoes de teste.
- `Combate`: iniciativa, ataque, defesa, dano, armas, manobras e regras taticas.
- `Personagens`: kits, classes, caminhos, aprimoramentos, vantagens, desvantagens, poderes e racas.
- `Magia e poderes`: caminhos de magia, rituais, grimorios, poderes cabalisticos, fe, vodu, magia negra, psiquismo e efeitos sobrenaturais.
- `Itens e equipamentos`: armas, armaduras, itens magicos, equipamentos, veiculos e objetos.
- `Criaturas e NPCs`: monstros, demonios, anjos, vampiros, lobisomens, youkais, mortos-vivos, entidades e antagonistas.
- `Ambientacao`: Trevas, Arkanun, Inquisicao, Vaticano, mitologias, religioes, regioes, cronologias e organizacoes.
- `Aventuras`: campanhas, modulos, one-shots e cenarios prontos.
- `Tabelas e geradores`: tabelas aleatorias, geradores de criaturas, itens, encontros e material de apoio.

## Funcionalidades recomendadas

- busca global por nome e texto;
- filtros por categoria, fonte, sistema, mundo/cenario, pagina e tags;
- detalhe de entidade com referencia de origem;
- indice por livro;
- relacoes entre entidades, por exemplo poder -> caminho, criatura -> tipo, item -> categoria, kit -> requisitos;
- import/export em JSON;
- validacao por schema para evitar dados inconsistentes;
- extracao rastreavel: cada entidade deve guardar `source`, `page`, `confidence` e `extractionMethod`.
