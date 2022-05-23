import json
import os
clear = lambda: os.system('cls')

def delAnime():
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
            i = int(input('Digite o número do anime que deseja deletar: '))
            if i in indices:
                break
            print('[Esse número não corresponde a nenhum anime!]')
        
        clear()
        print(data[i])
        confirmacao = input('Tem certeza de que deseja deletar esse anime? [S/N]: ').upper()
        
        while True:
            if confirmacao in 'SN':
                break
            print('[ERRO!] Digite apenas S ou N.')


        if confirmacao == 'N':
            break


        
        if confirmacao == 'S':
            del data[i]
            file = open('dados_animes.json', 'w+', encoding='utf-8')
            data = json.dumps(data)
            file.write(data)
            file.close()
            print('Anime deletado com sucesso!')
            
        
        

        opcao = input('Deseja deletar outro anime? [S/N]: ').upper()
        while True:
            if opcao in 'SN':

                clear()
                break
            opcao = input('Digite apenas S ou N: ').upper()
                
        if opcao == 'N':
            break

