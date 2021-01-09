''' Ex014 Escreva um programa que converta uma temperatura digitada em °C e
converta para °F.'''

c = int(input('Qual é a temperatura em °C? '))
f = (c * 9/5) + 32
print(f'{c}°C convertidos ficam em {f:.1f}°F')