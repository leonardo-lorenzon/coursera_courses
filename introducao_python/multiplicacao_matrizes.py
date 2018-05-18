def multiplicacao_matrizes(m1, m2):
	num_linhas_m1, num_colunas_m1 = len(m1), len(m1[0])
	num_linhas_m2, num_colunas_m2 = len(m2), len(m2[0])

	assert num_colunas_m1 == num_linhas_m2

	matriz_resultante = []
	for linha in range(num_linhas_m1):
		matriz_resultante.append([])
		for coluna in range(num_colunas_m2):
			matriz_resultante[linha].append(0)
			for k in range(num_colunas_m1):
				matriz_resultante[linha][coluna] += m1[linha][k] * m2[k][coluna]

	return matriz_resultante

