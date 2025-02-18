# Análise de Conversão de Clientes com Teste A/B, DBT e Power BI

## Resumo

## Introdução

Empresas de e-commerce frequentemente buscam maneiras de aumentar a conversão de 
clientes. Uma abordagem comum é o uso de campanhas de e-mail com descontos. 
Mas será que essas ofertas realmente influenciam a taxa de conversão? 

Para responder a essas perguntas, criamos um cenário hipotético no qual 
uma empresa de e-commerce que vende produtos variados decidiu testar o 
impacto de uma campanha promocional. A empresa ofereceu um voucher de 15% 
de desconto para compras acima de R$ 200 e utilizou um Teste A/B para avaliar 
sua eficácia.

Para garantir uma análise robusta, utilizamos um pipeline completo de DBT 
para transformação dos dados, SQL Server para armazenamento e Power BI 
para visualização dos resultados.


## 2. Visão geral de alguns conceitos:

Para entender a abordagem do projeto, é essencial compreender alguns conceitos-chave:

- **Teste A/B:** Um Teste A/B compara dois grupos:
    - **Grupo de Controle:** Clientes que não receberam o desconto.
    - **Grupo de Intervenção:** Clientes que receberam o desconto de 15%.

Se houver uma diferença significativa entre as taxas de conversão dos grupos, 
podemos inferir o impacto da campanha.

### 2.1. Pipeline de Dados

O pipeline do projeto segue estas etapas:
- **Extração e Armazenamento:** Os dados são carregados no SQL Server.
- **Transformação no DBT:** O DBT será utilizado para transformar e preparar os dados, 
facilitando a análise e respondendo às perguntas de negócios..
- **Análise Estatística no Python:** Realizamos o teste A/B para validar os resultados.
- **Visualização no Power BI:** Criamos dashboards interativos para tomada de decisão, 
com versionamento para acompanhar atualizações e manter a rastreabilidade das análises.

## 3. Visão geral e preparação dos dados

- Os dados foram gerados sintéticamente para simular um cenário de um e-commerce. 
As tabelas principais incluem:
    - **Dim_Clientes:** Dados sobre características e segmento de cada cliente.
    - **Dim_Segmentos:** Classificação dos diferentes segmentos de compra.
    - **Fato_Conversoes:** Registro dos clientes dos grupos de controle e intervenção, 
    indicando se realizaram uma conversão.
    - **Fato_Orders:** Informações detalhadas sobre os pedidos efetuados.

### 3.1  Carregamento dos dados no SQL Server (verificar)

As tabelas são criadas no SQL Server antes do carregamento dos arquivos CSV. 
Em seguida, os dados são inseridos utilizando BULK INSERT, COPY ou ferramentas 
gráficas do SSMS.

### 3.2. Modelagem no DBT (verificar)

Criamos modelos para transformar e consolidar os dados, incluindo a tabela 
ab_test_analysis, que une todas as informações necessárias.

### 3.3 Teste Estatístico no Python (verificar)

Rodamos um Teste Z para proporções para verificar se há diferença significativa 
entre os grupos:

### 3.4. Visualização no Power BI (verificar)

Criamos dashboards para visualizar as métricas, incluindo:
    - Taxa de Conversão por Grupo (Controle vs. Intervenção)
    - Análise de Receita Gerada pela Campanha
    - Segmentação de Clientes por Conversão

Esses dashboards serão versionados para acompanhar melhorias e novas necessidades 
de análise.

# 4. Análise dos Resultados