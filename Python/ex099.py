"""
ex099 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior
"""
from time import sleep
def linha():
    print('-=' * 30)
def maior(* num):
    lista = []
    linha()
    print('Analisando os valores passados...')
    sleep(1)
    for c in num:
        print(f'{c} ', end='')
        lista.append(c)
    print('Foram os valores ao todo')
    maior = max(lista)
    print(f'O maior valor informado foi {maior}')

maior(4, 2, 4, 6, 73, 2, 5)
maior(2, 5, 9, 1)