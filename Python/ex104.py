"""
Ex104 Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'ERRO! o valor digitado não é um número inteiro. Tente novamente.')
        else:
            return n

n1 = leiaInt('Digite um número Inteiro: ')

print(f'Você digitou o número {n1}')