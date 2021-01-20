'''
Ex072 Crie um programa que tenha uma tupla totalmente preenchida com contagem por extensão, de zero até vinte.
Seu programa deverá ler pelo teclado (entre 0 e 20) e mostra-lo por extenso.
'''
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
       num = int(input('Digite um número de 0 a 20: '))
       if 0 <= num <= 20:
              break
       print('Números de 0 a 20. Tente novamente.')
print(f'Você digitou o número {ext[num]}')