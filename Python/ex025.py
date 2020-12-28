#Ex025 Crie um programa que leia o nome de uma pessoa e dia se ela tem ''SILVA'' no nome.

nome = str(input('Digite seu nome: ')).strip().lower()

silva = nome.find('silva')
if silva == -1:
    print('O nome não tem "silva"')
else:
    print('O nome tem "silva"')
