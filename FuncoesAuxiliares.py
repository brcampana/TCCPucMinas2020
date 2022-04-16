## Funções auxiliares

# importação de bibliotecas
import pandas as pd
import numpy as np
import seaborn as sns

# Retorna as strings em uma lista que começam com um prefixo e termina com um 
# sufixo, sendo que o sufixo tem apenas um caracter
def ListaPrefixo(lista,prefixo,sufixo=''):
  return [a for a in lista if (not bool(a.find(prefixo))) and 
                              (not bool(a[::-1].find(sufixo[::-1])))]

def DispersaoPares(df):
  # gráficos de dispersão para comparação das variáveis aos pares
  g = sns.pairplot(df, height=2)
  # editar a posição dos lables dos eixos 'y' e 'x'
  for axes in g.axes.flat:
    axes.set_ylabel(axes.get_ylabel(), rotation=0, horizontalalignment='right',fontsize=16)
    axes.set_xlabel(axes.get_xlabel(), rotation=45,fontsize=16)
  plt.show()