"""
Ex103 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado completamente.
"""
def ficha(n = 'desconhecido', g = 0):
    print(f'O jogador {n} fez {g} gols')

nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int (gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
