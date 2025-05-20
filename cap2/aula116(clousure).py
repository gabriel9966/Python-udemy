#Closure é uma função que “lembra” do ambiente onde foi criada, mesmo depois desse ambiente ter terminado sua execução.
#Closure (ou fechamento) em Python acontece quando uma função interna (filha) "lembra" do ambiente onde foi criada — ou seja, ela mantém acesso às variáveis da função externa (mãe),
def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao} , {nome}'
    return saudar

#call stack = pilha de chamadas

bom_dia = saudacao('Bom dia ')
#print(s1('Luiz'))

for nome in ['Luiz','Joana','julia','Gustavo']:
    print(bom_dia(nome))