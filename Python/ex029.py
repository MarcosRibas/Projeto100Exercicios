'''Ex029 Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.'''

print('------RADAR ELETRONICO------')
vel = int(input('Velocidade do carro(km/h): '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Velocidade a cima do permitido. Multa de R${:.2f}'.format(multa))
else:
    print('Velocidade dentro do permitido')