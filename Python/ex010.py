'''Ex010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos Dólares ela pode comprar. Considere o dólar atual'''
real = float(input('Quantos reais você tem? R$'))
dolar = real / 5.22
print('Seu dinheiro convertido em doláres fica em: US${:.2f}'.format(dolar))
