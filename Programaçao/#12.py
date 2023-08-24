#12
#) Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
#os itens repetidos.

a = ["davi","andre","davi","bruno"]

dup = [x for i, x in enumerate(a) if i != a.index(x)]
print(dup)