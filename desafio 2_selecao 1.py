# Usando a biblioteca pandas, faça alguns filtros  no dataset do link anterior

# Selecione as pessoas vacinadas de Recife do sexo feminino da cor parda e preta maior de 60 anos
# Selecione as pessoas  que se vacinaram nos meses de abril e maio do sexo masculino
# Além do código, escreva no reade.me como você chegou na solução.

import pandas as pd

df_vacinados = pd.read_csv('vacinados_CERTO CERTO.csv')

selecao = df_vacinados_filtrado = df_vacinados.loc[(df_vacinados['sexo'] == 'FEMININO') & ((df_vacinados['raca_cor'] == 'PARDA') | (df_vacinados['raca_cor'] == 'PRETA')) & (df_vacinados['idade'] > 60)]
filtro = selecao[['sexo','raca_cor','idade']]
print(filtro)