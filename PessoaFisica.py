from datetime import date


class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_data_nascimento(self, data_nascimento: date) -> None:
        self.__data_nascimento = data_nascimento
