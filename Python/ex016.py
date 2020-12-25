#Ex016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

num = float(input('Digite um número real: '))
print('O número inteiro do número {} é {:.0f}'.format(num, num))