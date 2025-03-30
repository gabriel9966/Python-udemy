horario = int(input("Digite a hora:"))

if horario <= 24 and horario >= 0 :
    if horario <= 11 and horario >= 0:
        print("Bom Dia !!")
    elif horario <= 17 and horario > 11:
        print("Boa Tarde!!")
    else:
        print("Boa Noite!!")
else:
    print("Horário inválido")