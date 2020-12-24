#Ex009 Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número inteiro e descubra qual é a sua taboada: '))
c = 1
while c <= 10:
    r = c * n
    print('{} X {} = {}'.format(c,n,r))
    c = c +1