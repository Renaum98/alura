
from modelos.restaurante import Restaurante

res_praca = Restaurante('praça', 'gourmet')
res_praca.receber_avaliacao('Leando', 8)
res_praca.receber_avaliacao('Páblo', 2)
res_praca.receber_avaliacao('Paulo', 2)

#res_praca._ativo = True #Ativando o restaurante 
res_praca.alternar_estado() #forma de atualizar o estado do restaurante com um metodo entre true e false

res_sushi = Restaurante('sushi express', 'japonesa')


def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()