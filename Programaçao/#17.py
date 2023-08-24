#17
#Faca um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura):
#• Homens: (72.7 ∗ h) − 58
#• Mulheres: (62, 1 ∗ h) − 44, 7

altura = float(input("altura: "))
sexo = input("Sexo(m ou f): ")

if sexo == "m":
    peso = (72.7 * altura) - 58
    print("seu peso ideal é: ", peso)
else:
    peso = (62.1 * altura) - 44.7
    print("seu peso ideal é: ", peso)