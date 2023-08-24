#15
#Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
#tela dizendo se está “quente”, “frio” ou “agradável”.

temp = int(input("Qual a temperatura atual?: "))

if temp <= 18:
    print("esta frio :E")

elif (temp > 18) and (temp < 24):
    print("esta agradavel C:")

else:
    print("TA CALOR >:C")