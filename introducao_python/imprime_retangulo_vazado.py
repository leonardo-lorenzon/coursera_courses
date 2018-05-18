def imprime_retangulo_oco():
	largura = int(input("digite a largura: "))
	altura = int(input("digite a altura: "))
	cont_altura = 1
	cont_largura = 1
	while cont_altura <= altura:
		if cont_altura == 1 or cont_altura == altura:
			while cont_largura <= largura:
				print("#", end = "" )
				cont_largura = cont_largura + 1
		else:
			print("#", end = "")
			while cont_largura < largura - 1 :
				print(end = " ")
				cont_largura = cont_largura + 1
			print("#", end = "")		

		print()
		cont_largura = 1
		cont_altura = cont_altura + 1


imprime_retangulo_oco()
