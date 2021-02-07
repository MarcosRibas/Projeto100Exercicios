"""Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLErros:
    print('O sim Pudim não está acessivel no momento')
else:
    print('Tudo ok. Consegui acessar o site Pudim com sucesso.')