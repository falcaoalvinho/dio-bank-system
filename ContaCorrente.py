from Conta import Conta
from Cliente import Cliente
from Historico import Historico

class ContaCorrente(Conta):
    def __init__(
            self,
            saldo: float,
            numero: int,
            agencia: str,
            cliente: Cliente,
            historico: Historico,
            limite: float,
            limite_saques: int
            ):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.__limite = limite
        self.__limite_saques = limite_saques

    def set_limite(self, limite: float):
        self.__limite = limite

    def set_limite_saques(self, limite_saques: int):
        self.__limite_saques = limite_saques
