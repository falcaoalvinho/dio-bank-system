from Historico import historico
from Transacao import transacao

class conta():
    def __init__(self):
        self.__saldo     = None
        self.__numero    = None
        self.__agencia   = None
        self.__historico = None

    def nova_conta(self, numero: int) -> None:
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = "000"
        self.__historico = historico()

    def get_saldo(self) -> float:
        return self.__saldo
    
    def get_numero(self) -> int:
        return self.__numero
    
    def get_agencia(self) -> str:
        return self.__agencia
    
    def get_historico(self) -> historico:
        return self.__historico
    
    def sacar(self, valor: float) -> bool:
        if -valor <= 0:
            transacao = transacao()
            transacao.set_valor(-valor)
            transacao.registrar(self)

            return True
        return False
        

    def depositar(self, valor: float) -> bool:
        if valor >= 0:
            transacao = transacao()
            transacao.set_valor(valor)
            transacao.registrar(self)

            return True
        return False

    

