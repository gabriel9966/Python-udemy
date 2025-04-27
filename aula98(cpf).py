cpf = input("Digite seu CPF:").strip()


numeros_cpf = []
multiplicador = 10
soma_cpf = 0


#Limpando cpf
for i in cpf:
    if i.isdigit() == False:
        pass
    else:
        numeros_cpf.append(int(i))



# começo validação

for i in range(9):
    soma_cpf += (numeros_cpf[i] * multiplicador)
    multiplicador-=1





soma_cpf = (soma_cpf * 10) % 11


print(0 if soma_cpf > 9 else soma_cpf)

