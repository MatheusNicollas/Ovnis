# -*- coding: utf-8 -*-
"""5.7 - Limpeza dos dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mwx85o8RhUtXl-p5VmZRyaijrm8QQQDG
"""

import pandas as pd

#1. Carregar o seu arquivo OVNIS.csv em um dataframe
df_ovnis = pd.read_csv("ovnis.csv", index_col=[0])
df_ovnis

#2. Remover registros que tenham valores vazios (None, Unknown, ...) para City, State e Shape
df_notnull = df_ovnis.dropna(subset=["State"])
df_notnull = df_notnull.dropna(subset=["City"])
df_notnull = df_notnull.dropna(subset=["Shape"])

df_remove = df_notnull.loc[(df_notnull['Shape'] == 'Unknown') 
                         | (df_notnull['Shape'] == 'None')
                         | (df_notnull['City'] == 'Unknown') 
                         | (df_notnull['City'] == 'None')
                         | (df_notnull['State'] == 'Unknown') 
                         | (df_notnull['State'] == 'None')]

df_notnull = df_notnull.drop(df_remove.index)

df_notnull

#3. Manter somente os registros referentes aos 51 estados dos Estados Unidos:
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

selection = df_notnull['State'].isin(states)
df_usa = df_notnull[selection]

df_usa

#4. Remover variáveis irrelevantes para a análise (Duration, Summary e Posted);
df_colunas = df_usa.drop(columns=['Duration'])
df_colunas = df_colunas.drop(columns=['Summary'])
df_colunas = df_colunas.drop(columns=['Posted'])

df_colunas

#5. Manter somente os registros de Shapes mais populares (com mais de 1000 ocorrências);

df_colunas['Quantidade'] = df_colunas.groupby('Shape')['Shape'].transform('count')
df_final = df_colunas.query('Quantidade >= 1000')
df_final = df_final.drop(columns=['Quantidade'])
df_final

#6. Salvar o dataframe final em um arquivo CSV com o nome "df_OVNI_limpo".
df_final.to_csv("df_OVNI_limpo.csv")