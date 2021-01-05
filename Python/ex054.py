#Ex054 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores. (considerando maioridade 21 anos)
from datetime import datetime
now = datetime.now()
ano = (now.year)
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input('Digite o ano do nascimento da {}° pessoa:\n'.format(c)))
    idade = ano - nasc
    if idade < 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Das pessoas que você citou, {} são maiores de idade, e {} não são'.format(maior, menor))

