from Saque import saque
from Deposito import deposito

class transacao(saque, deposito):
    def __init(self, valor: float = 0):
        self.__valor = valor
    
    
    def set_valor(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.set_saldo(conta.get_saldo() + self.valor)
