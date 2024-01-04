import pandas as pd 

# Carregando os dados
data = pd.read_csv('data/Placement_Data_Full_Class(Bronze).csv')

print(data.head())

# Tratamento para valores ausentes
data.fillna(0, inplace=True)

# Salvar os dados processados em um novo arquivo CSV na pasta 'data'
data.to_csv('data/placement_data_silver.csv', index=False)  
# Index=False para não salvar o índice do DataFrame

# Carregar o conjunto de dados processado para verificar se as transformações foram aplicadas corretamente
processed_data = pd.read_csv('data/placement_data_silver.csv')
print(processed_data.head())