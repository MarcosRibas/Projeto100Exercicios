"""
Ex063 Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequência Fibonacci.
"""
print('SEQUÊNCIA DE FIBONACCI')
n = int(input('Quantos termos que você quer mostrar?\n'))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' → fim')