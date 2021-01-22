'''
Ex079 Crie um programa onde o usuário possa digitar vários valores e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
list = []
while True:
    num = int(input('Digite o valor: '))
    if num in list:
        print('Valor já digitado, então não foi cadastrado a lista.')
    else:
        list.append(num)
        print('Valor cadastrado com sucesso.')
    resp = str(input('Quer continuar?[s/n] \n')).lower().strip()
    if resp == 'n':
        break
list.sort()
print(f'Os valores cadastrados foram: {list}')