import os
palavra_secreta = "perfume"
letras_acertadas = ""
tentativas = 0
while True:
    
    letra_digitada = input("Digite uma letra:")
    tentativas += 1
    print("Tentativa:",tentativas)

    #Valida a entrada
    if len(letra_digitada) > 1 :
        print("Digite apenas uma letra.")
        continue

    #verifica se a letra digita está na palavra
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # a formação da palavra
    palavra_formada = ""

    #esse bloco faz o controle para exibição da palavra 
    #percorre a palavra secreta
    for letra_secreta in palavra_secreta:
        #verifica se a letra da palavra secreta está nas letras acertadas
        if letra_secreta in letras_acertadas:
            palavra_formada+= letra_secreta
        else:
            palavra_formada+= "*"


    print(palavra_formada)
    
    #Controle para parar o jogo
    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("ACERTOU!")
        print("A palavra era :",palavra_secreta)
        break
    elif tentativas >=13 :
        print("PERDEU")
        break 
    
    