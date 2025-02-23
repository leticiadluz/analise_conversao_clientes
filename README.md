# Análise de Conversão de Clientes com Teste A/B, SQL e Power BI

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
para transformação dos dados, PostgreSQL para armazenamento e Power BI 
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
- **Extração e Armazenamento:** Os dados são carregados no PostgreSQL.
- **Transformação dos Dados:** Integramos o banco de dados ao Python para executar as análises e 
transformações necessárias com linguagem SQL e responder às questões de negócio. Para isso, as tabelas serão 
unificadas, viabilizando a execução dos testes A/B e as análises no Power BI.
- **Análise Estatística no Python:** Aplicamos o teste A/B para validar os resultados.
- **Visualização no Power BI:** Desenvolvemos dashboards interativos para tomada de decisão, 
com versionamento para acompanhar atualizações e manter a rastreabilidade das análises.

## 3. Visão geral e preparação dos dados

- **Fonte de Dados:** 
Os dados foram gerados sinteticamente com base em instruções fornecidas ao chatgpt, 
detalhando as tabelas e colunas desejadas para simular um cenário de um e-commerce.
As tabelas principais incluem:
    - **Dim_Clientes:** Dados sobre características e segmento preferencial de compra de 
    cada cliente.
    - **Dim_Segmentos:** Classificação dos diferentes segmentos de compra.
    - **Fato_Conversoes:** Registro dos clientes dos grupos de controle e intervenção, 
    indicando se realizaram uma conversão.
    - **Fato_Orders:** Informações detalhadas sobre os pedidos efetuados.
    
Os dados gerados estão no formato CSV.
Antes do carregamento dos arquivos CSV, foram criadas as tabelas no **PostgreSQL**, 
garantindo que todas as chaves primárias (PK) e chaves estrangeiras (FK) estivessem 
corretamente definidas.
Após a criação das tabelas, os dados foram inseridos a partir de arquivos CSV.
Utilizamos a importação direta via interface gráfica no pgAdmin. 

## 4. Análises

### 4.1 Perguntas de Negócios

 Análise de Conversão:
    - Qual a taxa de conversão geral dos clientes?
    - Existe diferença entre a taxa de conversão do grupo controle vs. grupo de desconto?

Segmentação de Clientes:
    - Qual segmento de compra (Higiene Pessoal e Cuidados, Livros, Acessórios, Computação.) converte mais?
    - Como a idade ou gênero influencia a conversão?

Análise de Receita:
    - Qual a receita gerada pela campanha?
    - Qual é o ticket médio dos pedidos dos clientes que converteram?
    - Qual foi o ROI (Retorno sobre o Investimento) de cada campanha?

### Visualização no Power BI (verificar)

Criamos dashboards para visualizar as métricas, incluindo:
    - Taxa de Conversão por Grupo (Controle vs. Intervenção)
    - Análise de Receita Gerada pela Campanha
    - Segmentação de Clientes por Conversão

Esses dashboards serão versionados para acompanhar melhorias e novas necessidades 
de análise.

#  Análise dos Resultados