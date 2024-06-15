from abc import ABC, abstractmethod, property
from conta import Conta
from datetime import datetime

class Transacao(ABC, Conta):
    def __init__(self, data: datetime):
        super().__init__(Conta.saldo)
        self.data = data
        
    @abstractmethod
    def registrar(self, conta: Conta):
        pass

    @property
    @abstractmethod
    def valor(self):
        pass

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    
    @property
    def valor(self)-> float:
        return self._valor
    
    def registrar(self, conta: Conta):
        saque = conta.sacar(self.valor)

        if saque:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self)-> float:
        return self._valor
    
    def registrar(self, conta: Conta):
        deposito = conta.depositar(self.valor)

        if deposito:
            conta.historico.adicionar_transacao(self)
