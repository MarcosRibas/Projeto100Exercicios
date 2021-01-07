'''Ex022 Crie um programa que leia o nome completo de uma pessoa, e mostre:
O nome com todas as letras maiúsculas:
O nome com todas as letras minúsculas:
Quantas letras sem considerar espaço
Quantas letras tem o primeiro nome:'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
espaco = nome.count(' ')
tot = len(nome) - espaco
print('Seu nome tem {} letras'.format(tot))
pnome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(pnome[0])))
