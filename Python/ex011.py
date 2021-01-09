'''Ex011 Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta a área de 2m².'''

larg = float(input('Qual a largura de sua parede? '))
alt = float(input('Qual a altura de sua parede? '))
m = larg * alt
tinta = m / 2
print(f'sua parede tem {m:.2f}m². E para pinta-la, precisará de {tinta:.1f} litro(s) de tinta')

