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
        option = input("""Selecione a opção desejada:\n(D) Depositar\n(S) Sacar\n(E) Gerar extrato\n
        (C) Criar Conta\n (L) Listar contas, (U) Criar usuárioPressione a tecla Enter para sair. """)

        # Pega data do dia da consulta para contagem de saques
        data = datetime.now().strftime("%d %m %Y")
        if option == '':
            exit(0)
        
        elif option == 'a':
            valor = float(input("Quanto deseja depositar? "))
            depositar(valor, saldo, extrato) 
            sleep(1)

        elif option == 'b':
            saque = float(input("Informe o valor a ser sacado: "))
            sacar(saque, cont_saque_dia)
            sleep(1)
            
        elif option == 'c':
            gerar_extrato()
        else:
            print("Operação não reconhecida.")
    exit(0)

if __name__ == '__main__':
    menu()