def cria_matriz(num_linhas, num_colunas):
	matriz = []

	for i in range(num_linhas):
		linha = []
		for j in range(num_colunas):
			valor = int(input("Digite o elemento [" + str(i) +"][" + str(j) +"]: "))
			linha.append(valor)
		matriz.append(linha)

	return imprime_matriz(matriz)


def le_matriz():
	lin = int(input("Digite o número de linhas da matriz: "))
	col = int(input("Digite o número de coluna da matriz: "))
	return cria_matriz(lin, col)

def imprime_matriz(matriz):
	lin = len(matriz)
	col = len(matriz[0])

	for i in range(lin):
		for j in range(col):
			valor = matriz[i][j]
			print(valor, end = " ")
		print()

		
