"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""
def notas(*num, sit = ''):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas
    :param sit: valor opcional sobre a situação da média da turma
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = {}
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] < 7:
            r['situação'] = 'Regular'
        elif r['media'] < 5:
            r['situação'] = 'Ruim'
    return r


resp = notas(5, 2, 8, 4)
print(resp)