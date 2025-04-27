import decimal

num1 = 0.7
num2 = 0.1 

#Imprecisão do float

total = num1 + num2
print(total)

print(round(total,1))
print(decimal.Decimal(total,1))

# if total >= 0.8:
#     print("Maior ou igual a 0.8")
# else:
#     print("Menor que 0.8")
