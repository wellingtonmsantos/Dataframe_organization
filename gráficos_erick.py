'''
Objetivo é investigar as práticas de treino 
antes e durante 
as medidas de distanciamento social de atletas brasileiros de Halterofilismo Paralímpico.

1) Resultados divididos em total (homem e mulher juntos) 
- homem (n= ) e mulher (n= )

2) Resultados dos atletas que participam de 
jogos paralímpicos e competições internacionais; 
total (aqueles que participam competições internacionais e jogos paralímpicos)

3) Resultados daqueles que competem nos jogos paralímpicos, 
aí sem distinguir homem e m
'''
from scipy.stats import shapiro
from scipy.stats.stats import chisquare
from mc_nemar_and_bonferroni import McNemar_test
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort
from pandas.core import frame
from pandas.core.algorithms import value_counts
from pandas.core.reshape.pivot import crosstab
from statsmodels.stats.api import SquareTable
from statsmodels.stats.contingency_tables import mcnemar
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.offline as py
import csv
from scipy import stats
import seaborn as sns

#arquivo = "/home/well/GoogleDrive/PROGRAMAÇÃO/ProjetO_erick/dataset_headers_OK.csv"
#dataframe = pd.read_csv("C:/Users/wellm/Google Drive (w180947@dac.unicamp.br)/PROGRAMAÇÃO/ProjetO_erick/dataset_headers_OK.csv",sep=';')
dataframe = pd.read_csv('/home/well/GoogleDrive/PROGRAMAÇÃO/ProjetO_erick/dataset_headers_OK.csv', sep=';')

#Primeira análise 
# headers = 'Sexo','Competição','Faixa de R.antes','Faixa de Reps durante pandemia','Faixa de S.antes','Faixa de Séries durante pandemia','Frequência antes','Frequência de treino','Motivação antes','Motivação durante','Compra de equip','Comprou equipamento','Como estou'
# headers = ['Idade','Altura','Sexo','Peso','Estado','Escolaridade','Número de moradores:','Quem mora?','Tipo de trabalho','Tipo de deficiência','Tempo de treino','Competição','Categoria masculino','Categoria feminino','Desempenho última competição','Compra de equipamentos','Faixa de R.antes','Faixa de S.antes','Ex além supino','Faixa de Reps antes além supino','Faixa de Séries antes além supino','Frequência antes','Motivação antes','Treina durante pandemia','Continua treinando durante pandemia','Comprou equip','Quais comprados','Continua treinando','Faixa de Reps durante pandemia','Faixa de Séries durante pandemia','Ex além supino durante pandemia','Faixa de Reps durante além supino','Faixa de Reps mais utilizadas ','Frequência de treino','Motivação durante','Como estou','Percepção de desempenho','Centro de treinamento em Universidade','Academia de musculação','Studio de Personal Trainer','Em casa','Peso livre (exercícios feitos com barras, anilhas e halteres)','Máquina (exercícios feitos na máquina)','Exercícios com peso corporal','Resistência variável (Correntes, elásticos, board)','Membros superiores','Tronco (abdome, lombar)','Membros inferiores']

#PRINTANDO TODOS OS HISTOGRAMANS 
histogramas = ['Sexo', 'Competição',
'Comprou equip','Faixa de R.antes','Faixa de Reps durante pandemia',
'Faixa de S.antes', 'Faixa de Séries durante pandemia', 'Frequência antes', 
'Frequência de treino','Motivação antes', 'Motivação durante']

# for comparação in histogramas:
            fig = px.histogram(dataframe, x=dataframe[comparação])
            fig.show()

# for comparação in histogramas:
            co = dataframe[comparação].value_counts()
            print(co)
            shapiroW = shapiro(co)
            print(shapiroW)

#ANÁLISE DAS COMPROU EQUIPAMENTO 
couting_equip = dataframe['Comprou equip'].value_counts()
comp_equi_perc = (dataframe['Comprou equip'].value_counts())/len(dataframe['Comprou equip'])*100
comp_equi_perc.plot(kind = 'bar',color='black')
chi_equip = chisquare(couting_equip)
print(chi_equip)
plt.show()

#COMPETIÇÃO
counting_comp = dataframe['Competição'].value_counts()
comp_perc = (dataframe['Competição'].value_counts())/len(dataframe['Competição'])*100
comp_perc.plot(kind = 'bar',color='black')
chi_comp = chisquare(counting_comp)
print(chi_comp)
plt.show()

#SEXO
counting_sex = dataframe['Sexo'].value_counts()
sex_perc = (dataframe['Sexo'].value_counts())/len(dataframe['Sexo'])*100
sex_perc.plot(kind = 'bar',color='black')
chi_sex = chisquare(counting_sex)
print(chi_sex)
plt.show()

#ANÁLISE DAS REPS
reps = pd.crosstab(dataframe['Faixa de R.antes'], dataframe['Faixa de Reps durante pandemia'], normalize=True)
print(reps.head())
reps_square_bhapkar = SquareTable(reps, shift_zeros=False).homogeneity(method='bhapkar')
print('Reps | Bhapkar Statistic= %.2f, p = %.2f' % (reps_square_bhapkar.statistic, reps_square_bhapkar.pvalue))
class_test_reps = McNemar_test(dataframe)
results_McNemar_reps = class_test_reps.bowkerPHmc('Faixa de R.antes', 'Faixa de Reps durante pandemia')
print(results_McNemar_reps)
plotting_Reps_antes = dataframe[['Faixa de R.antes']]
plotting_Reps_antes['antes'] = 'antes'
plotting_Reps_depois= dataframe[['Faixa de Reps durante pandemia']]
plotting_Reps_depois['depois'] = 'depois'
plotting_Reps_antes.columns = ['faixa_reps', 'periodo']
plotting_Reps_depois.columns = ['faixa_reps', 'periodo']
result_reps = pd.concat([plotting_Reps_antes, plotting_Reps_depois], ignore_index=True)
count_reps = sns.countplot(x='faixa_reps', hue='periodo', data=result_reps)
plt.show()

#ANÁLISE DAS SÉRIES  
sets_table = pd.crosstab(dataframe['Faixa de S.antes'], dataframe['Faixa de Séries durante pandemia'])
print(sets_table.head())
sets_square_bhapkar = SquareTable(sets_table, shift_zeros=False).homogeneity(method='bhapkar')
print('Faixa de séries | Bhapkar Statistic= %.2f, p = %.2f' % (sets_square_bhapkar.statistic, sets_square_bhapkar.pvalue))
class_test_reps = McNemar_test(dataframe)
results_McNemar_sets = class_test_reps.bowkerPHmc('Faixa de S.antes', 'Faixa de Séries durante pandemia')
print(results_McNemar_sets)
plotting_Sets_antes = dataframe[['Faixa de S.antes']]
plotting_Sets_antes['antes'] = 'antes'
plotting_Sets_depois = dataframe[['Faixa de Séries durante pandemia']]
plotting_Sets_depois['depois'] = 'depois'
plotting_Sets_antes.columns = ['faixa_series','periodo']
plotting_Sets_depois.columns= ['faixa_series','periodo']
results_sets = pd.concat([plotting_Sets_antes, plotting_Sets_depois], ignore_index=True)
count_sets = sns.countplot(x='faixa_series', hue='periodo', data=results_sets)
plt.show()

##ANÁLISE DAS FREQUÊNCIA DE TREINO
fre_table = pd.crosstab(dataframe['Frequência antes'],dataframe['Frequência de treino'])
print(fre_table.head)
fre_square_bhapkar = SquareTable(fre_table, shift_zeros =False).homogeneity(method='bhapkar')
fre_square_mcnemar = SquareTable(fre_table, shift_zeros=False).symmetry()
print('Frequência | Bhapkar Statistic= %.2f, p = %.2f' % (fre_square_bhapkar.statistic, fre_square_bhapkar.pvalue))
class_test_fre = McNemar_test(dataframe)
results_McNemar_fre = class_test_fre.bowkerPHmc('Frequência antes', 'Frequência de treino')
print(results_McNemar_fre)
plotting_Fre_antes = dataframe[['Frequência antes']]
plotting_Fre_antes['antes'] = 'antes'
plotting_Fre_depois = dataframe[['Frequência de treino']]
plotting_Fre_depois['depois'] = 'depois'
plotting_Fre_antes.columns = ['frequencia','periodo']
plotting_Fre_depois.columns = ['frequencia','periodo']
results_Fre = pd.concat([plotting_Fre_antes, plotting_Fre_depois], ignore_index=True)
count_Fre = sns.countplot(x='frequencia', hue='periodo', data=results_Fre)
plt.show()