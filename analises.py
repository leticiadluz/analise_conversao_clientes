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

# 2. Segmentação de Clientes:
# 2.1. Qual segmento de compra (Higiene Pessoal e Cuidados, Livros, Acessórios, Computação.) converte mais?
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

# 2.2 Como a idade ou gênero influencia a conversão?