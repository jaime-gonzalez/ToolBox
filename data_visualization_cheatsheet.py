"""         
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            Visualizações de Dados com Seaborn e Matplotlib
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

#Plotar mapa de calor - é preciso eliminar as colunas de texto e manter apenas as de valores
import seaborn as sns

df['coluna01', 'coluna02', 'coluna03', 'valor01', 'valor02', 'valor03', 'valor04']
df_filtrado = df.drop(columns=['coluna01', 'coluna02', 'coluna03'])

f,ax = plt.subplots(figsize=(20,16))
sns.heatmap(df_filtrado.corr(),annot=True, 
            linewidths=.5, fmt='.1f', ax=ax) 
plt.show()


#Gráfico de dispersão 'Scatterplot', com as colunas dos  valores de eixos x e y
import matplotlib.pyplot as plt
plt.plot(df['valor01'], df['valor02'], 'o', color='blue');
plt.title('Título', size = 20)
plt.xlabel('Rótulo de x',size=16)
plt.ylabel('Rótulo de y', size=16)
plt.rcParams['figure.figsize']=(20,16)
plt.show()
    

#Plotar histograma com quantidade de intervalos pré definida (sempre colocar apenas a coluna com os valores)
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=15,6

df['coluna01', 'coluna02', 'valores']

df_valores = df['valores']
df_valores.plot(kind='hist', stacked=True,bins=50)
plt.title('Título do gráfico')
plt.xlabel('Rótulo do eixo x')
plt.ylabel('Rótulo do eixo y')

#Gráfico de série temporal com agregação de múltiplos parâmetros da série por valores definidos
df['data', 'valor']
fig, ax = plt.subplots(1,1, figsize=(12,10))
(df
     .assign(month=lambda df: df.index.month)
     .groupby('month')['valor'].agg(['mean','std','median','min','max'])
     .plot(ax=ax, marker='o',linewidth=3)
 )
ax.set_xlabel('Mês')

#Plotar resample de uma série temporal com base no período
df_filtrado = df['data','valor']
df.resample('M').apply([np.mean]).plot()
plt.title('Título do gráfico')
plt.ylabel('Rótulo do eixo y')
plt.xlabel('Rótulo do eixo x')

#Gráficos de bloxplot com Seaborn (Possível utilizar como X múltiplos grupos de dados, para avaliar a variação dentro dos grupos)
df['Faixa', 'Valor']
ax = sns.boxplot(y=df['Valor'], 
                 x=df['Faixa'], 
                 data=df,
                 palette="coolwarm")     #Para mais paletas de cores, https://seaborn.pydata.org/tutorial/color_palettes.html
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
