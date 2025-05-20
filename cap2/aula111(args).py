#O *args permite que você passe vários argumentos posicionais para uma função, sem precisar saber quantos serão.

#Empacotamento	Junta vários valores em uma variável (tupla)
#Desempacotamento	Separa os valores em variáveis individuais
def soma(*args):#*args Empacotamento
    soma = 0
    

    for i in args:
        soma+= i
    
    return soma



print(soma(5,7,8,10,14))

print(sum((75,88,99)))
    