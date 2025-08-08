# Definção da classe conta, contém apenas construtor e alguns atributos
class conta:
    def __init__(self, numero_conta: int, cpf_cliente: str):
        self.numero_conta: int = numero_conta
        self.cpf_cliente: str = cpf_cliente
        self.agencia: str = "0001"
        self.saldo: float = 0
