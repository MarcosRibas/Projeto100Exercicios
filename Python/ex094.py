"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média
de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
"""
d = {}
pessoas = []
mulheres = []
idade = 0
while True:
    d.clear()
    d['nome'] = str(input('Nome: '))
    while True:
        d['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if d['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas "M" para masculino, ou "F" para feminino')
    if d['sexo'] == 'F':
        mulheres.append(d['nome'])
    d['idade'] = int(input('Idade: '))
    idade = idade + d['idade']
    pessoas.append(d.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas "S" para continuar, ou "N" para sair')
    if resp == 'N':
        break
print('-='*20)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'A média de idade é de {idade / len(pessoas):.0f} anos.')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'Lista de péssoas que estão acima da média de idade: ')
for c in pessoas:
    if c['idade'] > idade / len(pessoas):
        print(f'{c["nome"]}, com {c["idade"]} anos.')


