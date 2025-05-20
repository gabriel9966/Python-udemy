# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados
s2 = set('gabriel')
print(s1)
print(s2)


set3 = {33,44,44,33,5,5,5,9,10,1}# set nao permitem valores duplicados , ele naturalmente remove os duplicados
print(set3)
set3.add(9999)
print(set3)
set3.update(('oi'))
print(set3)
set3.discard('o')# Elimina o valor
print(set3)



lista1 = [33,44,44,33,5,5,5,9,10,1]
print(lista1)
lista_corrigida = set(lista1)
lista_corrigida = list(lista_corrigida)
print(lista_corrigida)


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos