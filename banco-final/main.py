from abc import ABC
from datetime import datetime
from time import sleep
from sys import exit

def menu():
    while True:
        option = input("""Selecione a opção desejada:\n(U) Criar usuário\n(C) Criar conta\n(D) Depositar\n(S) Sacar\n(L) Listar contas\n(E) Gerar extrato\nPressione a tecla Enter para sair.\n""")

        # Pega data do dia da consulta para contagem de saques
        global data
        data = datetime.now().strftime("%d %m %Y")
        
    exit(0)

if __name__ == '__main__':
    menu()