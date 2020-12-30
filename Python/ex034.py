#Ex034 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para inferiores ou iguais o aumento é de 15%.

sal = float(input('Qual o salário? R$'))
if sal <= 1250:
    aum = sal + (sal * 15 / 100)
    print('O salário teve um aumento de 15%, e agora é de R${:.2f}'.format(aum))
else:
    aum = sal + (sal * 10 / 100)
    print('O salário teve um aumento de 10%, e agora é de R${:.2f}'.format(aum))