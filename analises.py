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



# 1.2 Existe diferença entre a taxa de conversão do grupo controle  vs. grupo de desconto?


'''taxa_conversao_grupo = pd.read_sql_query(query, con= engine)
print(taxa_conversao_grupo)'''

# 1.3 Qual segmento de compra (Higiene Pessoal e Cuidados, Livros, Acessórios, Computação.) converte mais?


# 2. Segmentação de Clientes:
# 2.1 Como a idade ou gênero influencia a conversão?



# 2.2 Existe uma relação entre a idade do cliente e o valor médio do pedido?

# 2.3 Os clientes do grupo controle gastam mais do que os do grupo de intervenção?

'''
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
'''
