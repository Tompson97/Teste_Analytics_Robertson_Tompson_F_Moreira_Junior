
## Parte 1: Programação em Python
# Limpeza e Análise de Dados de Vendas
Este script atenderá a primeira etapa da parte 1 das tarefas propostas

#### Sempre que for usado ```print("\n"))``` no código será para pular uma linha.

Instalando dependências e importando bibliotecas necessárias
Execute esse comando no terminal\
```pip install pandas ```

Importando a biblioteca Pandas para analisar dados de origem .xlsx (Excel).\
Usaremos o "pd" para referenciar essa biblioteca.\
```import pandas as pd```

Carregando dados da simulação para o ambiente de desenvolvimento
```dados = pd.read_excel("AgricultureData.xlsx")```

Transformando o conjunto de dados em um Dataframe
```df = pd.DataFrame(dados)```

Exibindo as colunas carregadas.
```print("Colunas carregadas")```\
```print(df.columns)```\
```print("\n")```

Selecionando apenas as colunas que serão necessárias para essa análise.
```df = df.rename(columns={"order_id": "id", "sale_date": "Data", "product_name": "Produto","category": "Categoria", "units_sold_kg": "Quantidade", "price_per_kg": "Preço"})```

Conferindo se existem valores nulos no dataframe
```print("Quantidade de nulos por coluna:")```\
```print(df.isnull().sum())```\
```print("\n")```\
Para este conjunto de dados não foram encontrados nulos.
Caso fosse encontrado usariámos a função dropna, porém dependendo da coluna uma análise seria necessária antes de executar a função

A chave primária do nosso conjunto de dados é a coluna "id", portanto todos os valores devem ser exclusivos. Checando se existem duplicatas na coluna "id".
```print("Quantidade de duplicatas na coluna 'id':")```\
```print(df["id"].duplicated().sum())```\
```print("\n")```

Checando os tipos de dados de cada coluna.\
```print("Tipos de dados de cada coluna:")```\
```print(df.dtypes)```\
```print("\n")```

Exibindo 10 amostras do dataframe para confirmar se o tipo de dado faz sentido.\
```print("Amostra com 10 linhas aleatórias do dataframe:")```\
```print(df.sample(10))```\
```print("\n")```

A coluna id é um fator identificador então precisa ser convertida para string. As demais colunas não precisam de ajustes quanto ao tipo de dados.
Convertendo id do tipo inteiro para string.\
```df["id"] = df["id"].astype(str)```

A análise proposta pelo cliente diz respeito ao período de 01/01/2023 até 31/12/2023.\
Portanto, vamos filtrar nosso dataframe para remover linhas desnecessárias fora desse intervalo.\
```df = df[(df['Data'] >= '2023-01-01') & (df['Data'] <= '2023-12-31')]```


Inserindo uma nova coluna com o valor total de vendido em cada order\
```df["Total Vendido"] = df["Quantidade"] * df["Preço"]```

### Salvando os dados tratando em um arquivo .csv
```df.to_csv("data_clean.csv", index=False, encoding='utf-8', decimal='.')```

### Criando uma variável que irá receber o valor total vendido por produto
```total_vendido = df.groupby("Produto")["Total Vendido"].sum()```

Ordenando o agrupamento do maior para o menor.\
```total_vendido = total_vendido.sort_values(ascending=False)```

Exibindo o total de vendas por produto.\
```print("Total de vendas por produto")```\
```print(total_vendido)```\
```print("\n")``` 

### Identificando o produto com maior número de vendas.
```print("Produto com o maior número de vendas totais:")```\
```print(total_vendido.head(1))```

# Análise Exploratória de Dados de Vendas
Este script atenderá a segunda etapa da parte 1 das tarefas propostas.

Instalando dependências necessárias:\
Execute esses comando no terminal\
```pip install matplotlib```

Importando a biblioteca matplotlib para exibir gráficos.
import matplotlib.pyplot as plt
Usaremos o "plt" para referenciar essa biblioteca.

Carregando dados da simulação para o ambiente de desenvolvimento.\
```dados = pd.read_csv("data_clean.csv")```

Transformando o conjunto de dados em um Dataframe.\
```df = pd.DataFrame(dados)```

Alterando o tipo da coluna Data de object para date.\
```df["Data"] = pd.DatetimeIndex(df["Data"])```\
```print("\n")```

Criando uma nova coluna para extrair o mês de cada venda.\
```df["Mês"] = df["Data"].dt.month```\
```print("\n")``` #

Criando uma variável que irá receber o valor total vendido de cada mês.\
```venda_mensal = df.groupby("Mês")["Total Vendido"].sum()```

Construindo um gráfico de linhas para exibir as vendas mensais.\
Criando uma lista com o nom de cada mês para exibir no gráfico\
```meses = [ "Janeiro","Feveiro","Março","Abril","Maio","Junho","Julho","Agosto", "Setembro","Outubro","Novembro","Dezembro"```\
```]```

Construindo um gráfico de linhas para exibir as vendas mensais.\

```plt.figure(figsize=(15, 6)) # Tamanho do gráfico```\
```plt.plot(venda_mensal.index, venda_mensal.values, marker="o") # Definindo o eixo X e Y```\
```for i, j in zip(venda_mensal.index, venda_mensal.values): plt.text(i, j+0.2, f"R$ {j:.2f}", ha='right', va='bottom', fontsize=8, color='black')```\
```plt.xlabel( # Definindo uma mensagem com obervações sobre o resultado.```\
```    "As vendas ao longo do ano apresentaram muitas oscilações. O primeiro trimestre apresentou uma queda progressiva e, a partir de maio, iniciou um crescimento, atingindo o pico em junho e,\n após isso, iniciou outra queda. Apenas os meses de julho e agosto ficaram equilibrados. Um estudo aprofundado deve ser realizado para identificar o motivo das oscilações e identificar as principais tendências\n dos meses em destaque para replicar nos demais meses do ano seguinte.")```\
```plt.ylabel("Total Vendido") # Rótulo do eixo y```\
```plt.title("Total Vendido por Mês") # Título do gráfico```\
```plt.xticks(venda_mensal.index, meses) # Exibindo o rótulo do eixo x com o nome dos meses da lista anterior```\
```plt.show() # Exibe o gráfico```