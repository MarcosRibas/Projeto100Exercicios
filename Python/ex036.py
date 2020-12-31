#Ex036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
val = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o valor do salário? R$'))
anos = int(input('Em quantos anos pretende pagar?'))
mes = (val / anos) / 12
if mes <= sal * 30 / 100:
    print('Empréstimo aprovado! As parcelas serão de R${:.2f}'.format(mes))
else:
    print('Empréstimo negado! As parcelas excedem 30% de seu salário. Tente novamente com um prazo maior')
