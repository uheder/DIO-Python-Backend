from abc import ABC
from cliente import Cliente
from conta import Conta
from datetime import datetime
import historico

class Transacao(ABC):
    pass

class Deposito(Cliente):
    pass

class Saque(Cliente):
    pass