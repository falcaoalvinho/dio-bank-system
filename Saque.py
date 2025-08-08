from abc import ABC, abstractmethod

class saque(ABC):
    def __init__(self, valor: float = 0):
        self.__valor = valor


    @abstractmethod
    def set_valor(self, valor: float = 0) -> None:
        self.__valor = valor
