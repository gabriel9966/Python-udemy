# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa1 = {
    'nome':'Gabriel',
    'dade':20,
    'email':'abcd@hotmail.com',
    'emprego':'Desempregado',
    'l1': [0,1,2,3]
}

pessoa2 = pessoa1.copy()# cópia rasa

print(len(pessoa1))# Devolve o tamanho, a quantidade de chaves

print(pessoa1.keys())
print(pessoa1.values())
print(pessoa1.items())

pessoa1['l1'][1] = 999

print(pessoa1)
print(pessoa2)