print("Bem vindo a calculadora")

n1 = float(input("Digite o N1:"))
operador = input("Digite o operador (+,-,*,/)")
n2 = float(input("Digite o N2:"))

if operador == "+":
    print(f"Resultado {n1 + n2}")
elif operador == "-":
    print(f"Resultado {n1 - n2}")
elif operador == "*":
    print(f"Resultado {n1 * n2}")
elif operador == "/":
    if n2 == 0:
        print("Não é possível dividir por zero!")
    else:
        print(f"Resultado {n1 / n2}")
else:
    print("Operação inválida")
