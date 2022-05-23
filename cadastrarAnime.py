import json
import os
from timeit import repeat


def cadastrarAnime():
    clear = lambda: os.system('cls')

    while True:
        clear()
     
        salvarDados = {
            'nome': input('Nome do anime: ').lower(),
            'genero': input('Gênero: ').lower(),
            'episodios': input('Quantidade de episodios: '),
            'ano': input('Ano do lançamento: '),
            'estudio': input('Nome do Estúdio de Animação: ').lower(),
            'criador': input('Nome do criador da obra: ').lower(),
            }
        clear()
   
        file = open('dados_animes.json', 'r', encoding='utf-8')
        data = file.read()
        data = json.loads(data)
        data.append(salvarDados)
        
        file = open('dados_animes.json', 'w+', encoding='utf-8')
        data = json.dumps(data)
        file.write(data)
        file.close()

        continuar = input('[Cadastro realizado com sucesso!]\n[1] Cadastrar outro anime.\n[2] Voltar pro menu.\nEscolha uma das opções acima: ')
        while True:
            if continuar in '12':
                clear()
                break
            clear()
            continuar = input('[1] Cadastrar outro anime.\n[2] Voltar pro menu.\nDigite apenas 1 ou 2: ')
                
        if continuar == '2':
            break
    

    
    


    

    








