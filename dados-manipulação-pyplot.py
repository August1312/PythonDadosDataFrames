import pandas as pd 
from matplotlib import pyplot as plt

# Nome do arquivo CSV
csv_filename = "dados_aleatorios_fake.csv"

# Ler dados CSV em um DataFrame
df = pd.read_csv(csv_filename, encoding='latin1')

pais = pd.DataFrame({'Pais': df['País'].unique()})

# Escolher a coluna para o
coluna_para_grafico = 'País'
df_limitado = df.head(50)

# Criar o gráfico de colunas
plt.bar(df_limitado['País'], df_limitado[coluna_para_grafico])

# Adicionar rótulos e títulos
plt.xlabel('País')
plt.ylabel(coluna_para_grafico)
plt.title(f'Gráfico de Colunas para a Coluna "{coluna_para_grafico}"')

# Ajusta rótulos do eixo X
plt.xticks(rotation=45, ha='right')

plt.show()