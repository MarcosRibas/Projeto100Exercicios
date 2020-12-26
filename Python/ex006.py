#Ex006 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
n = int (input('Digite um número: '))
d = n * 2
t = n * 3
r = math.sqrt(n)

print('O dobro de {} é {} \nO seu triplo é: {} \nE sua raiz quadrada é {:.1f}'.format(n, d, t, r))
