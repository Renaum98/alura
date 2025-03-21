class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        '''Criando um metodo construtor
        Atributos:
           - os atributos foram definidos com o metodo construtor usando o self para cada um deles
           - No atributo ativo foi usado um _ para definir o atributo como privado podendo somende ser alterado pelo @property'''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Modifica a forma de saida do objeto para string'''
        return f'{self._nome} | {self._categoria}'
    @classmethod
    def listar_restaurante(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for rest in cls.restaurantes:
            print(f'{rest._nome.ljust(25)} | {rest._categoria.ljust(25)} | {rest.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

Restaurante.listar_restaurante()