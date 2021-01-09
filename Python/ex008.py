#Ex008 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
print(f'O valor de {m:.0f}m, convetido em centimetros fica {cm:.0f}cm. E convertido em milimetros fica {mm:.0f}mm')