nome = 'Gabriel'
altura = 1.7
peso = 90
imc = peso / altura ** 2
# f string serve para formatar uma string / :.2f formatar o número
mensagem = f'Meu nome é {nome}, tenho {altura:.2f} de altura, peso {peso} kg e meu imc é {imc:.3f}'

print(mensagem)