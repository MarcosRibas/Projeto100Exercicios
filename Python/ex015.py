"""Ex015 Escreva um programa que pergunte a quantidade de km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o
preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado."""

km = int(input('Qual a distância percorrida? (km)'))
dia = int(input('Quantos dias ele foi alugado? '))
valor = (dia * 60) + (0.15 * km)
print(f'Valor a pagar R${valor:.2f}')