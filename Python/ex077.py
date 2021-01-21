"""
Ex077 Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são suas vogais.
"""
palavras = ('Brasil', 'Sol', 'Praia', 'Feijoada', 'Carnaval', 'Caipirinha', 'Futebol', 'Natureza')
for c in palavras:
    print(f'Na palavra {c.upper()} temos as vogais: ')
    for n in c:
        if n in 'aeiou':
            print(n)