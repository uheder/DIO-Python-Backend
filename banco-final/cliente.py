class Cliente:
    def __init__(self, cpf: int, nome: str, data_nasc: str, endereco: str, contas: list):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.contas = contas
    
