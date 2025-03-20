import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema','categoria':'Italiana','ativo':True},
                {'nome':'Sr Arabe','categoria':'Arabe','ativo':True}]

def exibir_nome_programa():
      '''Exibe o titulo do programa com um print'''
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
      '''Exibe as opções possiveis para serem escolhidas pelo usuario'''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar estado do restaurante')
      print('4. Sair\n')

def escolher_opcao():
      '''Roda o programa com base na escolha do usuario com uma condicional'''
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
      '''Caso houver alguma opção invalida ou não existente, a mensagem é exibida'''
      print('Opcão invalida!\n')
      voltar_menu()

def exibir_subtitulo(texto):
      '''Exibe o subtitulo ja formatado'''
      os.system('cls')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def listar_restaurantes():
      '''Listar todos restaurantes ja cadastrados'''
      exibir_subtitulo('Listando restaurantes')
      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
      for index,restaurante in enumerate(restaurantes):
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            situacao = 'Ativado' if restaurante['ativo'] else 'Desativado'

            print(f'{index}.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {situacao}')

      voltar_menu()

def cadastrar_novo_restaurante():
      '''Essa função é responsavel por cadastrar um novo restaurante
      
      inputs:
      - Nome do restaurante
      - Categoria

      Output:
      - Adiciona um novo restaurante a lista de restaurantes
      
      '''
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
      '''Ativa ou desativa restaurantes'''
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
      '''volta ao menu principal chamando a função main()'''
      input('\nDigite qualquer tecla para voltar ao menu.: ')
      main()

def finalizar_app():
      '''Finaliza a aplicação'''
      exibir_subtitulo('Finalizando o app')

def main():
    '''Função para resetar ou iniciar o sistema sempre que chamada'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()  

if __name__ == '__main__':
    main()