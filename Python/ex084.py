'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
list = []
pessoas = []
mai = men = 0
while True:
    nome = str(input('Nome: '))
    list.append(nome)
    peso = float(input('Peso: '))
    list.append(peso)
    if len(pessoas) == 0:
        mai = men = list[1]
    else:
        if list[1] > mai:
            mai = list[1]
        if list[1] < men:
                men = list[1]
    pessoas.append(list[:])
    list.clear()
    resp = str(input('Quer continuar? [s/n] \n')).lower().strip()
    if resp == 'n':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {mai}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ',end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}', end='')