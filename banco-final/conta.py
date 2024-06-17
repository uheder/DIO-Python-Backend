from cliente import Cliente
from historico import Historico
import transacoes


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
    
    @property
    def numero(self) -> int:
        return self._num_conta
    @property
    def agencia(self)-> str:
        return self._agencia
    
    @property
    def cliente(self)-> Cliente:
        return self._cliente
    
    @property
    def historico(self)-> Historico:
        return self._historico
    
    def sacar(self, valor: float)-> bool:
        if self._saldo - valor < 0:
            print('Erro: Saldo insuficiente.')
            return False
        elif valor < 0:
            print('Erro: não é possivel sacar menos que 0 reais.')
            return False
        print('Saque realizado com sucesso!')
        self_saldo -= valor
        return True

    def depositar(self, valor: float)-> bool:
        if valor <= 0:
            print('Erro: não é possivel depositar valores menores ou iguais a 0 reais')
            return False
        self._saldo += valor
        print('Deposito realizado com sucesso!')
        return True


class ContaCorrente(Conta):
    def __init__(self, limite: float = 500, limite_saques: int = 3) -> None:
        self.limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor: float):
        total_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo']
             == transacoes.Saque.__name__]
        )

        excedeu_saque = valor > self.limite
        excedeu_limite_saques = total_saques >= self._limite_saques

        if excedeu_saque:
            print('Erro: Valor de saque excede o limite de saque')
        elif excedeu_limite_saques:
            print('Erro: Limite de saques diarios excedido')
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self) -> str:
        return f'Agencia: {self.agencia}\nNum. Conta: {self.numero}\nCliente: {self._cliente}'

class PessoaFisica(Cliente):
    def __init__(self, cpf: int, nome: str, data_nasc: str, endereco: str) -> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
        super().__init__(endereco)