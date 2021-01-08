"""
Ex062 Melhore o Ex061, perguntando para o usuário se ele quer mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 termos.
"""
p = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = p
c = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while c <= tot:
        print('{} → '.format(termo), end='')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?\n'))
print('fim')