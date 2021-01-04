#Ex048 Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.
s = 0
for c in range(0,500,3):
    if c % 2 == 1:
        s = s + c
print('A soma de somados todos os números impáres múltiplos de três no intervalo de 1 a 500 é {}'.format(s))