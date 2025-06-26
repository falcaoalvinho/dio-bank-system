class conta():
    def __init__(self, numero_conta, cpf_cliente):
        self.numero_conta: int = numero_conta
        self.cpf_cliente: str = cpf_cliente
        self.agencia: str = '0001'
        self.saldo: float = 0