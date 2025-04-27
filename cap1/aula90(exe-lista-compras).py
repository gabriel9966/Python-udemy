import os
lista_compras = []
while True:
    inp = input("[i]nserir [a]pagar [l]istar:")

    if inp == "i":

        try:
            valor_inserido = input("Digite o valor a ser inserido:")
            lista_compras.append(valor_inserido)
            os.system("cls")
        except:
            os.system("cls")
            print("Erro")

    elif inp == "a":

        if lista_compras == []:
            print("Lista Vazia")
        else:
            try:
                valor_removido = int(input("Digite o indice a ser removido:"))
                os.system("cls")
                lista_compras.pop(valor_removido)
            except:
                os.system("cls")
                print("Digite um índice válido")

    elif inp == "l":
        
        if lista_compras == []:
            print("Lista Vazia")
        else:
            os.system("cls")
            for indice, item in enumerate(lista_compras):
                print(indice,item)

    else:
        print("Opção inválida")