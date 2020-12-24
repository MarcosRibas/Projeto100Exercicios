#Ex012 Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
val = float(input('Qual o valor do produto? R$ '))
desc = val - (val * 5 / 100)
print('O valor de R${:.2f}, com o desconto de 5% fica em R${:.2f}.'.format(val, desc))