"""
Ex071 ”Simulador de caixa eletrônico” Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunta ao usuário qual será o valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues.
OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1.

"""
print('-=-=-=CAIXA ELETRÔNICO=-=-=-')
n = int(input('Qual o valor que você deseja sacar? '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')