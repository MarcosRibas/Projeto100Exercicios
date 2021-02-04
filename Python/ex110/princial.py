""" Ex110 “Reduzindo ainda mais seu programa” Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada
resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui. """
from ex110 import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}')
print(f'Diminuido 10%, temos {moeda.diminuir(preço, 10, True)}')