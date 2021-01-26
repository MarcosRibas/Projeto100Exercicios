'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
'''
from random import randint
from operator import itemgetter
d = {'Jogador1': randint(1,6),
     'Jogador2': randint(1,6),
     'Jogador3': randint(1,6),
     'Jogador4': randint(1,6)}
print('Valores sorteados: ')
for c in d:
    print(f'O jogador {c} tirou {d[c]} no dado')
print('-='*18)
rank = sorted(d.items(), key=itemgetter(1),reverse=True)
print('== RANKING DOS JOGADORES ==')
y = 1
for c in rank:
    print(f'{y}° lugar ficou {c[0]} com {c[1]}')
    y += 1
