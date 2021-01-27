'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime
now = datetime.now()
ano = (now.year)
d = {}
d['Nome']=str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
d['Idade'] = ano - nasc
d['CTPS']= int(input('Carteira de trabalho (0 não tem)'))
if d['CTPS'] == 0:
    print()
else:
    d['Ano de contratação'] = int(input('Ano da contratação: '))
    d['Salário'] = float(input('Salário: R$'))
    d['Apossentadoria'] = d['Idade'] + (d['Ano de contratação'] + 35) - datetime.now().year
for v, n in d.items():
    print(f'{v}: {n}')