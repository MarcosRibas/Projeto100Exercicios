"""
Ex064 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
"""
quant = 0
x = 0
soma = 0
while x != 999:
    x = int(input('Digite um valor inteiro que deseja adicionar a lista, ou o cógigo "999" para sair\n'))
    quant += 1
    if x != 999:
        soma = soma + x
print(f'Você digitou {quant} valores, que somados resultam em {soma}')
