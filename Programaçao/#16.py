#16
#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão.

temp = int(input("temperatura: "))

f = input("voce quer passar a temperatura de °C para °F?")

if f == "não":
    c = input("você quer passar de °F para °C?")

if f == "sim":
    temp = (temp*1.8) + 32
    print(temp,"°F")
elif c == "sim":
    temp = (temp - 32)/ 1.8
    print(temp,"°C")
else:
    print(temp,"°F")