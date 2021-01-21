"""
Ex075 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.

"""
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')),
       int(input('Digite o ultimo número: ')))
print(f'Você digitou os números {num}')
print(f'Você digitou o número 9, {num.count(9)} vez(es)')
if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na posição {num.index(3)+1}')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ')
for c in num:
    if c % 2 == 0:
        print(c)

