class Saque:
    def __init__(self, valor: float = 0):
        self.__valor = valor

    def set_valor(self, valor: float = 0) -> None:
        self.__valor = valor