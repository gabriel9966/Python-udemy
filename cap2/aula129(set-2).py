# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1 | s2 # Unindo 2 sets
print(s3)
s4 = s1 & s2# interseção , itens presente em ambos sets
print(s4)

s5 = s1 - s2 #itens presentes apenas no set da esquerda
print(s5)

s6 = s1 ^ s2# itens que não estão em ambos
print(s6)