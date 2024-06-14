from transacoes import Transacao
from conta import Conta

class Historico(Conta):
    def __init__(self, saldo: float)-> object:
        super().__init__(saldo)
        self.transacoes = []

    # def adicionar_transacao(transacao: Transacao):
    #     self.transacoes.append(transacao)


