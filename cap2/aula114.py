"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def idade(idade):
    return idade

def bom_dia():
    return 'Bom Dia'

def executa(saudacao,nome,bomdia,idade):
    return f'{saudacao(bomdia(),nome)} , {idade}'


print(
    executa(saudacao,"Gabriel",bom_dia,idade(30))
)
