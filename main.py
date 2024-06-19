import os
import pandas
from IPython.display import display
import plotly.express as plotly

dados = os.listdir('./dados') # Cria uma lista com os dados da base, após percorre-lá
tabela_Vendas = pandas.DataFrame()

for arquivo in dados:
    if 'Vendas' in arquivo: # Para percorrer apenas as bases de venda, desconsiderando as de devoluções
        tabela = pandas.read_csv(f'./dados/{arquivo}') # Variável com um arquivo .csv
        tabela_Vendas = tabela_Vendas._append(tabela) # Todas as bases de vendas unificadas em uma

 # 1º objetivo - Calcular o produto mais vendido em quantidade
tabela_Produtos = tabela_Vendas.groupby('Produto').sum() # Agrupa as células usando 'Produtos' como index e somando as restantes
tabela_Produtos = tabela_Produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida',ascending=False) # Apresenta a tabela com o index ('Produtos') e 'Quantidade Vendida' e, organiza em ordem decrescente.
display(tabela_Produtos)

# 2º objetivo - Calcular o produto mais vendido em faturamento
tabela_Vendas['Faturamento'] = tabela_Vendas['Quantidade Vendida'] * tabela_Vendas['Preco Unitario'] # Faturamento do produto = preço x quantidade
tabela_Faturamento = tabela_Vendas.groupby('Produto').sum()
tabela_Faturamento = tabela_Faturamento[['Faturamento']].sort_values(by='Faturamento',ascending=False)
display(tabela_Faturamento)

# 3º objetivo - Calcular a loja/cidade que mais vende em faturamento
tabela_Lojas = tabela_Vendas.groupby('Loja').sum()
tabela_Lojas = tabela_Lojas[['Faturamento']].sort_values(by='Faturamento',ascending=False)
display(tabela_Lojas)

# 4º objetivo - Criar um gráfico de faturamento por loja
grafico = plotly.bar(tabela_Lojas,x = tabela_Lojas.index,y = 'Faturamento') # Definição do gráfico
grafico.show() # Exibe o gráfico
