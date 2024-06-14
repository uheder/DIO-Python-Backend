from cliente import Cliente
from datetime import date
from historico import Historico
from transacoes import Transacao


class Conta(Cliente):
    def __init__(self, cliente: Cliente, num_conta)-> None:
        super().__init__(Cliente.cpf)
        self._saldo = 0
        self._agencia = '0001'
        self._num_conta = num_conta
        self._cliente = cliente
        self._historico = Historico()

    # decorador gerador de conta
    @classmethod
    def nova_conta(cls, cliente: Cliente, num_conta: int) -> object:
        return cls(num_conta, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo
    

    def sacar(self, valor: float)-> bool:
        if self._saldo - valor < 0:
            return False
        
        # FIXME implementar funcao registrar na classe Transacao
        Transacao.registrar(saque)
        self_saldo -= valor
        
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