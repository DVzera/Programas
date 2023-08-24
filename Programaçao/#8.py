#8
#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
#quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

lar = float(input("largura da parede: "))
alt = float(input("altura da parede: "))

a = lar*alt
tinta = a/2

print(a, tinta)

