''' Ex014 Escreva um programa que converta uma temperatura digitada em °C e
converta para °F.'''

c = int(input('Qual é a temperatura em °C? '))
f = (c * 9/5) + 32
print('{}°C convertidos ficam em {:.1f}°F'.format(c,f))