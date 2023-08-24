#19
#Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
#Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
#a. Soma de 2 numeros.
#b. Diferença entre 2 números (maior pelo menor).
#c.Produto entre 2 números.
#d. Divisão entre 2 números (o denominador não pode ser zero).

    
def soma():
   som = n1 + n2
   print("o resultado é: ", som)

def diferenca():
    if n1 > n2:
        dif = n1 - n2
    else:
        dif = n2 - n1
    print("o resultado é", dif)

def produto():
    pr = n1 * n2
    print("o resultado é", pr)

def divisao():
    dv = n1/n2
    print("o resulatdo é", dv)

menu = input("o que deseja fazer?"
                "\nSoma de 2 numeros(a)" 
                "\nDiferença entre 2 números(b)"
                "\nProduto entre 2 números(c)"
                "\nDivisão entre 2 números(d)")
n1 = int(input("1° numero: "))
n2 = int(input("2° numero: "))

if menu == "a":
    soma()

elif menu == "b":
    diferenca()

elif menu == "c":
    produto()

elif menu == "d":
    divisao()