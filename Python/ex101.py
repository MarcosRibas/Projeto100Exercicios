"""
Ex101 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
"""


def voto(a):
    from datetime import datetime
    ano = datetime.now().year
    idade = ano - a
    print('-'* 30)
    print(f'Com {idade} anos: ',end='')
    if idade < 16:
        return 'NÃO VOTA'
    elif idade <18 and idade > 65:
        return 'VOTO OBRIGATÓRIO.'
    else:
        return 'VOTO OPCIONAL.'
print(voto(2011))
