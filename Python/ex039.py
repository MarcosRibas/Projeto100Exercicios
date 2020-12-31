#Ex039 Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar
#- Se já passou do tempo de alistamento.
#Seu programa deverá mostrar também quanto tempo falta ou que já passou do prazo.
#(se alista no ano que faz 18)
from datetime import datetime
now = datetime.now()
ano = (now.year)
nasc = int(input('Que ano você nasceu? '))
idade = ano - nasc
faltam = 18 - idade
passou = idade - 18
if idade == 18:
    print('Em {} você completa 18 anos. Precisa se alistar imediatamente: '.format(ano))
elif idade <= 17:
    print('Em {} você completa {} anos. Então, ainda faltam {} ano(s) pra você se alistar'.format(ano, idade, faltam))
else:
    print('Em {} você completa {} anos. Deveria ter se alistado a {} ano(s)'.format(ano, idade, passou))

