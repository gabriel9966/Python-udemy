# Escopo =  área ou contexto onde uma variável ou função é acessível 

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.


O global em Python é uma palavra-chave usada para informar ao Python que uma variável, normalmente definida no escopo global, será acessada e modificada dentro de uma função ou outro escopo local.
"""

# Refatorar = editar código/reorganizar
#Escopo = onde uma variável existe e pode ser usada.


'''
A call stack (pilha de chamadas) é uma estrutura de dados usada para gerenciar a execução de funções. Ela segue o princípio LIFO (Last In, First Out), ou seja, a última função chamada é a primeira a ser completada.
'''

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)