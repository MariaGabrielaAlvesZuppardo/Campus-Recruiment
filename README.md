# Campus-Recruiment Data Analysis

## Dados: Dataset utilizado no Kaggle 

<div align="center">
  <p>
    <img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white"/>
  </p>
</div>

### Sobre o dataset: 

Esse conjunto de dados consiste em dados de colocação de alunos em um campus XYZ. Inclui a percentagem e a especialização do ensino secundário e superior. Também inclui especialização, tipo e experiência profissional e ofertas salariais aos alunos colocados. 

## Descrição do Projeto

O projeto utiliza a biblioteca Pandas para carregar e manipular os dados do arquivo CSV 'Placement_Data_Full_Class(Bronze).csv'. As seguintes etapas são realizadas:

1. **Carregamento e Pré-processamento dos Dados**
   - Os dados são carregados do arquivo CSV 'Placement_Data_Full_Class(Bronze).csv'.
   - Valores ausentes são preenchidos com 0.
   - Os dados processados são salvos em um novo arquivo 'placement_data_silver.csv'.

2. **Transformação e Análise de Dados**
   - Utiliza-se o LabelEncoder para converter colunas categóricas em valores numéricos.
   - Criação de novas features:
     - 'total_marks': soma das notas 'ssc_p', 'hsc_p', 'degree_p', 'etest_p', e 'mba_p'.
     - 'percentage_increase': diferença percentual entre 'hsc_p' e 'ssc_p'.

3. **Uso da Arquitetura Medalhão**
   - O projeto adota a Arquitetura Medalhão para organizar o código em módulos independentes e reutilizáveis.
   - Os diferentes aspectos da análise, pré-processamento e transformações de dados são divididos em medalhões (ou módulos), facilitando a manutenção e extensão do projeto.

4. **Salvando os Dados Processados**
   - Os dados transformados são salvos em um novo arquivo 'placement_data_golden.csv'.
  
### Bibliotecas Utilizadas: 

<div align="center">
  <p>
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"/>
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  </p>
</div>
