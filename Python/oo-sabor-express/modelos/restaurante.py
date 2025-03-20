class Restaurante:
    def __init__(self, nome, categoria):
        '''Criando um metodo construtor'''
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        '''Modifica a forma de saida do objeto para string'''
        return f'{self.nome} | {self.categoria}'
        

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_pizza,restaurante_praca]

print(restaurante_praca)
print(restaurante_pizza)