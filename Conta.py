from Cliente import Cliente
from Historico import Historico
from Transacao import Transacao

class Conta():
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico):
        self.__saldo     = saldo
        self.__numero    = numero
        self.__agencia   = agencia
        self.__cliente   = cliente
        self.__historico = historico

    def nova_conta(self, cliente: Cliente, numero: int):
        return Conta(saldo = 0, numero = numero, agencia = "000", cliente = cliente, historico = Historico())

    def saldo(self) -> float:
        return self.saldo
    
    def sacar(self, valor: float) -> bool:
        if -valor <= 0:
            transacao = Transacao
            transacao.set_valor(-valor)
            transacao.registrar(self)

            return True
        return False
        

    def depositar(self, valor: float) -> bool:
        if valor >= 0:
            transacao = Transacao
            transacao.set_valor(valor)
            transacao.registrar(self)

            return True
        return False

    

