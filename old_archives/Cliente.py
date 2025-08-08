# Definição da classe cliente, contém apenas seu construtor e alguns atributos
class cliente:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        self.nome: str = nome
        self.data_nascimento: str = data_nascimento
        self.cpf: str = cpf
        self.endereco: str = endereco
        self.contas: list = []
