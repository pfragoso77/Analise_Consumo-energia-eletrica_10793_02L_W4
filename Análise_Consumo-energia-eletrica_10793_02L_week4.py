"""
Created on Sun Jun 25 17:12:13 2023

@author: Pedro
"""

#Exercício 4 10793_02/L 

# Importação da biblioteca Pandas para a realização de uma análise de dados
import pandas as pd

# tarefa 1 > importar dados da tabela Excel 
dados_analise = pd.read_excel('P_Data_Extract_From_World_Development_Indicators.xlsx', sheet_name='Data')
#print(dados_analise)

# tarefa 2 > limpeza de dados, somente os que interessam para o efeito
dados_analise = dados_analise[['Country Name', 'Country Code', '1990 [YR1990]', '2000 [YR2000]']]
#print(dados_analise)

# filtrar o pais pretendido = Portugal
dados_portugal = dados_analise[dados_analise['Country Name'] == 'Portugal']
print(dados_portugal)

# Valores específicos no dataframe que interessam para a análise
consumo_inicial = dados_portugal['1990 [YR1990]'].values[0]
consumo_final = dados_portugal['2000 [YR2000]'].values[0]

# tarefa 3 > definição para calcular a variaçãp
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100


# Chamar a função de cálcuo e imprimir o resultado
variacao_percentual = calcular_variacao_percentual(consumo_inicial, consumo_final)

# Imprimir o resultado (esta foi dura...)
print(f"A variação percentual no consumo de energia elétrica em Portugal entre 1990 e 2000: {variacao_percentual:.2f}%.")
