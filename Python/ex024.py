#Ex024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

nome = str(input('Digite o nome da cidade: ')).strip().upper().split()
if nome[0] == "SANTO":
    print('O nome da cidade começa com a palavra "Santo"')
else:
    print('O nome da cidade não começa com a palavra "Santo"')




