"""Ex074 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados s também indique o menor e o maior valor que estão na tupla
"""
from random import randint
s = (randint(1,10), randint(1,10), randint(1,10), randint(1, 10), randint(1, 10))
print(f'Números sorteados: {s}')
print(f'O maior número sorteado foi {max(s)}, e o menor foi {min(s)}')




