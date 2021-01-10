#Ex058 Melhore o jogo do ex028 onde o computador “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
print('Pensando...')
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = random.choice(l)
n = 12
p = 1
print('Tente adivinhar o número que estou pensando')
while n != s:
    n = int(input('Qual número você escolhe? Dica: é um número de 0 a 10: \n'))
    if s == n:
        print('Uau! Você acertou!')
    else:
        print('ERROU (voz do Faustão). Tente novamente')
        p = p + 1

print(f'Você precisou de {p} tentativas')