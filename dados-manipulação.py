import pandas as pd 
from matplotlib import pyplot as plt

# Nome do arquivo CSV
csv_filename = "dados_aleatorios_fake.csv"

# Ler dados CSV em um DataFrame
df = pd.read_csv(csv_filename, encoding='latin1')

# Imprimir a lista de colunas
print("Colunas no DataFrame:")
print(df.columns)


pais = pd.DataFrame({'Pais': df['País']})
nome = pd.DataFrame({'Nome': df['Nome']})
cidade = pd.DataFrame({'Cidade': df['Cidade']})
estado = pd.DataFrame({'Estado': df['Estado']})
print("\nNovo DataFrame para a coluna 'País':")
print(pais)
print(estado)
print(nome)
print(cidade)
