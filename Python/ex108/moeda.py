def aumentar(preço=0, pc=0):
    aum = preço + (preço * pc / 100)
    return aum


def diminuir(preço=0, pc=0):
    dim = preço - (preço * pc / 100)
    return dim


def dobro(preço=0):
    dob = preço * 2
    return dob


def metade(preço=0):
    met = preço / 2
    return met

def moeda(preço=0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

