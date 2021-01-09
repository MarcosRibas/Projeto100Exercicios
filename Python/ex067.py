"""
Ex067 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número for negativo
"""
c = 1
n = 0
print('------GERADOR DE TABUADAS-----')
while n >= 0:
    n = int(input('Qual valor você gostaria de saber a tabuada? (Se deseja sair digite um número negativo)\n'))
    if n < 0:
        break
    else:
        for c in range(1, 11):
            t = n * c
            print(f'{n} x {c} = {t}')
print('Saindo...')