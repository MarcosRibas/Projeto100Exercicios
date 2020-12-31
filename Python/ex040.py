#Ex040 Crie um programa que calcule duas notas de um aluno e calcule sua média, mostrando a mensagem no final,
# de acordo com a média atingida:
#- Média abaixo de 5.0:
#REPROVADO
#- Média entre 5.0 e 6.9:
#RECUPERAÇÃO
#- Média 7.0 ou superior:
#APROVADO
n1 = float(input('Nota um: '))
n2 = float(input('Nota dois: '))
media = (n1 + n2) / 2
print('Sua média é de {}'.format(media))
if media < 5:
    print('Está REPROVADO')
elif media >= 5 and media < 7:
    print('Ficou em RECUPERAÇÃO')
else:
    print('Parabéns! Está APROVADO')