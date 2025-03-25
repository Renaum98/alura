from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

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
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)


    def __str__(self):
        '''Modifica a forma de saida do objeto para string'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurante(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {'Avaliação'.ljust(25)} | {"Status"}')
        for rest in cls.restaurantes:
            print(f'{rest._nome.ljust(25)} | {rest._categoria.ljust(25)} | {str(rest.media_avaliacoes).ljust(25)} | {rest.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    
    def receber_avaliacao(self, cliente, nota):

        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Nenhuma avaliação'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante: {self._nome}\n')
        for index,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{index}.Nome:{item._nome.ljust(25)} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{index}.Nome:{item._nome.ljust(25)} | Preço: R${item._preco:.2f} | Descrição: {item.tamanho}'
                print(mensagem_bebida)
