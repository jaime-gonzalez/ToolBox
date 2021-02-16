


#Score R² da Regressão linear entre duas variáveis (x,y)
from sklearn.metrics import r2_score
score = r2_score(df['valor01'],df['valor02'])

#Cálculo dos valores de outliers para uma distribuição normal
import pandas as pd
resA1 = df.groupby(['Coluna01','Coluna02'])['Valor'].quantile([0.05]) #Quantil p/ limite inferior até 5% da distribuição normal (2 desvios padrões) 
resA2 = df.groupby(['Coluna01','Coluna02'])['Valor'].quantile([0.95]) #Quantil p/ limite superior até 95% da distribuição normal (2 desvios padrões)
res = pd.merge(resA1, resA2, on = ['Coluna01','Coluna02'], how = 'left',suffixes=('_Lim. Inf','_Lim. Sup'))



