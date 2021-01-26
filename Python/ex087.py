'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if c % 2 == 0:
            par += c
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
x = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos números pares da matriz é {par}')
print(f'A soma dos valores da terceira coluna é {x}')
print(f'O maior valor da segunda linha foi {max(matriz[1])}')
