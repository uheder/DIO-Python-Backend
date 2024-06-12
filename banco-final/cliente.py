from conta import Conta

class Cliente:
    def cadastrar(self, cpf, nome, dt_nasc, endereco):
        self.cpf = cpf
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.endereco = endereco
        
        if cpf in Conta.contas:
            return False
        return True
