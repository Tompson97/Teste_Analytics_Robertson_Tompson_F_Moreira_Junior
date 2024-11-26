# Este script atenderá a segunda etapa da parte 1 das tarefas propostas:
# Análise Exploratória de Dados.

# Instalando dependências necessárias:
# Execute esses comando no terminal
# pip install pandas
# pip install matplotlib

# Importando a biblioteca Pandas para analisar dados de origem .xlsx (Excel).
import pandas as pd
# Usaremos o "pd" para referenciar essa biblioteca.

# Importando a biblioteca matplotlib para exibir gráficos.
import matplotlib.pyplot as plt
# Usaremos o "plt" para referenciar essa biblioteca.


# Carregando dados da simulação para o ambiente de desenvolvimento.
dados = pd.read_csv(
    "data_clean.csv"
)

# Transformando o conjunto de dados em um Dataframe.
df = pd.DataFrame(dados)

# Alterando o tipo da coluna Data de object para date.
df["Data"] = pd.DatetimeIndex(df["Data"])
print("\n") # Pulando uma linha para exibir as próximas strings

# Criando uma nova coluna para extrair o mês de cada venda.
df["Mês"] = df["Data"].dt.month
print("\n") # Pulando uma linha para exibir as próximas strings

# Criando uma variável que irá receber o valor total vendido de cada mês.
venda_mensal = df.groupby("Mês")["Total Vendido"].sum()

# Construindo um gráfico de linhas para exibir as vendas mensais.
meses = [ # Criando uma lista com o nom de cada mês para exibir no gráfico
    "Janeiro",
    "Feveiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

plt.figure(figsize=(15, 6)) # Tamanho do gráfico
plt.plot(venda_mensal.index, venda_mensal.values, marker="o") # Definindo o eixo X e Y
for i, j in zip(venda_mensal.index, venda_mensal.values): # Adicionando  rótulo de dados, com tamanho 8 e cor preta
    plt.text(i, j+0.2, f"R$ {j:.2f}", ha='right', va='bottom', fontsize=8, color='black')
plt.xlabel( # Definindo uma mensagem com obervações sobre o resultado.
    "As vendas ao longo do ano apresentaram muitas oscilações. O primeiro trimestre apresentou uma queda progressiva e, a partir de maio, iniciou um crescimento, atingindo o pico em junho e,\n após isso, iniciou outra queda. Apenas os meses de julho e agosto ficaram equilibrados. Um estudo aprofundado deve ser realizado para identificar o motivo das oscilações e identificar as principais tendências\n dos meses em destaque para replicar nos demais meses do ano seguinte.")
plt.ylabel("Total Vendido") # Rótulo do eixo y
plt.title("Total Vendido por Mês") # Título do gráfico
plt.xticks(venda_mensal.index, meses) # Exibindo o rótulo do eixo x com o nome dos meses da lista anterior
plt.show()
print("\n") # Pulando uma linha para exibir as próximas strings