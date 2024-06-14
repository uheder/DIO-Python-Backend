from abc import ABC
from conta import Conta
from datetime import datetime

class Transacao(ABC, Conta):
    def __init__(self, data: datetime):
        super().__init__(Conta.saldo)
        self.data = data
    @staticmethod
    def registrar():
        pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass