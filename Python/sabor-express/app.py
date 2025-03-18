import os

restaurantes = ['Sushi Plus','Pizza Express']

def exibir_nome_programa():
      print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░''')

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair\n')

def escolher_opcao():
      try:
            opc = int(input('Escolha uma opção: '))
            print(f'\nVocê escolheu a opcção: {opc}')

            if opc == 1:
                  print('Cadastrar restaurante')
                  cadastrar_novo_restaurante()
            elif opc == 2:
                  print('Listar restaurante')
                  listar_restaurantes()
            elif opc == 3:
                  print('Ativar restaurante')
            elif opc == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def opcao_invalida():
      print('Opcão invalida!\n')
      voltar_menu()

def exibir_subtitulo(texto):
      os.system('cls')
      print(texto)
      print()

def listar_restaurantes():
      exibir_subtitulo('Listando restaurantes')
      
      for index,restaurante in enumerate(restaurantes):
            print(f'{index}.{restaurante}')

      voltar_menu()

def cadastrar_novo_restaurante():
      exibir_subtitulo('Cadastro de novos restaurantes')

      nome_restaurante = input('\nDigite o nome do resturante que deseja cadastras: ').title().strip()
      restaurantes.append(nome_restaurante)
      print(f'Restaurante {nome_restaurante} cadastrado com sucesso.')

      voltar_menu()

def voltar_menu():
      input('\nDigite qualquer tecla para voltar ao menu.: ')
      main()

def finalizar_app():
      exibir_subtitulo('Finalizando o app')

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()  

if __name__ == '__main__':
    main()