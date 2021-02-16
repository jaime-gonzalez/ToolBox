


#Score R² da Regressão linear entre duas variáveis (x,y)
from sklearn.metrics import r2_score
score = r2_score(df['valor01'],df['valor02'])

#Cálculo dos valores de outliers para uma distribuição normal
import pandas as pd
resA1 = df.groupby(['Coluna01','Coluna02'])['Valor'].quantile([0.05]) #Quantil p/ limite inferior até 5% da distribuição normal (2 desvios padrões) 
resA2 = df.groupby(['Coluna01','Coluna02'])['Valor'].quantile([0.95]) #Quantil p/ limite superior até 95% da distribuição normal (2 desvios padrões)
res = pd.merge(resA1, resA2, on = ['Coluna01','Coluna02'], how = 'left',suffixes=('_Lim. Inf','_Lim. Sup'))


"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Análise de Séries Temporais
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


#MOVING AVERAGE: Melhor modelo de regressão  para um modelo do tipo 'MA', com o resultado sendo a ordm (nº de períodos p/ a média) do modelo
#Para utilizar este modelo, pode ser necessário fazer um resample por mês/semana
optimal_n = None
best_mse = None
df['coluna01','coluna02','valor']
db = df[['valor']].values.astype('float32')
mean_results_for_all_possible_n_values = np.zeros(int(len(db) / 2 - 2))

for n in range(3, int(len(db) / 2 + 1)):
    mean_for_n = np.zeros(len(db) - n)
    for i in range(0, len(db) - n):
        mean_for_n[i] = np.power(np.mean(db[:, 0][i:i+n]) - db[i + n][0], 2)
    mean_results_for_all_possible_n_values[n - 3] = np.mean(mean_for_n)
optimal_n = np.argmin(mean_results_for_all_possible_n_values) + 3
best_mse = np.min(mean_results_for_all_possible_n_values)

print("MSE = %s" % mean_results_for_all_possible_n_values)
print("Melhor MSE = %s" % best_mse)
print("Otimo n = %s" % optimal_n)

#MOVING AVERAGE: Previsão utilizando o melhor modelo de previsão do tipo 'MA'
forecast = np.zeros(len(db) + 1)
for i in range(0, optimal_n):
    forecast[i] = db[i][0]
for i in range(0, len(db) - optimal_n + 1):
        forecast[i+optimal_n] = np.mean(db[:, 0][i:i+optimal_n])
plt.plot(db[:, 0],label = 'Dados Originais')
plt.plot(forecast, label = 'Previsão')
plt.legend()
plt.show()
