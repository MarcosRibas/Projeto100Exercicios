#Ex049 Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um
# laço for.
n = int(input('Digite o número no qual você deseja saber a tabuada: '))
for c in range(1, 11):
    t = n * c
    print(f'{c} x {n} = {t}')