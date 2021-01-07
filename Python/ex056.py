# Ex056 Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos.
somaidade = 0
meioridade = 0
menor = 0
for c in range(1, 5):
    print('Pessoa número {}'.format(c))
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [m/f] ')).strip()
    idade = int(input('Idade: '))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        menor = menor + 1
print('A média de idade do grupo é de {:.0f} anos'.format(somaidade / 4))
print('O homem mais velho tem {} anos, e se chama {}'.format(maioridade, nomevelho))
print('No grupo citado há {} mulher(res) com menos de 20 anos'.format(menor))
