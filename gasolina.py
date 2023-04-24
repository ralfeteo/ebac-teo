# código de geração do gráfico gasolina.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))

with sns.axes_style('whitegrid'):
  plt.title('Valor da gasolina,SP Julho.2021', fontsize=18)
  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda")
  grafico.set(xlabel='Dia', ylabel='Preço da venda' )
  grafico.get_figure().savefig("Preço médio da gasolina.png")