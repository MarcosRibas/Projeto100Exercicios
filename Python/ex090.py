'''
Ex090 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
'''
d = {}
lista = []
d['nome'] = str(input('Nome: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
d['media'] = (n1 + n2) / 2
if d['media'] < 5:
    d['situação'] = 'REPROVADO'
elif d['media'] < 7:
    d['situação'] = 'EM RECUPERAÇÃO'
else:
    d['situação'] = 'APROVADO'
print(f'- nome é igual a {d["nome"]}\n- média é igual {d["media"]}\n- situação éigual a {d["situação"]}')
