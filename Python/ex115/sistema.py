"""Ex115a “Criando um menu” Vamos criar um menu em Python, usando modularização."""
"""Ex115b “Arquivos com Python” Vamos ver como fazer acesso a arquivos usando o Python."""
"""Ex115c "Finalizando o projeto" Vamos finalizar o projeto de acesso a arquivos em Python."""
from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
cabeçalho('MENU PRINCIPAL')
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
       lerArquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'\033[31mERRO! opção {resp} é inválida\033[m')


