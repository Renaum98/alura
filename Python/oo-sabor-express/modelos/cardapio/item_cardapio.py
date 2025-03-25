from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome.title()
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass    