num1 = int(input('Digite o primeiro numero :'))
num2 = int(input('Digite o segundo numero :'))

if num1 > num2:
    print(f'O primeiro número {num1} é maior que o segundo {num2}.')
elif num2 > num1:
    print(f'O segundo {num2} número é maior que o primeiro {num1}.')
else:
    print('Valores iguais')