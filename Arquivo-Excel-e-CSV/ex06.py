# Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna TV, utilizando a biblioteca Matplotlib, apresente na cor blueviolet.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Propaganda.csv')

plt.hist(df['TV'], len(df), rwidth=0.8, color='blueviolet')
plt.title('Propaganda Via TV')

plt.show()