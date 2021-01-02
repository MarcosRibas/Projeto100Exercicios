#Ex045 Crie um programa que faça o computador jogar Jokenpô com você.
import random
itens = ('Pedra','Papel', 'Tesoura')
s = [0, 1, 2]
computador = random.choice(s)
print('O computador escolheu: {}'.format(itens[computador]))
print('Vamos jogar JOKENPÔ?')
print('''Para escolher pedra digite:   [ 1 ]
Para escolher papel digite:   [ 2 ]
Para escolher tesoura digite: [ 3 ]''')
jogador = int(input('Qual você escolhe? '))
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogador - 1]))
if jogador == 1:
    if computador == 0:
        print('Jogo empatou')
    elif computador == 1:
        print('Computador venceu')
    elif computador == 2:
        print('Você venceu')
elif jogador == 2:
    if computador == 0:
        print('Você venceu')
    elif computador == 1:
        print('O jogo empatou')
    elif computador == 2:
        print('Computador venceu')
elif jogador == 3:
    if computador == 0:
      print('Computador venceu')
    elif computador == 1:
        print('Você venceu')
    elif computador == 2:
        print('O jogo empatou')

