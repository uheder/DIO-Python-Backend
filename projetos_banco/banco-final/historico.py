from transacoes import Transacao
from conta import Conta
from datetime import datetime

class Historico(Conta):
    def __init__(self)->list:
        self._transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
        })

    @property
    def transacoes(self):
        return self._transacoes

