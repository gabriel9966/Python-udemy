#muda o fluxo do código
#if = se
#elif = senão se , adiciona condições
#else = senão
# else e elif dependem do if 
# Tem apenas um if e um else no bloco condicional

entrada = input('Digite se quer "entrar" ou "sair" :')

#bloco condicional
if entrada == 'entrar':#condição 1 
    #bloco de código
    print('Você entrou')
elif entrada == 'entrar':#condição 1 
    #bloco de código
    print('Você entrou2')
elif entrada == 'sair':#condição 2
    print('Você saiu')
else:
    print('Nenhuma opção aceita')

print('saiu do bloco')
#variável = guarda valor/dado na memória
idade = int(input('Digite sua idade:'))

if idade  == 18:
    print("Você tem 18 anos!")

elif idade > 18:
    print("Você tem mais que 18 anos") 
else:
    print("Você tem menos que 18 anos")
