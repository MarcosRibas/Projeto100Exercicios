"""
Ex070 “Estatísticas em produtos” Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final mostre:
a)	Qual é o total gasto na compra
b)	Quais produtos custam mais de R$1000
c)	Qual o nome do produto mais barato
"""
print('-=-=-=-INFOSTORE-=-=-=-')
nomes = []
list = [0]
tot = 0
menor = 1000000000
mais = []
resp = 's'
print('CADASTRO DE PRODUTOS')
while resp == 's':
    print('-'*23)
    n = str(input('Nome: ')).strip()
    nomes = [n]
    p = float(input('Valor: R$'))
    if p - menor:
        maisbarato = n
    list = [p]
    tot += p
    if p >= 1000:
        mais = mais + [n]
    print('-'*23)
    resp = str(input('Quer continuar? [S/N] \n')).strip().lower()[0]
    if resp != 's' and resp != 'n':
        print('Resposta inválida, tente novamente')
        resp = str(input('Quer continuar? [S/N] \n')).strip().lower()[0]
    if resp == 'n':
        break
min = min(list)
print(f'O total de sua compra deu R${tot:.2f}')
print(f'Produtos que foram mais de R$ 1000,00: {mais}')
print(f'O produto mais barato foi o produto {maisbarato}, com o valor de R${min:.2f}')



