#Ex005 Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número inteiro: '))
a = n - 1
s = n + 1
print('O número que você digitou é {} tendo seu antecessor {} e seu sucessor {}'.format(n, a, s))
