from datetime import date

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        self.cpf             = cpf
        self.nome            = nome
        self.data_nascimento = data_nascimento