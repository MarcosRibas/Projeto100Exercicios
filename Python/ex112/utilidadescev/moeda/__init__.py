def aumentar(preço=0, pc=0, formato = False):
    aum = preço + (preço * pc / 100)
    return aum if formato is False else moeda(aum)


def diminuir(preço=0, pc=0, formato = False):
    dim = preço - (preço * pc / 100)
    return dim if formato is False else moeda(dim)


def dobro(preço=0, formato = False):
    dob = preço * 2
    return dob if not formato else moeda(dob)


def metade(preço=0, formato = False):
    met = preço / 2
    return met if not formato else moeda(met)

def moeda(preço=0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço = 0, aum = 10, dim = 5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print(f'preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aum}% de aumento: \t{aumentar(preço, aum, True)}')
    print(f'{dim}% de desconto: \t{diminuir(preço, dim, True)}')

    print('-' * 35)

