import json
import os
from cadastrarAnime import *
from consultarAnime import *
from atualizarAnime import *
from deletarAnime import *

clear = lambda: os.system('cls')


def menu():
    while True:
        cabeçalho = ( '-' * 30)
        print(cabeçalho)
        print('[1] Cadastrar anime')
        print('[2] Consultar animes')
        print('[3] Alterar algum anime')
        print('[4] Deletar algum anime')
        print('[0] Sair')
        print(cabeçalho)

        opcao = int(input('Escolha uma opção: '))
        
        while opcao > 4 or opcao < 0:
            opcao = int(input('[Esse número não se encontra nas opções, tente novamente!]\nEscolha uma opção: '))
        
            
        if opcao == 1:
            clear()
            cadastrarAnime()

        if opcao == 2:
            clear()
            consultarAnime()
        
        if opcao == 3:
            clear()
            atualizarAnime()

        if opcao == 4:
            clear()
            delAnime()

        if opcao == 0:
            break

menu()
        
             
             





