
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


res_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

res_praca.adicionar_no_cardapio(bebida_suco)
res_praca.adicionar_no_cardapio(prato_paozinho)



'''res_praca.receber_avaliacao('Leando', 8)
res_praca.receber_avaliacao('Páblo', 2)
res_praca.receber_avaliacao('Paulo', 2)'''

#res_praca._ativo = True #Ativando o restaurante 
'''res_praca.alternar_estado() #forma de atualizar o estado do restaurante com um metodo entre true e false'''




def main():
    res_praca.exibir_cardapio

if __name__ == '__main__':
    main()