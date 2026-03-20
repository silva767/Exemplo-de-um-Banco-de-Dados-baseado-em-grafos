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

Com o diferencial de conectar dados por relações, os grafos, se tornam especialmente úteis para modelar serviços de plataformas de música, locais onde relações entre as entidades são prepoderantes, tais como lançar uma música, curtir uma música, criar uma playlist, seguir outra pessoa, etc. Com isso em mente e nas possiblidades que surgem como recomendações personalizadas, descobertas de gostos e tendências, abaixo disponibilizamos um modelo para tal caso e com figura que demonstra os nós e as relações de tal modelo.

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1AmdYAzBAUS-KAER0DJTFqQCoa9a7x2Qi" 
       width="560">
</p>

### Modelagem do banco e de suas entidades

As entidades e suas relações serão estas:

|Entidades | Relações |
|--------|---------|
|Usuários | Curtiu(entre pessoas e músicas) |
|Artistas | Segue (entre pessoas) |
|Músicas | Pertence (música e gênero) |
|Playlist | Criou (pessoa e playlist) |
|Gêneros | Lançou (artista e música) |

Um arquivo com dados para um exemplo de semente são disponibilizados no [arquivo](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/Exemplo_semente_m%C3%BAsica), nele já é possível visualizar diversos caminhos e aplicar algumas consultas, mesmo sendo um modelo simplificado, e que demonstram o poder dos grafos em situações propicias para tal modelagem.

Nesse exemplo a semente similar a realidade será disponibilizada no formato LOAD CSV, um formato que simplica a carga nos bancos de dados, pois são dispostos no formato:

```
musicas.csv
id,titulo,ano,duracao
1,Envolver,2022,180
2,Gods Plan,2018,198
3,Shake It Off,2014,242
4,Blinding Lights,2020,200
5,Hear Me Now,2016,190
6,Infiel,2016,210
7,Yellow,2000,270
```
que permite a carga rápida com o uso de outro arquivo csv:

```
LOAD CSV WITH HEADERS FROM 'file:///musicas.csv' AS row
CREATE (:Musica {
   id: toInteger(row.id),
   titulo: row.titulo,
   ano: toInteger(row.ano),
   duracao: toInteger(row.duracao)
});
```
vale lembrar que os arquivos devem ser colocados na pasta import, ao utilizar o Neo4j.

- Arquicos da relações:

|Entidades | Relações |
|--------|---------|
|[users](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/users.csv) |  [usuario_segue](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/usuario_segue.csv) & [usuario_segue_artista](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/usuario_segue_artista.csv) |
|[artistas](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/artistas.csv) | [artista_lancou](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/artista_lancou.csv)  |
|[musicas](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/musicas.csv) | [usuario_curtiu](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/usuario_curtiu.csv) |
|[playlist](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/playlists.csv) | [playlist_contem_musica](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/playlist_contem_musica.csv) |
|[generos](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/generos.csv) | [artista_genero](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/artista_genero.csv) |

- E o arquivo para o [load csv](https://github.com/silva767/Exemplo-de-um-Banco-de-Dados-baseado-em-grafos/blob/main/criar_rela%C3%A7%C3%B5es.csv).

E como exemplo do poder dos grafos nesse exemplo abaixo são apresentadas algumas consultas possíveis, com as demais consultas sendo disponibilizadas no arquivo xxxx.

```
```

### BDGraph de uma rede social

Agora tomamos como exemplo uma rede social, o modelamento dela é interessante pois expressa bem o modelo de nós e relações entre eles, visto que as redes sociais são uma das manifestações mais diretas de um grafo. Tomaremos como plataforma o Instagram e utilizaremos um dataset disponível no [Kaggle](https://www.kaggle.com/).

Para baixar o dataset são disponibilizadas duas algumas opções, o arquivo .zip e a utilização da biblioteca kagglehub. Abaixo está disponível a segunda opção.

```
import kagglehub

path = kagglehub.dataset_download("kundanbedmutha/instagram-analytics-dataset")
print(path)
```
Nesse formato é possível integrar Python com a API do Neo4j que permite manipular os grafos pelo ambiente de programação.

Com o dataset em mãos definimos os seguintes nós e relações para serem formados xxx
