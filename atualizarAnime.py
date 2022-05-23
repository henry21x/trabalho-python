import json
import os
clear = lambda: os.system('cls')

dadosAtualizados = {}

def atualizarAnime ():
    while True:
        clear()

        indices = []
        file = open('dados_animes.json', 'r', encoding='utf-8')
        data = file.read()
        data = json.loads(data)
        
        for i, item in enumerate(data, start=0 ): 
            print(f'{i}. {item}')                 
            indices.append(i)
        
        while True:                               
            i = int(input('Digite o número do anime o qual deseja alterar: '))
            if i in indices:
                break
            print('[Esse número não corresponde a nenhum anime!]')

        clear()
               
        dadosAtualizados['nome'] = input('Nome do anime: ').lower()
        dadosAtualizados['genero'] = input('Gênero: ').lower()
        dadosAtualizados['episodios'] = input('Quantidade de episodios: ')
        dadosAtualizados['ano'] = input('Ano do lançamento: ')
        dadosAtualizados['estudio'] = input('Nome do Estúdio de Animação: ').lower()
        dadosAtualizados['criador'] = input('Nome do criador da obra: ').lower()

        del data[i]
        data.insert(i,dadosAtualizados) 
        
        
        file = open('dados_animes.json', 'w+', encoding='utf-8')
        data = json.dumps(data)
        file.write(data)
        file.close()

        clear()
        print(f'Alteração feita com sucesso!\n{dadosAtualizados}')


        opcao = input('Deseja alterar outro anime? [S/N]: ').upper()
        while True:
            if opcao in 'SN':

                clear()
                break
            opcao = input('Digite apenas S ou N: ').upper()
                
        if opcao == 'N':
            break




 
 


