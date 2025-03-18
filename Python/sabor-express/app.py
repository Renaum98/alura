import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema','categoria':'Italiana','ativo':True},
                {'nome':'Sr Arabe','categoria':'Arabe','ativo':True}]

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
      print('3. Alternar estado do restaurante')
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
                  ativar_desativar()
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
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def listar_restaurantes():
      exibir_subtitulo('Listando restaurantes')
      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
      for index,restaurante in enumerate(restaurantes):
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            situacao = 'Ativado' if restaurante['ativo'] else 'Desativado'

            print(f'{index}.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {situacao}')

      voltar_menu()

def cadastrar_novo_restaurante():
      exibir_subtitulo('Cadastro de novos restaurantes')

      nome_restaurante = input('\nDigite o nome do resturante que deseja cadastras: ').title().strip()
      categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ').title().strip()

      dados_do_restaurante = {'nome':nome_restaurante,
                              'categoria':categoria,
                              'ativo':False}

      restaurantes.append(dados_do_restaurante)

      print(f'Restaurante {nome_restaurante} cadastrado com sucesso.')

      voltar_menu()

def ativar_desativar():
      exibir_subtitulo('Alternando estado do restaurante')

      nome_restaurante = input('Digite o nome do restaurante que dejesa alternar o estado: ').strip().title()
      restaurante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['nome'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)

      if not restaurante_encontrado:
            print('O restaurante não foi encontrado')
      
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