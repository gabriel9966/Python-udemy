
while True:
    try:
        num1 = float(input("Digite o primeiro numero"))
        num2 = float(input("Digite o segundo numero"))
        operador = ("Digite um operador + , - , * , / :")

        if operador == "+":
            print(num1 + num2)
        elif operador == "-":
            print(num1 - num2)
        elif operador == "*":
            print(num1 * num2)
        elif operador == "/":
            print(num1 / num2)
        else:
            print("Operador Inválido")

        sair = input("Digite [s] para sair e [f] para ficar:").lower().startswith('s')

        if sair:
            break


    except Exception as erro:
        print(erro)