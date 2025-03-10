#Operadores lógicos servem para conectar expressões,palavra-chave usado para realizar operações sobre valores booleanos 
#and = e
#Todas as condições precisam ser verdadeiras

#São considerados valores Falsy
# 0 , 0.0 , '' , False

#entrada = input('[e] Entrar , [s] Sair :')
#senha = input('Digite sua senha:')

senha_permitida = '123456'

#if condição == True:
#   ...
#if entrada == 'e' and senha == senha_permitida:
    #print('Entrou')
#else:
    #print( 'Sair')

#Ele retorna exatamente o valor que foi considerado false

print('Começõu')
print(True and True)
#Avaliação de curto circuito
print(True and 0 and True)
print(True and '' and True)
print(bool(''))
print('' or 'A')

