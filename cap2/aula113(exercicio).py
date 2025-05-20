def mult(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado


total = mult(1,2,3,4,5,6,7,8,9,10)
print(total)

def par_impar(num):
    return f'{num} : Par' if num %2 == 0 else f'{num} : Impar'

print(par_impar(10))