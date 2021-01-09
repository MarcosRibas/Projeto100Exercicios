#Ex030 Crie um programa que leia um número inteiro e mostre se ele é PAR ou IMPAR.
n = int(input('Digite um número inteiro: '))
x = n % 2
if x == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é impar')