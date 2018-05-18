def main():
	
	lista_inteiros = []
	x = int(input("Digite um número inteiro: "))
	cont_reverso = 0

	while x != 0:
		lista_inteiros.append(x)
		x = int(input("Digite um número inteiro: "))
	
	cont_reverso = len(lista_inteiros)
	while cont_reverso > 0:
		cont_reverso = cont_reverso - 1
		print(lista_inteiros[cont_reverso])


main()
