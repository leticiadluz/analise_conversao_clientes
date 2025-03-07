# Análise de Conversão de Clientes com Teste A/B, SQL e Power BI

## Resumo

## Introdução

Empresas de e-commerce frequentemente buscam maneiras de aumentar a conversão de 
clientes. Uma abordagem comum é o uso de campanhas de e-mail com descontos. 
Mas será que essa oferta realmente influencia a taxa de conversão? 

Para responder a essa pergunta, criamos um cenário hipotético no qual 
uma empresa de e-commerce que vende produtos variados decidiu testar o 
impacto de uma campanha promocional. A empresa ofereceu um voucher de 15% 
de desconto para compras acima de R$ 200 para um grupo selecionado de clientes e utilizou um Teste A/B para avaliar sua eficácia.

O teste A/B é uma metodologia de experimentação utilizada para comparar duas versões de uma variável (como um site, campanha de marketing ou funcionalidade de um produto) e determinar qual gera melhores resultados. Ele é amplamente aplicado em áreas como marketing digital, experiência do usuário (UX), design de produtos e ciência de dados.

O teste A/B envolve a seleção aleatória de clientes para garantir que os grupos sejam homogêneos a fim de evitar vieses que possam distorcer os resultados. Ele é ideal para realizar comparações, pois, por exemplo, comparar grupos com base no tempo pode não ser adequado. A sazonalidade pode influenciar os resultados, tornando comparações temporais menos confiáveis. Assim, o teste A/B permite avaliar, dentro do mesmo período, os efeitos de uma ação em comparação à ausência dela, proporcionando resultados mais precisos e isentos de vieses temporais.

Definição dos grupos:
- Grupo Controle: Recebe a versão original (sem mudanças).
- Grupo Variante: Recebe a versão modificada para testar o impacto da mudança.

São observadas métricas-chave, como taxa de conversão, tempo de permanência e número de cliques. Os resultados são analisados para verificar se a diferença entre os grupos é estatisticamente significativa. Se a variante apresentar melhor desempenho, a mudança pode ser implementada permanentemente.

### 1.1 Objetivo:
- O objetivo principal é verificar se o envio de um e-mail contendo um voucher promocional aumenta a taxa de conversão dos usuários em comparação com um e-mail sem voucher.
-  **Métrica de sucesso:** Taxa de conversão (compras realizadas após o recebimento do e-mail).

### 1.2 Visão geral de alguns conceitos:

a) **Teste de Hipótese:**  Um teste de hipótese 
é um procedimento estatístico usado para avaliar se há evidências 
suficientes nos dados para rejeitar uma suposição inicial (hipótese nula) sobre
 uma população. Desta forma, utilizamos um teste de hipótese para avaliar 
 a validade de uma afirmação (hipótese) sobre um parâmetro populacional, 
 com base em dados amostrais.

 b) **Hipótese Nula (H0):** A hipótese nula representa o estado 
 padrão ou **a suposição inicial sobre os dados**. 
 Ela assume que não há efeito, mudança ou diferença real. 
 O objetivo do teste é tentar refutar essa hipótese com base nos dados.
 Ela contém uma afirmação de igualdade: (=, ≤ , ≥).

 c) **Hipótese Alternativa (H1 ou Ha):** A hipótese alternativa é a afirmação 
 oposta à hipótese nula. Ela sugere que existe um efeito, 
 uma diferença ou uma mudança real nos dados, ela contradiz H0 (≠).

 d) **p-valor:** O p-valor é a probabilidade de observarmos um resultado tão 
 extremo quanto o encontrado na amostra, assumindo que a hipótese nula (H0) 
 seja verdadeira. Ou seja, qual a probabilidade 
 de encontrar uma diferença(entre os grupos) ou um valor mais extremo dado 
 que os grupos são iguais, dado que a diferença não existe. 

 e) **Nível de significância:** O nível de significância (α) é um valor 
 que define o quanto estamos dispostos a aceitar que um 
 resultado pode ter ocorrido por acaso ao realizar um teste de hipótese. 

 ### 1.3 Hipótese
- O envio de um e-mail com um voucher promocional aumentará a taxa de conversão
 em pelo menos X% em relação ao e-mail sem voucher.

### 1.4 Público Alvo 
- Homens e mulheres entre 18 e 70 anos.
- Que tenham realizado uma compra nos últimos três meses.
- Cuja última compra tenha sido de produtos dos seguintes segmentos: Higiene Pessoal e Cuidados, Livros, Acessórios ou Computação.


## 2. 

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

1. Análise de Conversão:  
    - Qual a taxa de conversão geral dos clientes?  
    - Existe diferença entre a taxa de conversão do grupo controle vs. grupo de desconto?
    - Qual segmento de compra (Higiene Pessoal e Cuidados, Livros, Acessórios, Computação.) converte mais?    

2. Segmentação de Clientes e comportamento de compra:  
    - Como a idade ou gênero influencia a conversão?  
    - Existe uma relação entre a idade do cliente e o valor médio do pedido?
    - Os clientes do grupo controle gastam mais do que os do grupo de intervenção?



### Visualização no Power BI (verificar)

Criamos dashboards para visualizar as métricas, incluindo:
    - Taxa de Conversão por Grupo (Controle vs. Intervenção)
    - Análise de Receita Gerada pela Campanha
    - Segmentação de Clientes por Conversão

Esses dashboards serão versionados para acompanhar melhorias e novas necessidades 
de análise.

#  Análise dos Resultados