"""
Ex098 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
"""
from time import sleep
def linha():
    print('-='* 20)

def contador(i, f, p):
    if p == 0:
        print('ERRO! O número minimo do passo é 1')
    if p < 0:
        p *= -1
    if f > i:
        print(f'Contagem de {i} até {f} contando de {p} em {p}')
        while i <= f:
            print(f'{i} ', end='')
            sleep(0.3)
            i += p
        print()
    else:
        print(f'Contagem de {f} até {i} contando de {p} em {p}')
        while i >= f:
            print(f'{i} ', end='')
            sleep(0.3)
            i -= p
        print()

linha()
contador(1, 10, 1)
linha()
contador(2,10,2)
linha()
print('Agora é sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)