#Ex046 Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10
# até 0, com pausa de 1 segundo entre eles.
from time import  sleep
print('Vai começar a contagem regressiva para o ano novo...')
for c in range(10,0,-1):
    print(c)
    sleep(1)
print('Feliz ano novo!')