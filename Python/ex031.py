#Ex031 Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.

km = int(input('Qual a distância da viagem (km)?'))
if km < 200:
    val = km * 0.50
else:
    val = km * 0.45

print('O valor da passam ficou R${:.2f}'.format(val))