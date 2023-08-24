#11
#Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.

nome = input("seu nome: ")
numero = int(input("seu numero: "))
valor = int(input("Valor por hora: "))

salariob = numero*valor
inss = salariob * 0.98

print("salario depois que o estado roubou uma parte: ", inss)