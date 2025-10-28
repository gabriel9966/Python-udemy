a = 'A'
b = 'B'
c = 1.111#                                             #parâmetro nomeado
formato = 'a={nome2} , b={nome1} ,c={nome3:.2f}'.format(nome1=a,nome2=b,nome3=c)#0,1,2
print(formato)

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato2 = string.format(
    nome1=a, nome2=b, nome3=c
)

#a,b,c = argumentos
texto = '{1}{2}{0}'.format(a,b,c)


print(formato2)
print(texto)


