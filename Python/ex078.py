'''
Ex078 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posições.
'''
list = []
maior = 0
c = 1
while c <= 5:
    num = int(input(f'Valor da posição {c}: '))
    list.append(num)
    if num > maior:
        maior = c
    c += 1
mai = max(list)
men = min(list)
print(f'O maior número digitado foi: {mai} nas posições: ')
for cont, c in enumerate(list):
    if c == mai:
        print(f'{cont+1}... ')
print(f'E o menor valor digitado foi {men} nas posições: ')
for cont, c in enumerate(list):
    if c == men:
        print(f'{cont+1}... ')


