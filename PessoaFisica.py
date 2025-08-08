from datetime import date

class pessoaFisica:
    def __init__(self):
        self.__cpf = None
        self.__nome = None
        self.__data_nascimento = None

    def get_cpf(self) -> str:
        return self.__cpf
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_data_nascimento(self) -> date:
        return self.__data_nascimento

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_data_nascimento(self, data_nascimento: date) -> None:
        self.__data_nascimento = data_nascimento
