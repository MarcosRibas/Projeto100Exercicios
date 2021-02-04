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

