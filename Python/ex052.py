#Ex052 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite o número inteiro que você quer saber se é primo: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c),end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')