#Ex044 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
#- À vista dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- Em até 2x no catão: preço normal
#- Em 3x ou mais no cartão: 20% de juros
preço = float(input('Qual o valor do produto? R$'))
print('''Formas de pagamento:
[ 1 ] À vista no dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto) 
[ 3 ] Em até 2 vezes no cartão (preço normal)
[ 4 ] Em 3 vezes ou mais no cartão (20% de juros) ''')
forma = int(input('Qual a forma de pagamento escolhida? '))
if forma == 1:
    valor = preço - (preço * 10 /100)
    print(f'O valor final à vista com 10% de desconto fica R${valor:.2f}')
elif forma == 2:
    valor = preço - (preço * 5 / 100)
    print(f'O valor à vista no cartão com 5% de desconto fica R${valor:.2f}')
elif forma == 3:
    print(f'Parcelado em duas vezes o produto mantém o preço de R${preço:.2f}')
elif forma == 4:
    valor = preço + (preço * 20 / 100)
    print(f'O valor em 3 ou maias vezes fica em R${valor:.2f}')
else:
    print('Valor informado inválido, tente novamente')