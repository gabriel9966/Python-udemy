def func(*args,mult):
     for num in args:
        lista = []
        for n in range(1,mult+1):
            lista.append(num*n)
        print(lista)

    
#func(12,44,55)
func(1,2,3,4,5,mult=4)


#Closure é quando uma função interna "lembra" das variáveis do escopo externo, mesmo após esse escopo ter terminado.
#Closure (ou fechamento) em Python acontece quando uma função interna (filha) "lembra" do ambiente onde foi criada — ou seja, ela mantém acesso às variáveis da função externa (mãe),

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
        