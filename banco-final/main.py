from abc import ABC
from time import sleep
from sys import exit

def menu():
    while True:
        option = input("""Selecione a opção desejada:\n(U) Criar usuário\n(C) Criar conta\n(D) Depositar\n(S) Sacar\n(L) Listar contas\n(E) Gerar extrato\nPressione a tecla Enter para sair.\n""")

    ### FIXME implementar logica de escolha ###
        
    exit(0)

if __name__ == '__main__':
    menu()