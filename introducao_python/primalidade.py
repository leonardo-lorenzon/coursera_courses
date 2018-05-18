valor = int(input("Digite um número inteiro: "))

if valor == 2 or valor == 3 or valor == 5 or valor == 7:
        print("primo")
else:
        if (valor % 2 == 0 or valor % 3 == 0 or valor % 5 == 0 or valor % 7 == 0):
                print("não primo")
        else:
                print("primo")

