import pandas as pd 
from sklearn.preprocessing import LabelEncoder


# Carregando os dados
data = pd.read_csv('data/Placement_Data_Full_Class(Bronze).csv')

# Tratamento para valores ausentes
data.fillna(0, inplace=True)

# Salvar os dados processados em um novo arquivo CSV na pasta 'data'
data.to_csv('data/placement_data_silver.csv', index=False)  
# Index=False para não salvar o índice do DataFrame

# Carregar o conjunto de dados processado para verificar se as transformações foram aplicadas corretamente
processed_data = pd.read_csv('data/placement_data_silver.csv')
print(processed_data.head())

# Carregar os dados
data = pd.read_csv('data/placement_data_silver.csv')

# Inicializar o LabelEncoder
label_encoder = LabelEncoder()

# Aplicar o LabelEncoder em cada coluna categórica
categorical_columns = ['gender', 'ssc_b', 'hsc_s', 'degree_t', 'workex', 'specialisation', 'status']
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Visualizar as primeiras linhas dos dados
print(data.head())

# Criar uma nova feature 'total_marks' representando a soma das notas
data['total_marks'] = data['ssc_p'] + data['hsc_p'] + data['degree_p'] + data['etest_p'] + data['mba_p']

# Visualizar as primeiras linhas dos dados com a nova feature
print(data[['ssc_p', 'hsc_p', 'degree_p', 'etest_p', 'mba_p', 'total_marks']].head())
