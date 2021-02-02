"""Ex027 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
Último nome separadamente.
Exemplo: Ana Maria de Souza
Primeiro = Ana
Último = Souza"""

nome = str(input('Digite seu nome completo: ')).strip().split()
last = len(nome) - 1
print('Seu primeiro nome é: ', nome[0])
print('Seu ultimo nome é: ', nome[last])