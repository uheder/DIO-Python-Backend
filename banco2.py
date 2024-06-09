from datetime import datetime
from sys import exit
from time import sleep

print("Bem-vindo ao meu banco!")

saldo = 500
extrato = ''
saques = []
cont_saque_dia = 0
usuarios = []

def criar_usuario(nome,data_nasc, cpf, end):
    pass

def criar_conta(conta, usuario):
    pass

def depositar(valor):
    global saldo, extrato
    if valor <= 0:
        print("Valor de deposito inválido.")
        return
    saldo += valor
    extrato += f'Depósito: R$ {valor:.2f}, {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
    print("Depósito bem sucedido.")
    
def sacar(valor):
    global saldo, extrato, cont_saque_dia
    if saldo - valor < 0:
        print("Saldo insuficiente.")
        return
    elif valor > 500:
        print("Valor do saque excede o limite por transação.")
        return
    elif cont_saque_dia > 3:
        print("Chegou ao limite de saques diários, operação recusada.")
        return
    
    saques.append(data)
    if data in saques:
        cont_saque_dia += 1
    else:
        cont_saque_dia = 1
    saldo -= valor
    extrato += f'Saque: R$ {valor:.2f}, {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
    print("Saque bem sucedido.")


def gerar_extrato():
    global saldo, extrato
    if extrato:
        print(f"{extrato} Seu saldo atual é: R$ {saldo: .2f}")
    else:
        print(f"Sem operações recentes.\nSeu saldo é: R$ {saldo:.2f}")

while True:
    option = input("Selecione a opção desejada:\n(a) Depositar\n(b) Sacar\n(c) Extrato\nPressione a tecla Enter para sair. ")

    # Pega data do dia da consulta para contagem de saques
    data = datetime.now().strftime("%d %m %Y")
    if option == '':
        exit(0)
    
    elif option == 'a':
        valor = float(input("Quanto deseja depositar? "))
        depositar(valor=valor) 
        sleep(1)

    elif option == 'b':
        saque = float(input("Informe o valor a ser sacado: "))
        sacar(valor=saque)
        sleep(1)
        

    elif option == 'c':
        gerar_extrato()
    else:
        print("Operação não reconhecida.")
exit(0)