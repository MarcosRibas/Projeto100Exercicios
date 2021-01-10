"""
Ex068 “Jogo par ou ímpar” Faça um programa que jogue par ou impar com o usuário. Jogo será interrompido quando o
jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
"""
import random
print('----VAMOS JOGAR PAR OU IMPAR?----')
continua = 0
vitorias = 0
while continua == 0:
    list = [0,1,3,4,5]
    comp = random.choice(list)
    resp = str(input('Você quer par ou impar? [P/I]\n')).strip().lower()[0]
    jog = int(input('Digite um valor: '))
    x = (comp + jog) % 2
    print(f'Eu joguei {comp}, e você jogou {jog}')
    if x == 0 and resp == 'p':
        print(f'{comp} + {jog} é par. Você venceu!')
        vitorias += 1
    elif x == 1 and resp == 'i':
        print(f'{comp} + {jog} é impar. Você venceu!')
        vitorias += 1
    elif x == 0 and resp == 'i':
        print(f'{comp} + {jog} é par. Eu venci!')
        continua = 1
    elif x == 1 and resp == 'p':
        print(f'{comp} + {jog} é impar. Eu venci!')
        continua = 1
print(f'Você conseguiu vencer {vitorias} vez(es) seguida(s)')

