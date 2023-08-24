#09
#Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
#mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
#Euros.

nome = input("escreva seu nome: ")
valor = float(input("valor da pessoa: "))

dolar = valor/5.14
euro = valor/5.21

print("dolares: ", dolar, ";euros: ", euro)
