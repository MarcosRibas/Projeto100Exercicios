#Ex007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Agora digite sua segunda nota: '))
media = (n1 + n2) / 2

print('Sua média é {:.1f}'.format(media))