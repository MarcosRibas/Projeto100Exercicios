'''
Ex081 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
a)	Quantos números foram digitados.
b)	A lista de valores de forma decrescente.
c)	Se o valor 5 foi digitado e está ou não na lista

'''

list = []
while True:
    n = int(input('Digite um número: '))
    list.append(n)
    next = str(input('Quer continuar?[s/n] ')).lower().strip()
    if next == 'n':
        break
print(f'Sua lista tem {len(list)} itens')
list.sort(reverse=True)
print(f'Os númeroas listados em ordem decrescente: {list}')
if 5 in list:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')