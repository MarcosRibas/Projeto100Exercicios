#Ex051 Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final, mostre os
# 10 primeiros termos dessa progressão
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range (termo, 11, razao):
    print(c)