import csv
modelo_ = {
    'competições_tipos':['Regional', 'Nacional', 'Jogos Parapan-americanos', 'Mundial','Jogos Paralímpicos'],
    'treino':['Centro de treinamento em Universidade', 'Academia de musculação', 'Studio de Personal Trainer', 'Centro de treinamento em Universidade','Em casa'],
    #treino_durante_pan = treino_antes_pan
    'equipamentos':['Peso livre (exercícios feitos com barras, anilhas e halteres)', 'Máquina (exercícios feitos na máquina)', 'Exercícios com peso corporal', 'Resistência variável (Correntes, elásticos, board)'],
    #equipamentos_antes = equipamentos_no_momento 
    'articulação_envolvida_treino_atual':['Membros superiores', 'Tronco (abdome, lombar)', 'Membros inferiores']
    }

item_colunas_ = ['competição', 'treino_antes_pandemia', 'materias_antes', 'onde_treina_durante_pandemia', 'grupos_articulares_envolvidos_treino_atual', 'material_utilizado_no_momento']

fieldnames_ = ['data_hora','termo','nome','idade','sex','height','kgs','estado','escolaridade',
            'pessoa_casa','pessoas_que_moram','trabalho','deficiencia','anos_treino','competição','categoria_m','categoria_f','desempenho_ultima_competição',
            'treino_antes_pandemia','treino_possui_equipamentos?','comprou_equipamento','treinava_coachXsozinho','grupos_musculares_antes','materias_antes',
            'faixa_reps_antes','faix_series_antes','exercicios_alem_supino','faixa_reps_antes_alem_supino','faixa_reps_antes_alem_supino','frequencia_antes',
            'anda_motivado_antes_pandemia','treina_durante_pandemia','continua_treinando_durante_pandemia','onde_treina_durante_pandemia','comprou_equipamentos_halterofilismo',
            'quais_foram_compŕados','esta_treinando','grupos_articulares_envolvidos_treino_atual','material_utilizado_no_momento','faixa_reps_durante_pandemia','faixa_series_durante_pandemia',
            'exercicios_alem_supino_no_momento','faix_reps_no_momento_alem_supino','faixa_reps_mais_utilizada','atual_frequencia_treino','anda_motivado_durante_pandemia','atualmente_estou?','desempenho_percepcao_atleta']

arquivo_ = "/home/well/GoogleDrive/PROGRAMAÇÃO/ProjetO_erick/erick raw data.csv"




with open(arquivo_) as dados_mestrado:  
    data = csv.DictReader(dados_mestrado, delimiter= ',', fieldnames=fieldnames_)
    lista_pessoas = list()
    
    for row in data: 
        #Para cada linha no conjunto de linhas, dentro de row 1 linha, dentro de data todas
        #row passa por toda a linha e muda na hora que terminar
        pessoa = {
            'Idde': row['idade'],
                'Altura':row['height'],
                'Sexo':row['sex'],
                'Peso (kgs)':row['kgs'],
                'Estado':row['estado'],
                'Escolaridade':row['escolaridade'],
                'Número de moradores: ':row['pessoa_casa'],
                'Quem mora? ':row['pessoas_que_moram'],
                'Tipo de trabalho':row['trabalho'],
                'Tipo de deficiência':row['deficiencia'],
                'Tempo de treino':row['anos_treino'],
                'Categoria masculino':row['categoria_m'],
                'Categoria feminino':row['categoria_f'],
                'Desempenho última competição':row['desempenho_ultima_competição'],
                'Compra de equipamentos':row['comprou_equipamento'],
                'Faixa de R.antes':row['faixa_reps_antes'],
                'Faixa de S.antes':row['faix_series_antes'],
                'Ex além supino':row['exercicios_alem_supino'],
                'Faixa de Reps antes além supino':row['faixa_reps_antes_alem_supino'],
                'Faixa de Séries antes além supino':row['faixa_reps_antes_alem_supino'],
                'Frequência antes':row['frequencia_antes'],
                'Motivação antes':row['anda_motivado_antes_pandemia'],
                'Treina durante pandemia':row['treina_durante_pandemia'],
                'Continua treinando durante pandemia':row['continua_treinando_durante_pandemia'],
                'Comprou equip':row['comprou_equipamentos_halterofilismo'],
                'Quais comprados':row['quais_foram_compŕados'],
                'Continua treinando':row['esta_treinando'],
                'Faixa de Reps durante pandemia':row['faixa_reps_durante_pandemia'],
                'Faixa de Séries durante pandemia':row['faixa_series_durante_pandemia'],
                'Ex além supino durante pandemia':row['exercicios_alem_supino_no_momento'],
                'Faixa de Reps durante além supino':row['faix_reps_no_momento_alem_supino'],
                'Faixa de Reps mais utilizadas ':row['faixa_reps_mais_utilizada'],
                'Frequência de treino':row['atual_frequencia_treino'],
                'Motivação durante':row['anda_motivado_durante_pandemia'],
                'Como estou':row['atualmente_estou?'],
                'Percepção de desempenho':row['desempenho_percepcao_atleta']}
        for item in item_colunas_:
            row[item] = row[item].split(';')
            for categoria in modelo_: 
                for comparador in modelo_[categoria]:
                    print(modelo_[categoria])

                    break
                    if comparador in row[item]:
                        pessoa[comparador] = 1
                    else:
                        pessoa[comparador] = 0                
        lista_pessoas.append(pessoa)
    #print(lista_pessoas[1])