def aumentar(preço, pc):
    aum = preço + (preço * pc / 100)
    return aum


def diminuir(preço, pc):
    dim = preço - (preço * pc / 100)
    return dim


def dobro(preço):
    dob = preço * 2
    return dob


def metade(preço):
    met = preço / 2
    return met

