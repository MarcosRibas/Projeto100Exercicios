#Ex018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, radians, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O angulo {} tem o SENO de {:.2f}'.format(a, seno))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(a, cos))
print('O ângulo {} tem o TANGENTE de {:.2f}'.format(a,tan))
