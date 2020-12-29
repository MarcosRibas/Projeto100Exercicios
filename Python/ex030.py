#Ex030 Crie um programa que leia um número inteiro e mostre se ele é PAR ou IMPAR.
n = int(input('Digite um número inteiro: '))
x = n % 2
if x == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))