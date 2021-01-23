'''
Ex080 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta (sem usar o sort()).
No final mostre a lista ordenada na tela.

'''
list = []
for c in range(0, 5):
    num = int(input(f'Digite um valor: '))
    if c == 0 or num > list[-1]:
        list.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(list):
            if num <= list[pos]:
                list.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {list}')