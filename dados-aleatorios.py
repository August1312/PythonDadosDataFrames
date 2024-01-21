import csv
from faker import Faker
import random

# Criar uma instância do Faker
fake = Faker()

# Número de linhas no CSV
num_rows = 10000

# Lista de cabeçalhos
headers = ["ID", "Nome", "Idade", "Cidade", "Estado", "País"]

# Nome do arquivo CSV
csv_filename = "dados_aleatorios_fake.csv"

# Geração dos dados aleatórios e escrita no arquivo CSVpip
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escrever cabeçalhos
    writer.writerow(headers)
    
    # Gerar dados aleatórios usando Faker
    for i in range(1, num_rows + 1):
        nome = fake.name()
        idade = random.randint(18, 60)
        cidade = fake.city()
        estado = fake.state()
        pais = fake.country()
        
        row_data = [i, nome, idade, cidade, estado, pais]
        writer.writerow(row_data)

print(f"Arquivo CSV '{csv_filename}' gerado com sucesso.")
