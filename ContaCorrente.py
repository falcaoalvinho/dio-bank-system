from Conta import conta
from Cliente import cliente
from Historico import historico

class contaCorrente(conta):
    def __init__(self,):
        super().__init__()
        self.__limite        = None
        self.__limite_saques = None

    def get_limite(self) -> float:
        return self.__limite
    
    def get_limite_saques(self) -> float:
        return self.__limite_saques

    def set_limite(self, limite: float) -> None:
        self.__limite = limite

    def set_limite_saques(self, limite_saques: int) -> None:
        self.__limite_saques = limite_saques
