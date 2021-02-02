"""
Ex101 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
"""
from datetime import datetime
now = datetime.now()
ano = (now.year)



def voto(a):
    idade = ano - a
    print('-'* 30)
    print(f'Com {idade} anos: ',end='')
    if idade < 16:
        print('NÃO VOTA.')
    elif idade >= 16 and idade < 65:
        print('VOTO OBRIGATÓRIO.')
    else:
        print('VOTO PCIONAL.')


voto(2015)