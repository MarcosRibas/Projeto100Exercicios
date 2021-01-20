"""Ex074 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados s também indique o menor e o maior valor que estão na tupla
"""
import random
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
x = []
for c in range(0,5):
    num = random.choice(s)
    x = num
print(x)




