class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []
    
    def realiza_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

