from classe_para_novo_df import separator
import csv


#Parâmetros gerais 

modelo_ = {
    'treino':['Centro de treinamento em Universidade', 'Academia de musculação', 'Studio de Personal Trainer', 'Centro de treinamento em Universidade','Em casa'],
    #treino_durante_pan = treino_antes_pan
    'equipamentos':['Peso livre (exercícios feitos com barras, anilhas e halteres)', 'Máquina (exercícios feitos na máquina)', 'Exercícios com peso corporal', 'Resistência variável (Correntes, elásticos, board)'],
    #equipamentos_antes = equipamentos_no_momento 
    'articulação_envolvida_treino_atual':['Membros superiores', 'Tronco (abdome, lombar)', 'Membros inferiores']
    }

item_colunas_ = ['treino_antes_pandemia', 'materias_antes', 'onde_treina_durante_pandemia', 'grupos_articulares_envolvidos_treino_atual', 'material_utilizado_no_momento']

fieldnames_ = ['idade','sex','height','kgs','estado','escolaridade',
            'pessoa_casa','pessoas_que_moram','trabalho','deficiencia','anos_treino','competição','categoria_m','categoria_f','desempenho_ultima_competição',
            'treino_antes_pandemia','treino_possui_equipamentos?','comprou_equipamento','treinava_coachXsozinho','grupos_musculares_antes','materias_antes',
            'faixa_reps_antes','faix_series_antes','exercicios_alem_supino','faixa_reps_antes_alem_supino','faixa_reps_antes_alem_supino','frequencia_antes',
            'anda_motivado_antes_pandemia','treina_durante_pandemia','continua_treinando_durante_pandemia','onde_treina_durante_pandemia','comprou_equipamentos_halterofilismo',
            'quais_foram_compŕados','esta_treinando','grupos_articulares_envolvidos_treino_atual','material_utilizado_no_momento','faixa_reps_durante_pandemia','faixa_series_durante_pandemia',
            'exercicios_alem_supino_no_momento','faix_reps_no_momento_alem_supino','faixa_reps_mais_utilizada','atual_frequencia_treino','anda_motivado_durante_pandemia','atualmente_estou?','desempenho_percepcao_atleta']

#DATA NEEDE TO SEPARETE TO COLUMNS 

arquivo_ = "/home/well/GoogleDrive/PROGRAMAÇÃO/ProjetO_erick/erick raw data.csv"
#arquivo_ = 'C:/Users/wellm/Google Drive (w180947@dac.unicamp.br)/PROGRAMAÇÃO/ProjetO_erick/erick raw data.csv'

#Chamando a classe
obj_ = separator(arquivo=arquivo_, modelo=modelo_, item_colunas=item_colunas_, fieldnames=fieldnames_)
dados = obj_.split_string()

# #GERANDO o NOVO DATAFRAME
with open('dataset_headers_OK.csv', 'w') as df: 
    full_df = csv.writer(df, delimiter= ';')
    full_df.writerow(dados[0])
    for row in dados:
        full_df.writerow(row.values())
