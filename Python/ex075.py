"""
Ex075 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.

"""
num = ()
for c in range(1, 5):
    num = int(input(f'Digite o {c}° valor: '))
print(num)