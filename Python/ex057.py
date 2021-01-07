#Ex057 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
sexo = ''
while sexo != 'M' and sexo != 'F':
    print('Resposta inválida. Tente novamente.')
    sexo = str(input('Qual o seu sexo? [M/F]\n')).strip().upper()
if sexo == 'M':
    print('Dados coletados, seu sexo é masculino.')
if sexo == 'F':
    print('Dados coletados, seu sexo é feminino.')