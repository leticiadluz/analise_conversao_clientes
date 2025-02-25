from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Variáveis de ambiente
load_dotenv()
dbname = os.getenv('dbname')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')

connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(connection_string)

try:
    with engine.begin() as conn:
        print('Conexão bem-sucedida!')
except Exception as e:
    print(f"Erro na conexão: {e}")

# 1. Análise de Conversão:
# 1.1 Qual a taxa de conversão geral dos clientes?

query = '''
SELECT ROUND((SUM(converted)*100.0)/ count(*), 2) AS conversao_geral
FROM fato_conversoes
'''
taxa_conversao_geral = pd.read_sql_query(query, con=engine)
print(taxa_conversao_geral)

# 1.2 Existe diferença entre a taxa de conversão do grupo controle  vs. grupo de desconto?
query = '''SELECT control_group, ROUND((SUM(converted) * 100.0)/ COUNT(*),2) AS conversao_grupo
FROM fato_conversoes
GROUP BY control_group'''

taxa_conversao_grupo = pd.read_sql_query(query, con= engine)
print(taxa_conversao_grupo)

# 1.3 Qual segmento de compra (Higiene Pessoal e Cuidados, Livros, Acessórios, Computação.) converte mais?
query = '''SELECT dim_segmentos.segment_name,
ROUND(SUM(converted) * 100.0 / count(*), 2) AS conversao_segmento
FROM fato_conversoes
LEFT JOIN dim_clientes ON
fato_conversoes.customer_id = dim_clientes.customer_id
LEFT JOIN dim_segmentos ON
dim_clientes.segment_id = dim_segmentos.segment_id 
GROUP BY dim_segmentos.segment_name
ORDER BY conversao_segmento DESC'''

taxa_conversao_segmento = pd.read_sql_query(query, con = engine)
print(taxa_conversao_segmento)

# 2. Segmentação de Clientes:
# 2.1 Como a idade ou gênero influencia a conversão?

query = '''SELECT dim_clientes.gender,
ROUND(SUM(CONVERTED) *100.0 / COUNT(*), 2) AS conversao_genero
FROM fato_conversoes

LEFT JOIN dim_clientes ON
dim_clientes.customer_id = fato_conversoes.customer_id
GROUP BY dim_clientes.gender'''

taxa_conversao_genero = pd.read_sql_query(query, con = engine)
print(taxa_conversao_genero)

query = '''SELECT 
ROUND(SUM(CONVERTED) *100.0 / COUNT(*), 2) AS conversao_idade,
CASE 
WHEN dim_clientes.age BETWEEN 18 AND 28 THEN  'Geracao_Z'
WHEN dim_clientes.age BETWEEN 29 AND 44 THEN 'Millennials'
WHEN dim_clientes.age BETWEEN 45 AND 60 THEN 'Geracao_X'
ELSE 'Boomers'
END AS idade_geracoes
FROM fato_conversoes

LEFT JOIN dim_clientes ON
dim_clientes.customer_id = fato_conversoes.customer_id
GROUP BY idade_geracoes'''

taxa_conversao_idade = pd.read_sql_query(query, con = engine)
print(taxa_conversao_idade)

# 2.2 Existe uma relação entre a idade do cliente e o valor médio do pedido?
query = '''SELECT ROUND(AVG(fato_orders.order_value),2) AS media_pedido,
CASE 
WHEN dim_clientes.age BETWEEN 18 AND 28 THEN  'Geracao_Z'
WHEN dim_clientes.age BETWEEN 29 AND 44 THEN 'Millennials'
WHEN dim_clientes.age BETWEEN 45 AND 60 THEN 'Geracao_X'
ELSE 'Boomers'
END AS idade_geracoes
FROM fato_orders
LEFT JOIN dim_clientes ON
dim_clientes.customer_id = fato_orders.customer_id
GROUP BY idade_geracoes'''

valor_medio_pedido_idade = pd.read_sql_query(query, con = engine)
print(valor_medio_pedido_idade)
# 2.3 Os clientes do grupo controle gastam mais do que os do grupo de intervenção?

query = '''SELECT
SUM(fato_orders.order_value) AS valor_pedido_grupo,
fato_conversoes.control_group
FROM fato_orders

LEFT JOIN fato_conversoes ON
fato_conversoes.customer_id = fato_orders.customer_id
GROUP BY fato_conversoes.control_group'''

valor_pedido_grupos = pd.read_sql(query, con = engine)
print(valor_pedido_grupos)


output_file = "relatorio_analise_conversao.xlsx"

df_dict = {
    "Taxa Conversão Geral": taxa_conversao_geral,
    "Taxa Conversão Grupo": taxa_conversao_grupo,
    "Taxa Conversão Segmento": taxa_conversao_segmento,
    "Taxa Conversão Gênero": taxa_conversao_genero,
    "Taxa Conversão Idade": taxa_conversao_idade,
    "Valor Médio Pedido Idade": valor_medio_pedido_idade,
    "Valor Pedido Grupo": valor_pedido_grupos
}


with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    for sheet_name, df in df_dict.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

