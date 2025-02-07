# not = inverte a lógica
#not True = False
#not False = True

print(not True)
print(not False)


senha = input('Digite a senha:')

if not senha != '123456':
    print('Senha correta!')
else:
    print('Senha incorreta')
