cpf = input("Digite os primeiros 9 números do seu CPF:").strip()


numeros_cpf = []
multiplicador = 10
multiplicador2 = 11
soma_cpf = 0
soma_cpf2 = 0 


#Limpando cpf
for i in cpf:
    if i.isdigit() == True:
        numeros_cpf.append(int(i))

        



# começo validação
#validação1
for i in range(9):
    soma_cpf += (numeros_cpf[i] * multiplicador)
    multiplicador-=1
#validação2

soma_cpf = (soma_cpf * 10) % 11
numeros_cpf.append(soma_cpf)

for i in range(10):
    soma_cpf2 += (numeros_cpf[i] * multiplicador2)
    multiplicador2-=1

soma_cpf2 = (soma_cpf2 * 10) % 11


print("Seu CPF é :",*numeros_cpf , soma_cpf2)


