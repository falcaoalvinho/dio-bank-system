from Saque import Saque
from Deposito import Deposito
from Conta import Conta

class Transacao(Saque, Deposito):
    def __init(self, valor: float = 0):
        self.__valor = valor
    
    
    def set_valor(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
