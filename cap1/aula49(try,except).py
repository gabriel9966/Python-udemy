#Tratamento de exceções
# try -> tenta exceutar o código
#except -> captura a exceção
#exceção erro em tempo de execução
try:

    numero = input("Dobre o número digitado:")


    numero_float = float(numero)

    print(f"O número é {numero_float*2}")
except:
    print("Deu errado")



#try código que pode gerar uma exceção 
#exception código que sera executado caso a exceção aconteça

