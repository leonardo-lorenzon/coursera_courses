# Uses python3

def cria_matriz(num_linhas, num_colunas, valor):

	matriz = []
	for i in range(num_linhas):
		linha= []
		for j in range(num_colunas):
			linha.append(valor)

		matriz.append(linha)

	return matriz



def edit_distance(a , b):
	d = cria_matriz(len(a) + 1, len(b) + 1, 1)
	for k in range(len(a) + 1):
		d[k][0] = k
	for z in range(len(b) + 1):
		d[0][z] = z

	for j in range(1, len(b) + 1):
		for i in range(1, len(a) + 1):
			insertion = d[i][j - 1] + 1
			deletion = d[i - 1][j] + 1
			match = d[i - 1][j - 1]
			mismatch = d[i - 1][j - 1] + 1

			if a[i - 1] == b[j - 1]:
				d[i][j] = min(insertion, deletion, match)
			else:
				d[i][j] = min(insertion, deletion, mismatch)
	return d[len(a)][len(b)]






if __name__ == "__main__":
    print(edit_distance(input(), input()))
