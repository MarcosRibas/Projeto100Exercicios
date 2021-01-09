'''Ex026 Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece pela última vez.'''
frase = str(input('Digite uma frase: ')).strip().lower()
n_a = frase.count('a')
f_a = frase.find('a')+1
l_a= frase.rfind('a')-1
print(f'Sua frase tem {n_a} letras a')
print(f'A letra A aparece pela primeira vez na {f_a}° posição')
print(f'A letra A apaerece pela ultima vez na {l_a}° posição')



