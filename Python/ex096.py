"""
Ex096 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno
"""


def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é {a:.1f}m²')


print('Controle de terrenos')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento(m): '))
area(larg, comp)
