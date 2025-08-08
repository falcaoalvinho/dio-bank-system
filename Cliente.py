from PessoaFisica import pessoaFisica
from Transacao import transacao
from Conta import conta
from datetime import date


class cliente(pessoaFisica):
    def __init__(self):
        super().__init__()
        self.__endereco = None
        self.__contas   = []

    def get_endereco(self):
        return self.__endereco
    
    def get_contas(self):
        return self.__contas

    def set_endereco(self, endereco: str) -> None:
        if endereco.strip() != "":
            self.__endereco = endereco

    def adcionar_conta(self, conta) -> None:
        self.__contas.append(conta)

    def realizar_transacao(self, conta: conta, transacao: transacao) -> None:
        transacao.registrar(conta=conta)

