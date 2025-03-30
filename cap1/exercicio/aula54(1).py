try:


    num = input("Digite um numero inteiro :")
#isdigit verifica se todos os caracteres são dígitos
    if(num.isdigit()):
        num = int(num)

        if(num % 2 == 0):
            print("O número é par")
        else:
            print("O número é impar")
    else:
        print("O número não é inteiro")

except:
    print("Não foi fornecido um valor valido")
    