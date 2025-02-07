#muda o fluxo do código
#if = se
#elif = senão se , adiciona condições
#else = senão
# else e elif dependem do if 
# Tem apenas um if e um else no bloco condicional
entrada = input('Digite se quer "entrar" ou "sair" :')

if entrada == 'entrar':#condição 1
    #bloco de código
    print('Você entrou')
elif entrada == 'sair':#condição 2
    print('Você saiu')
else:
    print('Nenhuma opção aceita')