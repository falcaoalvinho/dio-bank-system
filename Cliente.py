from PessoaFisica import PessoaFisica
from datetime import date

class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str, contas: list):
        super().__init__(cpf, nome, data_nascimento)
        self.__endereco = endereco
        self.__contas   = contas

    def set_endereco(self, endereco: str) -> None:
        if endereco.strip() != "":
            self.__endereco = endereco

    #FIX ME: Criar classes Conta
    def adcionar_conta(self, conta) -> None:
        self.__contas.append(conta)
        
    #FIX ME: Criar classes Conta e Transacao
    def realizar_transacao(self, conta, transacao) -> None:
        pass
