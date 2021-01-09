#Ex006 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
n = int (input('Digite um número: '))
d = n * 2
t = n * 3
r = math.sqrt(n)

print(f'O dobro de {n} é {d} \nO seu triplo é: {t} \nE sua raiz quadrada é {r:.1f}')
