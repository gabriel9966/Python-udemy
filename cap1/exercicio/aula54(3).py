nome = input("Digite o seu nome:")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) <= 6 and len(nome) >= 5:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")