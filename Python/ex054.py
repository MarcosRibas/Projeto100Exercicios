#Ex054 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores. (considerando maioridade 21 anos)
from datetime import datetime
now = datetime.now()
ano = (now.year)
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input(f'Digite o ano do nascimento da {c}° pessoa:\n'))
    idade = ano - nasc
    if idade < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print(f'Das pessoas que você citou, {maior} são maiores de idade, e {menor} não são')

