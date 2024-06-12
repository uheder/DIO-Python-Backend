from cliente import Cliente

class Conta(Cliente):
    contas = []
    def cadastra_conta(self, cliente, agencia):
        self.cliente = cliente
        self.agencia = agencia