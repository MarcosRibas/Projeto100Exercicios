#Ex012 Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
val = float(input('Qual o valor do produto? R$ '))
desc = val - (val * 5 / 100)
print(f'O valor de R${val:.2f}, com o desconto de 5% fica em R${desc:.2f}.')