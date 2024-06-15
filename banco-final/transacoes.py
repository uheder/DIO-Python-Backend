from abc import ABC, abstractmethod, property
from conta import Conta
from datetime import datetime

class Transacao(ABC, Conta):
    def __init__(self, data: datetime):
        super().__init__(Conta.saldo)
        self.data = data
        
    @abstractmethod
    def registrar(self):
        pass
    
    @property
    @abstractmethod
    def valor(self):
        pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass