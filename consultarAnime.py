import json
import os
clear = lambda: os.system('cls')

def consultarAnime():
    while True: 
        file = open('dados_animes.json', 'r', encoding='utf-8')
        data = file.read()
        data = json.loads(data)

        print('[Nome] | [Genero] | [Episodios] | [Ano] | [Estudio] | [Criador]')
        while True:
            filtro = input('Digite uma das opções acima para filtrar: ').lower().removeprefix('[').removesuffix(']')
            if filtro == 'nome':
                break
            elif filtro == 'genero':
                break
            elif filtro == 'episodios':
                break
            elif filtro == 'ano':
                break
            elif filtro == 'estudio':
                break
            elif filtro == 'criador':
                break
            clear()
            print('[ERRO!] Verifique se escreveu corretamente.')
            print('[Nome] | [Genero] | [Episodios] | [Ano] | [Estudio] | [Criador]')
        
        filtro2 = input(f'Digite o {filtro}: ').lower()

        if ([i for i in data if i[filtro] == (filtro2)]): 
            clear()
            animesFiltrado = ([i for i in data if i[filtro] == (filtro2)])
            for x in animesFiltrado:
                print(x)
            print(f'De acordo com o filtro [{filtro.capitalize()} - {filtro2.capitalize()}], esses são os animes que correspondem a busca.')
        
        elif not any(d[filtro] == filtro2 for d in data):
            clear()
            print('Nenhum anime corresponde a busca!')

        opcao = input('Deseja realizar outra consulta? [S/N]: ').upper()
        while True:
            if opcao in 'SN':

                clear()
                break
            opcao = input('Digite apenas S ou N: ').upper()
                
        if opcao == 'N':
            break


    
        


