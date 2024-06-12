from abc import ABC
from conta import Conta
from datetime import datetime

class Transacao(ABC, Conta):
    data = datetime.now().strftime('%d/%m%Y %H:%M:%S')

    @staticmethod
    def registrar():
        pass

    def depositar(self, saldo, valor):
        self._saldo = saldo
        self._valor = valor
        

    def sacar(self, saldo, valor, LIMITE_SAQUE):
        self._saldo = saldo
        self._valor = valor
        self._LIMITE_SAQUE = LIMITE_SAQUE
        

