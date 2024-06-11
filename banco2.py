from datetime import datetime
from sys import exit
from time import sleep

print("Bem-vindo ao meu banco!")

AGENCIA = '0001'
extrato = ''
MAX_SAQUE_DIA = 3
saldo = 500
saques = []

cont_saque_dia = 0
usuarios = []

def criar_usuario(nome, data_nasc, cpf, end):
    pass

def criar_conta(agencia, conta, usuario):
    pass

def depositar(valor, saldo, extrato, /):
    if valor <= 0:
        return "Valor de deposito inválido."
    saldo += valor
    extrato += f'Depósito: R$ {valor:.2f}, {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
    print("Depósito bem sucedido.")
    return saldo, extrato
    
def sacar(valor, cont_saque_dia):
    if saldo - valor < 0:
        return "Saldo insuficiente."
    elif valor > 500:
        return "Valor do saque excede o limite por transação."
    elif cont_saque_dia > MAX_SAQUE_DIA:
        return "Chegou ao limite de saques diários, operação recusada."
    
    saques.append(data)
    if data in saques:
        cont_saque_dia += 1
    else:
        cont_saque_dia = 1
    saldo -= valor
    extrato += f'Saque: R$ {valor:.2f}, {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
    print("Saque bem sucedido.")
    return saldo, extrato

def gerar_extrato(saldo, extrato):
    if extrato:
        print(f"{extrato} Seu saldo atual é: R$ {saldo: .2f}")
    else:
        print(f"Sem operações recentes.\nSeu saldo é: R$ {saldo:.2f}")

def menu():
    while True:
        option = input("""Selecione a opção desejada:\n(U) Criar usuário\n(C) Criar conta\n(D) Depositar\n(S) Sacar\n(L) Listar contas\n(E) Gerar extrato\nPressione a tecla Enter para sair.\n""")

        # Pega data do dia da consulta para contagem de saques
        global data
        data = datetime.now().strftime("%d %m %Y")
        if option == '':
            exit(0)
        
        elif option.upper() == 'D':
            valor = float(input("Quanto deseja depositar? "))
            depositar(valor, saldo, extrato) 
            sleep(1)

        elif option.upper() == 'S':
            saque = float(input("Informe o valor a ser sacado: "))
            sacar(saque, cont_saque_dia)
            sleep(1)
            
        elif option.upper() == 'E':
            gerar_extrato(saldo, extrato)
            sleep(1)
        
        elif option.upper() == 'C':
            criar_conta()
            sleep(1)
        
        elif option.upper() == 'U':
            criar_usuario()
            sleep(1)

        else:
            print("Operação não reconhecida.")
    exit(0)

if __name__ == '__main__':
    menu()