#Ex026 Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece pela última vez.
frase = str(input('Digite uma frase: ')).strip().lower()
n_a = frase.count('a')
f_a = frase.find('a')+1
l_a= frase.rfind('a')-1
print('Sua frase tem {} letras a'.format(n_a))
print('A letra A aparece pela primeira vez na {}° posição'.format(f_a))
print('A letra A apaerece pela ultima vez na {}° posição'.format(l_a))



