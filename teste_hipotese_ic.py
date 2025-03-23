from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep

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


query = '''
SELECT converted, test_group
FROM fact_conversions
'''
df_teste_hipotese = pd.read_sql_query(query, con = engine)
print(df_teste_hipotese)


conversao = df_teste_hipotese.groupby('test_group')['converted'].agg(['sum', 'count'])
print(conversao)


conversoes_teste = conversao.query('test_group == 1')['sum'].values[0]
total_teste = conversao.query("test_group == 1")['count'].values[0]

conversoes_controle = conversao.query('test_group == 0')['sum'].values[0]
total_controle = conversao.query('test_group == 0')['count'].values[0]


stat, p_value = proportions_ztest(
    [conversoes_teste, conversoes_controle],  
    [total_teste, total_controle],            
    alternative= 'two-sided') #teste bilateral


conf_int = confint_proportions_2indep(
    count1=conversoes_teste, 
    nobs1=total_teste, 
    count2=conversoes_controle, 
    nobs2=total_controle, 
    method="wald"  
)

print(f'Estatística Z: {stat:.4f}')
print(f'Valor-p: {p_value}')
print(f'Intervalo de Confiança de 95%: ({conf_int[0]:.4f}, {conf_int[1]:.4f})')
