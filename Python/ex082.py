'''
Ex082 Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
list = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    list.append(num)
    if num % 2 == 0:
        par.append(num)
        print('Número par cadastrado com sucesso!')
    else:
        impar.append(num)
        print('Número ímpar cadastrádo com sucesso!')
    next = str(input('Quer continuar? [s/n]\n')).lower().strip()
    if next == 'n':
        break
print(f'Os números cadastrados foram {list}\nSendo os pares: {par}, e os ímpares {impar}')