"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Pandas - Trabalhando com DataFrames: Operações Básicas de I/O, Leitura e Tratamentos
         Imports Necessários: Pandas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
 
import pandas as pd

 #Criar DataFrame a partir de um dicionário
df_meses = pd.DataFrame(pd.DataFrame({'Mes':[1,2,3,4,5,6,7,8,9,10,11,12],
                             'desc_mes':['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'],
                             'Trimestre':[1,1,1,2,2,2,3,3,3,4,4,4],
                             'Semestre':[1,1,1,1,1,1,2,2,2,2,2,2]}))

#Importando o DataFrame de um caminho específico (para fins desse exemplo, considerar um df com as colunas 'coluna01','coluna02','data','valor')
df = pd.read_csv('/filepath, 
                  encoding='utf-16',
                  sep=';',
                  squeeze=True,
                  header=infer)
#Gravar o DataFrame em um local específico, num formato desejado
df.to_csv('/filepath/name.csv',)

#Converter para DataFrame (ex: quando se tem uma série e se quer mudar para DataFrame)
df = pd.DataFrame(series)

#Utilizar mais de uma coluna como index
df.set_index(['coluna01','coluna02'])

#Resetar o index, transformando-o novamente em uma coluna
df.reset_index()

#Transformar um DataFrame em uma série temporal (transformando a data em index)
series = df.set_index('data')

#Eliminar duplicatas mantendo o primeiro e eliminando o último, tomando como referência duas colunas específicas e ignorando o index
df02 = df01.drop_duplicates(igonre_index = True, subset=['coluna01','coluna02'], keep='first')          

#Eliminar colunas
df = df.drop(columns=['coluna01'])

#Filtro simples para até n termos de busca em um determinado dataFrame
df = df[(df['coluna01']=='termo_filtrado_01')&
          df['coluna02']=='termo_filtrado_02')]

#Filtrar um DataFrame deixando apenas valores menores ou iguais a determinado numero (útil para séries temporais ou groupby)
df_filtrado = df[df<=100000]

#Agrupar df por uma coluna específica e executar operações matemáticas
df.groupby('coluna01')['valor'].agg(['count','sum','mean','std','median','min','max'])

#Mergir duas bases de dados a partir de uma ou mais colunas como referência
df_mergido01 = pd.merge(df01, df02, on=['coluna01','coluna02','coluna03'],how='left') #tomando como referência o df01
df_mergido02 = pd.merge(df01, df02, on=['coluna01','coluna02','coluna03'],how='right') #tomando como referência o df02
df_mergido03 = pd.merge(df01, df02, on=['coluna01','coluna02','coluna03'],how='inner') #tomando como referência os valores presentes em ambos
df_mergido04 = pd.merge(df01, df02, on=['coluna01','coluna02','coluna03'],how='outer') #tomando como referência os valores que um não tem igual no outro
df_mergido05 = pd.concat([df01, df02]) #unindo todos os valores de df01 e df02

#Substituir '.' ou outros valores de texto numa coluna do df (no caso abaixo, supor que o DataFrame tenha valores numéricos como um '33.54')
df['valor'] = df['valor'].str.replace('.',',')
df['valor'] = df['valor'].astype(float)



"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Dates - Trabalhando com Datas: lendo e convertendo em Datas 
         Imports Necessários: Pandas e Datetime
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import pandas as pd
from datetime import datetime

#Convertendo uma coluna do formato 'dd/mm/aaaa - 01/01/2000' para um datetime
df['Ano'] = df['Data'].astype(str).str[6:]
df['Mes'] = df['Data'].astype(str).str[3:5]
df['Dia'] = df['Data'].astype(str).str[:2]

df['Data_Convertida'] = pd.to_datetime(df['Ano']+'-'+df['Mes']+'-'+df['Dia'],
                                       format='%Y-%m-%d')



"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Funções - Algumas funções úteis no tratamento de dados 
          Imports Necessários: Pandas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import pandas as pd

#Criar uma lista vazia
lista01 = []

#Colocar os valores no final de uma lista após a execução de uma série de cálculos/operações ou aplicação de uma função específca
from statsmodels.tsa.stattools import adfuller 
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
#Filtro dinâmico, filtrando as informações de um df com as de um df02, e aplicando uma função para cada conjunto de valores no novo DataFrame
for(i,j) in df02.iterrows():
  filtro_01 = j.loc['coluna01']
  filtro_02 = j.loc['coluna02']
  df_filtrada = df[(df['coluna01']==filtro_01)&
                   (df['coluna02']==filtro_02)].drop(columns=['coluna01','coluna02'])
  analisar_DataFrame(df_filtrada)
 

 
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Resample - Redimensionamento de dados
           Imports Necessários: Numpy e Pandas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import pandas as pd
import numpy as np

#Redimensionamento de uma série temporal por unidades de tempo, aplicando multiplas operações da classe numpy
operacoes = [np.mean,np.sum,np.std,np.max,np.min,np.count]

df03 = df.resample('B').apply(operacoes).add.add_suffix('_businessDay')
df03 = df.resample('W').apply(operacoes).add.add_suffix('_semanal')
df03 = df.resample('15D').apply(operacoes).add.add_suffix('_quinzenal')
df03 = df.resample('M').apply(operacoes).add.add_suffix('_mensal')
df03 = df.resample('B').apply(operacoes).add.add_suffix('_bimestral')
df03 = df.resample('Q').apply(operacoes).add.add_suffix('_trimestral')

#Agregação por mês
df05 = df04.assign(month=lambda df: df.index.month).groupby('month')['_semanal'].agg(['mean','std','median','min','max'])

#Pivotear o dataframe por valores repetidos de uma coluna específica, por ano
df_anual = pd.pivot_table(df,index=["Item","Filial"], columns='ano',values=['peso','custo','fatuamento'])



"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
SQLite - Conectar com banco de dados sqlite e executar operações de leitura e gravação
         Imports Necessários: Pandas e Sqlite3
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import pandas as pd
import sqlite3

#Conectar com banco de dados do tipo sqlite3
cnx = sqlite3.connect('path/database.db')

#Definir colunas a serem lidas
colunas_relatorio = 'header_coluna01, header_coluna02, header_coluna03'

#Ler tabelas do bando de dados
tabela01 = pd.read_sql_query("SELECT "+colunas_relatorio+" FROM tabelaDoBancoDeDados", cnx)

#Gravar DataFrame no Banco de Dados como uma tabela específica, substituindo a anterior
df.to_sql(tabela01, cnx, if_exists='replace',index=False)
