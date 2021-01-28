'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
d = {}
gols = []
tot = 0
d['nome']=str(input('Nome: '))
quant_partidas = int(input(f'Quantas partidas {d["nome"]} jogou? '))
for c in range(1, quant_partidas+1):
    gol = (int(input(f'Quantos gols na partida {c}? ')))
    gols.append(gol)
    tot = tot + gol
d['gols'] = gols
d['total'] = tot
print('-='*20)
print(d)
print('-='*20)
for v, k in (d.items()):
    print(f'O campo {v} tem o valor {k}')
print('-='*20)
print(f'O jogador {d["nome"]} jogou {quant_partidas} partidas.')
cont = 1
for c in gols:
    print(f' => Na partida {cont}, fez {c} gols.')
    cont += 1
