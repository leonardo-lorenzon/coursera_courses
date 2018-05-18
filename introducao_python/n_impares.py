n = int(input("Digite o valor de n: "))
cont = 0

while cont < 2 * n:
	if cont % 2 != 0:
		print(cont)
	cont = cont + 1
