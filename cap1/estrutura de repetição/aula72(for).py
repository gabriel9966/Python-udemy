txt = "Python"

for i in txt:
    print(i)

lista1 = [1,5,6,8,22]
# in verifica se algo está dentro ou precorre o objeto no caso do for
for a in lista1:#usado para percorrer iteraveis
    print(a)


indice = 0

while indice < len(txt):
    print(txt[indice],indice)
    indice+=1