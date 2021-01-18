'''
Ex072 Crie um programa que tenha uma tupla totalmente preenchida com contagem por extensão, de zero até vinte.
Seu programa deverá ler pelo teclado (entre 0 e 20) e mostra-lo por extenso.
'''
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número de 1 a 20: '))
print(ext[num])