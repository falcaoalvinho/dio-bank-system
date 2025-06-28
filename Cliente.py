class cliente():
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        self.nome = nome;
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []
