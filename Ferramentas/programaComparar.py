#Programa de Comparação de Relatorios
"""
Objetivo:
    -Pegar duas bases de dados(relatorios) que sera selecionado pelo usuario e comparar valores
    -Os valores a serem de compras feitas pegos serão:
        -compras feitas pela mesma pessoa
        -valor
        -horario(que pode variar até 10segundos de um relatorio para o outro)
    -O sistema deve compliar isso em um arquivo CSV mostrando o valor comprado por cada pessoa e tambem mostrar os valores que nao conseguiram ser associados 
""" 

import pandas as pd

df = pd.read_excel(r"C:\Users\user\Desktop\MovimentaçãoPixBB (5).xls")
print(df.head())