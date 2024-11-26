# Este script atenderá a primeira etapa da parte 1 das tarefas propostas:
# Limpeza e Análise de Dados de Vendas.

# Instalando dependências necessárias:
# pip install pandas

# Importando a biblioteca Pandas para analisar dados de origem .xlsx (Excel).
import pandas as pd
# Usaremos o "pd" para referenciar essa biblioteca.


# Carregando dados da simulação para o ambiente de desenvolvimento.
dados = pd.read_excel(
    "AgricultureData.xlsx"
)

# Transformando o conjunto de dados em um Dataframe
df = pd.DataFrame(dados)

# Exibindo as colunas carregadas.
print("Colunas carregadas")
print(df.columns)
print("\n") # Pulando uma linha para exibir as próximas strings

# Selecionando apenas as colunas que serão necessárias para essa análise.
df = df[
    ["order_id","sale_date","product_name","category","units_sold_kg", "price_per_kg"]
]

# Alterando o nome das colunas para melhor entendimento.
df = df.rename(
    columns={
        "order_id": "id", "sale_date": "Data", "product_name": "Produto",
        "category": "Categoria", "units_sold_kg": "Quantidade", "price_per_kg": "Preço"
    }
)

# Conferindo se existem valores nulos no dataframe
print("Quantidade de nulos por coluna:")
print(df.isnull().sum())
print("\n") # Pulando uma linha para exibir as próximas strings
# Para este conjunto de dados não foram encontrados nulos.
# Caso fosse encontrado usariámos a função dropna, /
# porém dependendo da coluna uma análise seria necessária antes de executar a função

# A chave primária do nosso conjunto de dados é a coluna "id", portanto todos os valores devem ser exclusivos.
# Checando se existem duplicatas na coluna "id".
print("Quantidade de duplicatas na coluna 'id':")
print(df["id"].duplicated().sum())
print("\n") # Pulando uma linha para exibir as próximas strings

# Checando os tipos de dados de cada coluna.
print("Tipos de dados de cada coluna:")
print(df.dtypes)
print("\n") # Pulando uma linha para exibir as próximas strings

# Exibindo 10 amostras do dataframe para confirmar se o tipo de dado faz sentido.
print("Amostra com 10 linhas aleatórias do dataframe:")
print(df.sample(10))
print("\n") # Pulando uma linha para exibir as próximas strings

# A coluna id é um fator identificador então precisa ser convertida para string.
# As demais colunas não precisam de ajustes quanto ao tipo de dados.

# Convertendo id do tipo inteiro para string.
df["id"] = df["id"].astype(str)

# A análise proposta pelo cliente diz respeito ao período de 01/01/2023 até 31/12/2023.
# Portanto, vamos filtrar nosso dataframe para remover linhas desnecessárias fora desse intervalo.
df = df[(df['Data'] >= '2023-01-01') & (df['Data'] <= '2023-12-31')]

# Salvando os dados tratando em um arquivo .csv
df.to_csv("data_clean.csv", index=False, encoding='utf-8')

#--------------------------------------------------------------------------------------------------------------#

# Inserindo uma nova coluna com o valor total de vendido em cada order
df["Total Vendido"] = df["Quantidade"] * df["Preço"]

# Criando uma variável que irá receber o valor total vendido por produto
total_vendido = df.groupby("Produto")["Total Vendido"].sum()

# Ordenando o agrupamento do maior para o menor.
total_vendido = total_vendido.sort_values(ascending=False)

# Exibindo o total de vendas por produto.
print("Total de vendas por produto:")
print(total_vendido)
print("\n") # Pulando uma linha para exibir as próximas strings

# Identificando o produto com maior número de vendas.
print("Produto com o maior número de vendas totais:")
print(total_vendido.head(1))