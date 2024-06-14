from cliente import Cliente
from datetime import date
from historico import Historico


class Conta(Cliente):
    def __init__(self, agencia: str, saldo: float, cliente: Cliente, historico: Historico, num_conta)-> None:
        super().__init__(Cliente.cpf)
        self._saldo = saldo
        self._historico = historico
        self._agencia = agencia
        self._num_conta = num_conta
        self._cliente = cliente

    def gera_saldo(self) -> float:
        return self._saldo
    
    def nova_conta(self, cliente: Cliente, num_conta: int) -> object:
        pass

    def sacar(self, valor: float)-> bool:
        pass
    def depositar(self, valor: float)-> bool:
        pass


class ContaCorrente(Conta):
    def __init__(self, limite: float, limite_saques: int) -> None:
        self.limite = limite
        self.limite_saques = limite_saques
    
class PessoaFisica(Cliente):
    def __init__(self, cpf: int, nome: str, data_nasc: date, endereco: str) -> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
        super().__init__(endereco)