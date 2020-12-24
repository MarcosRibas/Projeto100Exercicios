#Ex008 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
print('O valor de {:.0f}m, convetido em centimetros fica {:.0f}cm. E convertido em milimetros fica {:.0f}mm'.format(m, cm, mm))