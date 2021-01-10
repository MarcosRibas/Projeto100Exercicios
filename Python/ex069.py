"""
Ex069 “Análise de dados do grupo” Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada o programa deverá perguntar se o usuário quer ou  não continuar. No final mostre:
a)	Quantas pessoas tem mais de 18 anos
b)	Quantos homens foram cadastrados
c)	Quantas mulheres tem menos de 20 anos.
"""
print('-=-=-=-=-CADASTRO DE PESSOAS-=-=-=-=-')
maior = homem = mulher= 0
continua = 's'
while continua == 's':
    print('-'*38)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = str(input('Sexo: [M/F]')).strip().lower()[0]
    if sexo == 'm':
        homem += 1
    if sexo == 'm' and idade < 20:
        mulher += 1
    print('-'*38)
    resp = str(input('Quer continuar? [S/N]\n')).strip().lower()[0]
    if resp != 's':
        break
print(f'{maior} pessoa(s) cadastrada(s) tem mais de 18 anos.\nO número de homens cadastrados foi de {homem}\n'
      f'E o número de mulheres com menos de 20 anos foi de {mulher}')


