perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

num_acertos = 0 

for pergunta in perguntas:

    pergunta_da_vez = pergunta['Pergunta']
    print(pergunta_da_vez)

    for i in pergunta['Opções']:
        print(f'- {i}')

    resposta = input('Responda:')

    if resposta == pergunta['Resposta']:
        print('Acertou')
        num_acertos+=1
    else:
        print('Errou')


print(f'Você acertou {num_acertos} respostas.')
