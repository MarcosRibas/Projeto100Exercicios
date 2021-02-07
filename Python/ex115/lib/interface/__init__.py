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


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc