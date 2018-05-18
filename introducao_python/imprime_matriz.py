def imprime_matriz(matriz):
	lin = len(matriz)
	col = len(matriz[0])

	for i in range(lin):
		for j in range(col):
			valor = matriz[i][j]
			if j < col - 1:
				print(valor, end = " ")
			else:
				print(valor)
		
