"""
Ex100 Faça um programa que tenha uma lista chamada números e funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior
"""
from random import randint
from time import sleep
lista = []


def sorteia():
    c = 0
    while c < 5:
        lista.append(randint(1, 9))
        c += 1
    print(f'Sorteando 5 valores da lista: ',end='')
    for c in lista:
        print(f'{c} ', end='')
        sleep(0.5)
    print(f'PRONTO!')


def somaPar():
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando todos os valores pares de {lista}, temos {soma}')


sorteia()
somaPar()



