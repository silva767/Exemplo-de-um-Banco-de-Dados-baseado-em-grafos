# Exemplos-de-um-Bancos-de-Dados-baseados-em-grafos
Serão disponibilizados exemplos diversos de banco de dados baseado em grafos com sementes e consultas padrões que podem ser realizadas na sua máquina nativa. 
O banco de dados é escrito em cypher, uma lingugagem construida pela Neo4j para seus bancos de dados(BD), este projeto foi pensado para exemplificar diversos sitemas e serviços com BD's baseados em grafos demonstrando a vsersatilidade e poder dos grafos.


## Abaixo apresentamos uma documentação sobre o banco de dados, cuja finalidade está em exemplificar como seria a construção de banco de serviço de streaming.

### Introdução
O projeto foi concebido para responder um desafio sobre um banco de dados baseado em grafos para um serviço de streaming, em resposta ao desafio o seguinte repositório foi construído. O banco tem uma semente com 30 nós de cada tipo, sendo os tipos elencados em actors, directors, movies, series, users e genres com seus relacionamentos de acted_in, directed, in_genre e watched. Como foi utilizado o neo4j a semente está escrita em cypher.

### Implementação 

```
Você pode baixar o software da neo4j, a versão desktop, ou utilizar a versão online do produto.
```
A versão desktop apresenta algumas exigências de hardware que podem ser acessadas na página do produto, enquanto é possível utilizar a versão free para o exemplo em questão sem maiores dificuldades.
A documentação do neo4j e da linguagem cypher pode ser acessada por aqui, [documentação neo4j](https://neo4j.com/docs/).

### DBGraph de um serviço de streaming 

O banco apresenta a seguinte representação gráfica:

![Grafo do sistema](https://drive.google.com/uc?export=view&id=1eqGFLFoxBTq2tuef39d61BDjABquopie)

A formatação segue como a descrita e pode ser acessada uma semente exemplo no arquivo [Exemplo de semente](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/Exemplo%20de%20semente).
A escrita em cypher é similar ao SQL e apresenta sintaxe direta, intuitiva e fluída com palavras reservadas para a criação dos nós, relações e demais consultas. 

Exemplos de consultas possíveis no DB - [Consultas cypher](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/Consultas%20cypher).
No arquivo estão dispostas 10 exemplos de consultas, que buscar responder diferentes perguntas ligadas ao escopo do banco.

Semente inicial utilizada no teste - [Semente](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/Consultas%20cypher). 
No arquivo é disponibilizado uma semente com 180 nós iniciais, para usuários, atores, diretores, filmes e séries, inspirados em filmes e atores reais.

### DBGraph de um serviço de uma plataforma de música

Com o diferencial de conectar dados por relações, os grafos, se tornam especialmente úteis para modelar serviços de plataformas de música, locais onde relações entre as entidades são prepoderantes, tais como lançar uma música, curtir uma música, criar uma playlist, seguir outra pessoa, etc. Com isso em mente e nas possiblidades que surgem como recomendações personalizadas, descobertas de gostos e tendências, abaixo disponibilizamos um modelo para tal caso.

### Modelagem do banco e de suas entidades

As entidades e suas relações serão estas:

- Usuários
- Artistas
- Músicas
- Playlist
- Gêneros

- Pertence
- Curtiu
- Segue
- Criou
- Lançou

Um arquivo com dados para um exemplo de semente são disponibilizados no arquivo xxxx, nele já é possível visualizar diversos caminhos e aplicar algumas consultas, mesmo sendo um modelo simplificado.
