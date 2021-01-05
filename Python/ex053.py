#Ex053 Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: apos a sopa
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.strip()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')