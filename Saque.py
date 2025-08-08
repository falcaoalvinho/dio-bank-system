from abc import ABC, abstractmethod

class Saque(ABC):
    def __init__(self, valor: float = 0):
        self.__valor = valor


    @abstractmethod
    def set_valor(self, valor: float = 0) -> None:
        self.__valor = valor
