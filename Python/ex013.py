"""Ex013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento."""
sal = float(input('Qual o salário atual? R$ '))
aum = sal + (sal*15/100)
print(f'O salario antigo de R${sal:.2f}, com o aumento de 15% fica em R${aum:.2f}')