# or = ou 

#print(True or False)

entrada = input('[e] Entrar , [s] Sair :')
senha = input('Digite sua senha:')

senha_permitida = '123456'

#if condição == True:
#   ...
if (entrada == 'e' or entrada == 'E') and senha == senha_permitida:
    print('Entrou')
else:
    print( 'Sair')
