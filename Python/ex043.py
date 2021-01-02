#Ex043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o status, de acordo
#com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do peso
#- Entre 18.5 e 25: Peso Ideal
#- Entre 25 até 30: Sobrepeso
#- Acima de 40: Obesidade mórbida
peso = float(input('Qual seu peso? (kg)'))
altura = float(input('Qual sua altura?'))
imc = peso / (altura * altura)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está obeso')
else:
    print('Você tem obesidade mórbida')
