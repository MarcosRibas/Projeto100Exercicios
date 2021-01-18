'''
Seu programa deverá ler pelo teclado (entre 0 e 20) e mostra-lo por extenso.
Ex073 Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem
de colocação. Depois mostre:
a)	Apenas os 5 primeiros colocados
b)	Os últimos quatro colocados
c)	Uma lista com os times em ordem alfabética.
d)	Em que posição da tabela está o time Flamengo.
'''
tabela = ('São Paulo', 'Internacional', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense', 'Santos', \
         'Corinthians', 'Athletico','Ceará', 'Bragantino', 'Atlético- GO', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', \
         'Goiás', 'Coritiba', 'Botafogo')
print('-'*20)
print('Os times que estão se classificando para a libertadores:')
for c in (tabela[:5]):
    print(c)
print('-'*20)
print('Os times que estão na zona de rebaixamento: ')
for c in (tabela[16:20]):
    print(c)
print('Tabela em ordem alfabética: \n',(sorted(tabela)))
fla = (tabela.index('Flamengo'))+1
print(f'O Flamengo está na {fla}° posição')
