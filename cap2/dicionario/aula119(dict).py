# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')


# {chave:valor}
# dict = dicionario = pares de chave - valor
#Organizar dados relacionados entre si
dicionario1 = {1:10,2:20,3:30}

print(dicionario1[1])

pessoa1 = {
    'nome':'Gabriel',
    'dade':20,
    'email':'abcd@hotmail.com',
    'emprego':'Desempregado'
}

print(pessoa1['emprego'])

chave = 'Carro'
pessoa1[chave] = 'uno'

print(pessoa1)

pessoa1[chave] = 'palio'
print(pessoa1)

del pessoa1[chave]# Apaga a chave

print(pessoa1)