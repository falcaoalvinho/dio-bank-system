from Transacao import transacao

class historico:
    def __init__(self):
        self.__transacoes = []

    def adicionar_transacao(self, transacao: transacao):
        self.__transacoes.append(transacao)
