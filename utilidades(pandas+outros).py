import pandas as pd
from statsmodels.tsa.stattools import adfuller
 
#Importando o DataFrame de um caminho específico (para fins desse exemplo, considerar um df com as colunas 'coluna01','coluna02','data','valor')
df = pd.read_csv('\filepath, 
                  encoding='utf-16',
                  sep=';',
                  squeeze=True,
                  header=infer)
                  
#Eliminar duplicatas de cima pra baixo
df02 = df01.drop_duplicates(keep='first')          

#Criar uma lista vazia
lista01 = []

#Colocar os valores no final de uma lista após a execução de uma série de cálculos/operações ou aplicação de uma função específca
def analisar_DataFrame(dataset):
    dataset = dataset.astype('int32')
    try:
        adfResult = adfuller(dataset)
    except:
        adfResult = 'sample size too short'
    lista01.append(termo_filtrado_01,
                   termo_filtrado_02,
                   adfResult[0],
                   adfResult[4]['10%'],
                   adfResult[4]['5%'],
                   adfResult[4]['1%']
                   )
                   
#Filtro simples para até n termos de busca em um determinado dataFrame
df = df[(df['coluna01']=='termo_filtrado_01')&
          df['coluna02']=='termo_filtrado_02')]

#Filtro dinâmico, filtrando as informações de um df com as de um df02, e aplicando uma função para cada conjunto de valores no novo DataFrame
for(i,j) in df02.iterrows():
  filtro_01 = j.loc['coluna01']
  filtro_02 = j.loc['coluna02']
  df_filtrada = df[(df['coluna01']==filtro_01)&
                   (df['coluna02']==filtro_02)].drop(columns=['coluna01','coluna02'])
  analisar_DataFrame(df_filtrada)
            
#Agrupar df por uma coluna específica e executar múltiplos cálculos com a coluna de valores
df.groupby('coluna01')['valor'].agg(['count','sum','mean','std','median','min','max'])

#Transformar um DataFrame em uma série temporal (transformadno a data em index)
df.set_index('data')

#Resetar o index da série temporal
df.reset_index()

#Utilizar mais de uma coluna como index
df.set_index(['coluna01','coluna02'])
          
