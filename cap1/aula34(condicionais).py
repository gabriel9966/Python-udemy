#muda o fluxo do código
#if = se
#elif = senão se 
#else = senão

entrada = input('Digite se quer "entrar" ou "sair" :')

if entrada == 'entrar':#condição 1
    #bloco de código
    print('Você entrou')
elif entrada == 'sair':#condição 2
    print('Você saiu')
else:
    print('Nenhuma opção aceita')