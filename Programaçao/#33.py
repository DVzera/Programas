#33
#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
#códigos utilizados são:
# 1 , 2, 3, 4 - Votos para os respectivos candidatos
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#a. O total de votos para cada candidato;
#b. O total de votos nulos;
#c. O total de votos em branco;
#d. A percentagem de votos nulos sobre o total de votos;
#e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
#valor zero.

mito = []
lulo = []
branco = []

t = int(input("total de votos: "))

for i in range(t):
    voto = int(input("código do candidato(1 lula, 2 mito)"))
    a = len(mito)
    b = len(lulo)
    c = len(branco)
    if voto == 1:
        aux = a + 1
        mito.append(aux)
    if voto == 2:
        aux = b + 1
        lulo.append(aux)
    else:
        aux = c + 1
        branco.append(aux)

porcentagem = len(branco) * 100 / t

print("Mito: ", len(mito)," Lulo: ", len(lulo)," branco: ", len(branco))
print(porcentagem, "% dos votos foram em branco")
