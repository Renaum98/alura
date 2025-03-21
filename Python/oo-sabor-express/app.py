
from modelos.restaurante import Restaurante

res_praca = Restaurante('praça', 'gourmet')
res_praca.receber_avaliacao('Leando', 8)
res_praca.receber_avaliacao('Páblo', 5)
res_praca.receber_avaliacao('Paulo', 2)



def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()