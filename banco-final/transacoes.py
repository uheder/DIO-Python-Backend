from abc import ABC
from cliente import Cliente
from conta import Conta
from datetime import datetime
import historico

class Transacao(ABC, Conta):
    def __init__(self, data: datetime):
        super().__init__(Conta.saldo)
        self.data = data
    @staticmethod
    def registrar():
        pass

    def sacar(self):
        pass