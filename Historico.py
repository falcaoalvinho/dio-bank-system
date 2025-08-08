from Transacao import Transacao

class Historico:
    def __init__(self):
        self.__transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.__transacoes.append(transacao)
