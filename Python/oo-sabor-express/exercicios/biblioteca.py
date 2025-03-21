from ex06 import Livro

livro1 = Livro('o conto de aia','joseph mones', 1998)
livro2 = Livro('a fada', 'Mary lan', 2004)

print(f'Status: {livro1._disponivel}')

Livro.emprestrar(livro1)

print(f'Status: {livro1._disponivel}')

Livro.livros = [livro1, livro2]

ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")

