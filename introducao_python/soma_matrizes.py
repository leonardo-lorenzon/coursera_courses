import matriz

def soma_matrizes(m1,m2):
	num_linhas = len(m1)
	num_colunas = len(m2[0])

	matriz_somada = matriz.cria_matriz(num_linhas, num_colunas,0)

	for lin in range(num_linhas):
		for col in range(num_colunas):
			matriz_somada[lin][col] = m1[lin][col] + m2[lin][col]

	return matriz_somada

