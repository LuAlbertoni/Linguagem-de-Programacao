# Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente a média da coluna do arquivo 'Valor Unitário'.

import pandas as pd

df = pd.read_excel('Vendas.xlsx')
print(f"{df['Valor Unitário'].mean():.2f}")
