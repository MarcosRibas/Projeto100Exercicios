"""Ex023 Faça um programa que leia um número de 1 a 9999 e mostre na tela cada um dos dígitos separados.
exemplo: digite um número: 1843
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1"""

n = int(input('Digite um número de 1 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
