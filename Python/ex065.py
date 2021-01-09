"""
Ex065 Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""
print('Digite quantos números inteiros quiser, e no final lhe mostrarei qual foi o maior valor, o menor e a média entre todos eles')
resp = 's'
valor = 0
c = 0
list = []


while resp == 's':
    x = int(input('Digite um valor: '))
    valor = valor + x
    c += 1
    list += [x]
    resp = str(input('Quer continuar digitando mais valores? [sim/não]\n')).strip().lower()[0]
    media = valor / c
print(f'A média entre todos os valores lidos foi de {media:.1f}. O maior valor digitado foi de {max(list)}. E o menor valor digitado foi de {min(list)}.')
