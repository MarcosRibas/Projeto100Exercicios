#Ex055 Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lst=[]
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]
print('')
print('O Maior peso foi:', max(lst))
print('O Menor peso foi:', min(lst))