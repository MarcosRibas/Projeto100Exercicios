"""
Ex108  “Formatando moedas” Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga
mostrar os números como um valor monetário formatado.
"""
from ex108 import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'Diminuido 10%, temos {moeda.moeda(moeda.diminuir(preço, 10))}')