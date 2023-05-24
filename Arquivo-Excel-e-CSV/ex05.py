# Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna Rádio, utilizando a biblioteca plotly.

import pandas as pd
import plotly.express as px

df = pd.read_csv('Propaganda.csv')
fig = px.histogram(df, x="Radio")
fig.show()