"""Ex113 “Funções aprofundadas” Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! o valor digitado não é um número inteiro. Tente novamente.\033[m')
            continue
        except(KeyboardInterrupt):
            print('O usuário preferiu sair')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! o valor digitado não é um valor real. Tente novamente.\033[m')
        except(KeyboardInterrupt):
            print('O usuário preferiu sair.')
            return 0
        else:
            return n

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1}, e o número real {n2}')