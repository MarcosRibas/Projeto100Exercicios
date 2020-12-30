#Ex033 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o ultimo número: '))
lista = [n1, n2, n3]
max = max(lista)
min = min(lista)
print('O maior número dessa lista é {}. E o menor número dessa lista é {}.'.format(max, min))

