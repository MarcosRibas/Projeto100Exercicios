"""Ex061 Refaça o Ex051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while."""
p = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = p
c = 1
while c <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    c += 1
print('Fim')
