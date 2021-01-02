#Ex041 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JUNIOR
#- Até 20 anos: SÊNIOR
#- Acima: Master
from datetime import datetime
now = datetime.now()
ano = (now.year)
nasc = int(input('Em que ano o atleta nasceu? '))
idade = ano - nasc
print('Em {} o atleta completa {} anos'.format(ano, idade))
if idade < 9:
    print('Categoria: MIRIM')
elif idade >= 9 and idade < 14:
    print('Categoria: INFANTIL')
elif idade >=14 and idade < 19:
    print('Categoria: JUNIOR')
elif idade == 20 or idade == 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')