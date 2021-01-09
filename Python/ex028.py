'''Ex028 Escreva um programa que faça o computador ‘’pensar’’ um número inteiro entre 0 e 5 e peça para o
usuário descobrir qual foi o número escolhido pelo computador.'''
import random
print('Pensando...')
l = [1, 2, 3, 4, 5]
s = random.choice(l)
n = int(input('Tente adivinhar o número que estou pensando. Dica: é um número de 1 a 5: \n'))
if s == n:
    print('Uau! Você acertou!')
else:
    print(f'ERROU (voz do Faustão). O número que pensei foi {s}. Tente novamente')

