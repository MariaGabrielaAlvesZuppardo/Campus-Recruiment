import pandas as pd 
from sklearn.preprocessing import LabelEncoder

# Carregando os dados
data = pd.read_csv('data/Placement_Data_Full_Class(Bronze).csv')

# Tratamento para valores ausentes (preenchendo com 0)
data.fillna(0, inplace=True)

# Salvando os dados processados em um novo arquivo CSV na pasta 'data'
data.to_csv('data/placement_data_silver.csv', index=False)  # Index=False para não salvar o índice do DataFrame

# Carregando o conjunto de dados processado para verificar se as transformações foram aplicadas corretamente
processed_data = pd.read_csv('data/placement_data_silver.csv')
print(processed_data.head())

# Carregando os dados novamente
data = pd.read_csv('data/placement_data_silver.csv')

# Inicializando o LabelEncoder
label_encoder = LabelEncoder()

# Aplicando o LabelEncoder em cada coluna categórica
categorical_columns = ['gender', 'ssc_b', 'hsc_s', 'degree_t', 'workex', 'specialisation', 'status']
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

# Visualizando as primeiras linhas dos dados após a aplicação do LabelEncoder
print(data.head())

# Criando uma nova feature 'total_marks' representando a soma das notas
data['total_marks'] = data['ssc_p'] + data['hsc_p'] + data['degree_p'] + data['etest_p'] + data['mba_p']

# Visualizando as primeiras linhas dos dados com a nova feature 'total_marks'
print(data[['ssc_p', 'hsc_p', 'degree_p', 'etest_p', 'mba_p', 'total_marks']].head())

# Criando uma feature "Diferença entre HSC e SSC"
data['percentage_increase'] = ((data['hsc_p'] - data['ssc_p']) / data['ssc_p']) * 100

# Visualizando as primeiras linhas dos dados com a nova feature 'percentage_increase'
print(data[['ssc_p', 'hsc_p', 'percentage_increase']].head())
