#Escopo de função = as variáveis são acessiveis apenas dentro da função

'''
 Em Python, toda função tem um retorno. Se você não especificar um valor de retorno usando a palavra-chave return, a função irá retornar implicitamente o valor None
'''
#epois que o return é executado dentro de uma função, nada mais dentro daquela função é executado. 


def soma(a,b):
    return a + b


print(print())

print(soma(5,10))
print(type(soma(5,10)))