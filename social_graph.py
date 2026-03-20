import kagglehub
import pandas as pd
from neo4j import GraphDatabase

# =========================
# 1. Download do dataset
# =========================
path = kagglehub.dataset_download("kundanbedmutha/instagram-analytics-dataset")

csv_file = f"{path}/instagram_data.csv"
df = pd.read_csv(csv_file)

# =========================
# 2. Conexão Neo4j
# Aqui você deve inserir seu usuário e senha do seu servidor da Neo4j 
# =========================
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "password"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

# =========================
# 3. Criar constraints e índices
# =========================
def create_constraints(tx):
    queries = [
        # Unicidade principal
        "CREATE CONSTRAINT account_id IF NOT EXISTS FOR (a:Account) REQUIRE a.account_id IS UNIQUE",
        "CREATE CONSTRAINT post_id IF NOT EXISTS FOR (p:Post) REQUIRE p.post_id IS UNIQUE",

        # Dimensões
        "CREATE CONSTRAINT media_type_unique IF NOT EXISTS FOR (m:MediaType) REQUIRE m.type IS UNIQUE",
        "CREATE CONSTRAINT category_unique IF NOT EXISTS FOR (c:Category) REQUIRE c.name IS UNIQUE",
        "CREATE CONSTRAINT traffic_unique IF NOT EXISTS FOR (t:TrafficSource) REQUIRE t.source IS UNIQUE",
        "CREATE CONSTRAINT day_unique IF NOT EXISTS FOR (d:Day) REQUIRE d.name IS UNIQUE",

        # Month (composto)
        "CREATE CONSTRAINT month_unique IF NOT EXISTS FOR (m:Month) REQUIRE (m.year, m.month) IS UNIQUE",

        # Índices
        "CREATE INDEX post_engagement_index IF NOT EXISTS FOR (p:Post) ON (p.engagement_rate)",
        "CREATE INDEX post_virality_index IF NOT EXISTS FOR (p:Post) ON (p.viral_score)",
        "CREATE INDEX post_impressions_index IF NOT EXISTS FOR (p:Post) ON (p.impressions)",
        "CREATE INDEX post_date_index IF NOT EXISTS FOR (p:Post) ON (p.date_time)",
        "CREATE INDEX account_followers_index IF NOT EXISTS FOR (a:Account) ON (a.followers)",

        # Existência
        "CREATE CONSTRAINT post_engagement_exists IF NOT EXISTS FOR (p:Post) REQUIRE p.engagement_rate IS NOT NULL"
    ]

    for q in queries:
        tx.run(q)

# =========================
# 4. Inserção em batch
# Faz a inserção em pacotes, para não travar e tornar lento o processo e permite que nenhuma carga seja perdida em ocorrências nada fortuitas.
# =========================
def create_batch(tx, rows):
    tx.run("""
    UNWIND $rows AS row

    WITH row,
         datetime(row.post_date) AS dt

    // Account
    MERGE (a:Account {account_id: row.account_id})
    SET a.account_type = coalesce(row.account_type, "unknown"),
        a.followers = coalesce(toInteger(row.followers), 0)

    // Post
    MERGE (p:Post {post_id: row.post_id})
    SET p.likes = coalesce(toInteger(row.likes), 0),
        p.comments = coalesce(toInteger(row.comments), 0),
        p.shares = coalesce(toInteger(row.shares), 0),
        p.saves = coalesce(toInteger(row.saves), 0),
        p.impressions = coalesce(toInteger(row.impressions), 0),
        p.engagement_rate = coalesce(toFloat(row.engagement_rate), 0.0),
        p.followers_gained = coalesce(toInteger(row.followers_gained), 0),
        p.caption_length = coalesce(toInteger(row.caption_length), 0),
        p.hashtags_count = coalesce(toInteger(row.hashtags_count), 0),
        p.date_time = dt,
        p.day = dt.day,
        p.viral_score = CASE 
            WHEN coalesce(toFloat(row.impressions),0) > 0 
            THEN (coalesce(toFloat(row.likes),0)*0.4 +
                  coalesce(toFloat(row.comments),0)*0.3 +
                  coalesce(toFloat(row.shares),0)*0.2 +
                  coalesce(toFloat(row.saves),0)*0.1)
                 / toFloat(row.impressions)
            ELSE 0 
        END

    // Month (nó)
    MERGE (mo:Month {year: dt.year, month: dt.month})

    // Dimensões
    # Dimensão é uma maneira de se referir à atributos categóricos reutilizáveis.
    MERGE (m:MediaType {type: coalesce(row.media_type, "unknown")})
    MERGE (c:Category {name: coalesce(row.category, "unknown")})
    MERGE (t:TrafficSource {source: coalesce(row.traffic_source, "unknown")})
    MERGE (d:Day {name: coalesce(row.day_of_week, "unknown")})

    // Relações
    MERGE (a)-[:POSTED]->(p)
    MERGE (p)-[:HAS_MEDIA_TYPE]->(m)
    MERGE (p)-[:IN_CATEGORY]->(c)
    MERGE (p)-[:FROM_TRAFFIC]->(t)
    MERGE (p)-[:POSTED_ON]->(d)
    MERGE (p)-[:POSTED_IN]->(mo)
    """, rows=rows)

# =========================
# 5. Execução
# =========================
BATCH_SIZE = 1000

with driver.session() as session:
    print("Criando constraints...")
    session.execute_write(create_constraints)

    print("Inserindo dados...")
    batch = []

    for _, row in df.iterrows():
        batch.append(row.to_dict())

        if len(batch) == BATCH_SIZE:
            session.execute_write(create_batch, batch)
            batch = []

    # restante
    if batch:
        session.execute_write(create_batch, batch)

driver.close()

print("Importação concluída com sucesso!")

# Criar um ordenamento de meses, possiblitando consultas temporais.
# Para que essa relação seja criada com êxito, o nó de meses deve ser criado primeiro.

def create_month_relationships(tx):
    tx.run("""
    MATCH (m:Month)
    WITH m ORDER BY m.year, m.month
    WITH collect(m) AS months

    UNWIND range(0, size(months)-2) AS i
    WITH months[i] AS m1, months[i+1] AS m2

    MERGE (m1)-[:NEXT]->(m2)
    """)
