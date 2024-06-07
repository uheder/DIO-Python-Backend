from datetime import datetime
from sys import exit
from time import sleep

print("Bem-vindo ao meu banco!")

saldo = 500
extrato = ''
saques = []
cont_saque_dia = 0

while True:
    option = input("Selecione a opção desejada:\n(a) Depositar\n(b) Sacar\n(c) Extrato\nPressione a tecla Enter para sair. ")

    # Pega data do dia da consulta para contagem de saques
    data = datetime.now().strftime("%d %m %Y")
    if option == '':
        exit(0)
    
    elif option == 'a':
        deposito = int(input("Quanto deseja depositar? "))
        if deposito <= 0:
            print("Valor de deposito inválido, retornando ao menu principal.")
            sleep(2)
            continue
        saldo += deposito

        #adiciona o valor do deposito mais a data e hora da operação
        extrato += f'Depósito: R$ {deposito:.2f}, {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
        print("Depósito bem sucedido. Retornando ao menu principal")
        sleep(2)

    elif option == 'b':
        saque = int(input("Informe o valor a ser sacado: "))
        
        # Lida com operações recusadas de saque
        if saldo - saque < 0:
            print("Saldo insuficiente.")
            sleep(1)
            continue
        elif saque > 500:
            print("Valor do saque excede o limite por transação.")
            continue
        elif cont_saque_dia >= 3:
            print("Chegou ao limite de saques diários, operação recusada.")
            continue

        # Lida com operações de saque bem sucedida
        saques.append(data)
        if data in saques:
            cont_saque_dia += 1
        else:
            cont_saque_dia = 1

        saldo -= saque
        print("Saque bem sucedido. Retornando ao menu principal.")
        sleep(2)

        # Adiciona o valor de saque mais a data e hora da operação
        extrato += f'Saque: R$ {saque:.2f}, {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'

    elif option == 'c':
        if extrato:
            print(f"{extrato} Seu saldo atual é: R$ {saldo: .2f}")
        else:
            print(f"Sem operações recentes. \n Seu saldo é: R$ {saldo:.2f}")
    else:
        print("Operação não reconhecida.")
exit(0)