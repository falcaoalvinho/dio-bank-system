class cliente():
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome: str = nome;
        self.data_nascimento: str = data_nascimento
        self.cpf: str = cpf
        self.endereco: str = endereco
        self.contas: list = []
