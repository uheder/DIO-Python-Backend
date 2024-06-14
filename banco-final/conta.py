from cliente import Cliente

class Conta(Cliente):
    num_conta = 0
    def __init__(self, agencia:int, saldo: float, transacoes: list):
        super().__init__(Cliente.cpf)
        self.saldo = saldo
        self.transacoes = transacoes
    

    
    pass
