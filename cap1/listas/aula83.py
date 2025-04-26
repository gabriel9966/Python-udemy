'''
= - copia o valor (imultável)
= - aponta para o mesmo local na memória (multável)
'''

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

listaConcatenada = lista1 + lista2

print(listaConcatenada)

lista1.extend(lista2)

print(lista1)

l1 = [1,2,3]
l2 = l1
l2.append(4)
print(l1)

print(id(l1))
print(id(l2))