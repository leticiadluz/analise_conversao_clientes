from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import pandas as pd

# Variáveis de ambiente
load_dotenv()
dbname = os.getenv('dbname')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')

connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'
engine = create_engine(connection_string)

try:
    with engine.begin() as conn:
        print('Conexão bem-sucedida!')
except Exception as e:
    print(f'Erro na conexão: {e}')

# 1. Análise de Conversão:
# 1.1 Qual a taxa de conversão geral dos clientes?
query = '''
SELECT
ROUND(AVG(converted)* 100.0, 2) as conversao_geral
FROM fact_conversions
'''

conversao_geral = pd.read_sql_query(query, con = engine)
print(conversao_geral)

# 1.2 Existe diferença entre a taxa de conversão do grupo controle  vs. grupo de teste?
query = '''
SELECT
ROUND(AVG(converted)* 100.0, 2) as conversao_teste
FROM fact_conversions
WHERE test_group = 1
'''

conversao_teste = pd.read_sql_query(query, con = engine)
print(conversao_teste)

query = '''
SELECT
ROUND(AVG(converted)* 100.0, 2) as conversao_controle
FROM fact_conversions
WHERE test_group = 0
'''

conversao_controle = pd.read_sql_query(query, con = engine)
print(conversao_controle)

# 1.3 Qual canal de comunicação apresenta a maior taxa de conversão?
query = '''
SELECT
ROUND(AVG(converted)* 100.0, 2) as conversao_email
FROM fact_conversions
WHERE communication = 'Email'
'''

conversao_email = pd.read_sql_query(query, con = engine)
print(conversao_email)

query = '''
SELECT
ROUND(AVG(converted)* 100.0, 2) as conversao_whats
FROM fact_conversions
WHERE communication = 'WhatsApp'
'''

conversao_whats = pd.read_sql_query(query, con = engine)
print(conversao_whats)

# 2. Segmentação de Clientes:
# 2.1 De que forma idade, gênero ou valor do ticket médio impactam a taxa de conversão?  
query = '''
SELECT 
CASE WHEN age BETWEEN '18' AND '25' THEN '18-25'
WHEN age BETWEEN '26' AND '45' THEN '26-45'
WHEN age BETWEEN '46' AND '60' THEN '46-60'
ELSE 'Mais de 60'
END AS faixa_etaria,
ROUND(AVG(converted) * 100.0, 2) AS conversao_idade
FROM fact_conversions
LEFT JOIN dim_clients ON
dim_clients.customer_id = fact_conversions.customer_id
GROUP BY faixa_etaria
'''
conversao_idade = pd.read_sql_query(query, con = engine)
print(conversao_idade)


query = '''
SELECT 
gender,
ROUND(AVG(converted) * 100.0, 2) AS conversao_genero
FROM fact_conversions
LEFT JOIN dim_clients ON
dim_clients.customer_id = fact_conversions.customer_id
GROUP BY gender
'''

conversao_genero = pd.read_sql_query(query, con = engine)
print(conversao_genero)

query = '''
SELECT 
average_ticket,
ROUND(AVG(converted) * 100.0, 2) AS conversao_ticket_medio
FROM fact_conversions
LEFT JOIN dim_clients ON
dim_clients.customer_id = fact_conversions.customer_id
GROUP BY average_ticket
'''

conversao_ticket_medio = pd.read_sql_query(query, con = engine)
print(conversao_ticket_medio)

# 2.2 Como idade influencia o valor médio do pedido?
query = '''
SELECT 
CASE WHEN age BETWEEN '18' AND '25' THEN '18-25'
WHEN age BETWEEN '26' AND '45' THEN '26-45'
WHEN age BETWEEN '46' AND '60' THEN '46-60'
ELSE 'Mais de 60'
END AS faixa_etaria,
ROUND(AVG(order_value), 2) AS ticket_medio
FROM fact_orders
LEFT JOIN dim_clients ON
dim_clients.customer_id = fact_orders.customer_id
GROUP BY faixa_etaria
'''
ticket_medio_idade = pd.read_sql_query(query, con = engine)
print(ticket_medio_idade)

# 2.3 Os clientes do grupo de teste apresentam um ticket médio maior do que os do grupo controle?

query = '''
SELECT 
test_group,
ROUND(AVG(order_value), 2) AS ticket_medio
FROM fact_orders
LEFT JOIN fact_conversions ON
fact_conversions.customer_id = fact_orders.customer_id
GROUP BY test_group
'''
ticket_medio_conversao = pd.read_sql_query(query, con = engine)
print(ticket_medio_conversao)


with pd.ExcelWriter('analise_conversao.xlsx', engine='xlsxwriter') as writer:
    analise_inicial = pd.concat([conversao_geral, conversao_teste, conversao_controle, conversao_email, conversao_whats])
    
    analise_inicial.to_excel(writer, sheet_name='analise_conversao', index=False)
    conversao_genero.to_excel(writer, sheet_name='conversao_genero', index=False)
    conversao_idade.to_excel(writer, sheet_name='conversao_faixa_etaria', index=False)
    conversao_ticket_medio.to_excel(writer, sheet_name='conversao_ticket_medio', index=False)
    ticket_medio_idade.to_excel(writer, sheet_name='ticket_medio_idade', index=False)
    ticket_medio_conversao.to_excel(writer, sheet_name='ticket_medio_teste', index=False)

print("Arquivo Excel 'analise_conversao.xlsx' criado com sucesso!")

