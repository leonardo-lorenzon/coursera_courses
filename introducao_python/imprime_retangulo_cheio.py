def imprime_retangulo():
	largura = int(input("digite a largura: "))
	altura = int(input("digite a altura: "))
	cont_altura = 1
	cont_largura = 1
	while cont_altura <= altura:
		while cont_largura <= largura:
			print("#", end = "" )
			cont_largura = cont_largura + 1
		print()
		cont_largura = 1
		cont_altura = cont_altura + 1


imprime_retangulo()
