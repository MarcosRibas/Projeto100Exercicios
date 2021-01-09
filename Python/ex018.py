#Ex018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, radians, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print(f'O angulo {a} tem o SENO de {seno:.2f}')
print(f'O ângulo {a} tem o COSSENO de {cos:.2f}')
print(f'O ângulo {a} tem o TANGENTE de {tan:.2f}')
