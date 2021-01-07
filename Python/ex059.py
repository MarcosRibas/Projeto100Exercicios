#Ex059 Crie um programa que leia dos valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em casa caso.

print('----CALCULADORA----')
num = 8
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
while num != 5:
    num = float(input('''Qual a ação você deseja aplicar aos valores? {} e {}
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] Qual é maior
    [ 4 ] novos valores
    [ 5 ] sair\nOpção escolhida: '''.format(n1, n2)))
    if num == 1:
        soma = n1 + n2
        print('O valor de {} somado ao valor de {} tem o resultado de {}'.format(n1, n2, soma))
    elif num == 2:
        mult = n1 * n2
        print('O valor {} multiplicado pelo valor {} tem o resultado de {}'.format(n1, n2, mult))
    elif num == 3:
        if n1 > n2:
            print('O valor de {} é maior do que o valor de{}'.format(n1, n2))
        elif n2 > n1:
            print('O valor de {} é maior que o valor de {}'.format(n2, n1))
        else:
            print('Os valores são iguais')
    elif num == 4:
        print('Digite novos valores: ')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif num == 5:
        print('Saindo...')
    else:
        print('Opção inválida, tente novamente')

