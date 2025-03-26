from exercicios.ex07.ex07 import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def __str__(self):
        print(f'{self.marca} - {self.modelo} - {self.cor}')