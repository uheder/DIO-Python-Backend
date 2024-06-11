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
contas = []

def checa_cpf(cpf: int, usuarios: list):
    for user in usuarios:
        if user['cpf'] == cpf:
            return True
        return False
    
def criar_usuario(nome, data_nasc, cpf, endereco):
    usuarios.append({'cpf': cpf, 'nome': nome, 'data_nasc': data_nasc, 'endereço': endereco})
    print('Usuário criado com sucesso!')
    return usuarios

def criar_conta(agencia, num_conta, cpf, contas):
    for conta in contas:
        if conta['cpf'] == cpf:
            conta['contas'].append({'agencia': agencia, 'conta': num_conta})
            print('Conta criada com sucesso!')
            return contas
    contas.append({'cpf': cpf, 'contas': [{'agencia': agencia, 'conta': num_conta}]})
    print('Conta criada com sucesso!')
    return contas
def listar_contas(contas):
    for conta in contas:
        cpf = conta['cpf']
        for lista in conta['contas']:
            print(f"""\n
            CPF titular: {cpf}\n
            Agência: {lista['agencia']}\n
            Nº Conta: {lista['conta']}""")
    
def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        return "Valor de deposito inválido."
    saldo += valor
    extrato += f'Depósito: R$ {valor:.2f}, {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
    print("Depósito bem sucedido.")
    return saldo, extrato
    
def sacar(*, valor, cont_saque_dia):
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

def gerar_extrato(saldo, /, *, extrato):
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
            saldo, extrato = depositar(valor, saldo, extrato) 
            sleep(1)

        elif option.upper() == 'S':
            saque = float(input("Informe o valor a ser sacado: "))
            saldo, extrato = sacar(saque=saque, cont_saque_dia=cont_saque_dia)
            sleep(1)
            
        elif option.upper() == 'E':
            gerar_extrato(saldo,  extrato=extrato)
            sleep(1)

        elif option.upper() == 'U':
            cpf = int(input('Informe o numero do CPF do usuário: '))
            if checa_cpf(cpf, usuarios):
                print('CPF já cadastrado na lista de usuários')
                sleep(1)
                continue
            nome = input('Informe o nome do usuário: ')
            dt_nasc = input('Informe a data de nascimento no formato DD/MM/AAAA: ')
            endereco = input('Informe seu endereço com logradouro - nº - bairro - cidade - sigla do estado: ')
            criar_usuario(nome=nome, data_nasc=dt_nasc, cpf=cpf, endereco=endereco )
            sleep(1)

                
        elif option.upper() == 'C':
            cpf = int(input('Informe o CPF para o cadastro da conta: '))
            if not checa_cpf(cpf, usuarios):
                print('Usuario não possui cadastro, impossivel criar conta.')
                continue
            criar_conta(agencia=AGENCIA, num_conta=len(contas) + 1, cpf=cpf, contas=contas)
            sleep(1)
        
        
        elif option.upper() == 'L':
            if len(contas) == 0:
                print('Não existem contas cadastradas')
                sleep(1)
                continue
            listar_contas(contas)
            sleep(2)

        else:
            print("Operação não reconhecida.")
    exit(0)

if __name__ == '__main__':
    menu()