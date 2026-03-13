# Exemplo-de-um-Banco-de-Dados-baseado-em-grafos
Será disponibilizado um banco de dados baseado em grafos com uma semente e consultas padrões que podem ser realizadas na sua máquina nativa. 
O banco de dados é escrito em cypher, uma lingugagem construida pela Neo4j para seus bancos de dados(BD), este projeto foi pensado para exemplificar um serviço de streaming com um BD baseado em grafos demonstrado a vsersatilidade e poder dos grafos.


## Abaixo apresentamos uma documentação sobre o banco de dados, cuja finalidade está em exemplificar como seria a construção de banco de serviço de streaming.

### Introdução
O projeto foi concebido para responder um desafio sobre um banco de dados baseado em grafos para um serviço de streaming, em resposta ao desafio o seguinte repositório foi construído. O banco tem uma semente com 30 nós de cada tipo, sendo os tipos elencados em actors, directors, movies, series, users e genres com seus relacionamentos de acted_in, directed, in_genre e watched. Como foi utilizado o neo4j a semente está escrita em cypher.

### Implementação 

```
Você pode baixar o software da neo4j, a versão desktop, ou utilizar a versão online do produto.
```

A documentação pode ser acessada por aqui, [documentação neo4j](https://neo4j.com/docs/).

### DB

O banco apresenta a seguinte representação gráfica:

![imagem](https://keep.google.com/u/0/media/v2/1icxbkYq6CXtd8tLDHgU5YQaSQMHZY_IiVvMQH7bAvCRIG7A6fcqLmCosSh6Tpuc/1Bk0Bi_bAHktGOU8bFuqWN9ePvT7xKFmvIqyaHTok9VUx_V36lpomQqBTiQYz3Q?sz=512&accept=image%2Fgif%2Cimage%2Fjpeg%2Cimage%2Fjpg%2Cimage%2Fpng%2Cimage%2Fwebp)
