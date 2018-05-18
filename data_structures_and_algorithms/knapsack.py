# Uses python3
import sys

def cria_matriz(num_linhas, num_colunas, valor):

	matriz = []
	for i in range(num_linhas):
		linha= []
		for j in range(num_colunas):
			linha.append(valor)

		matriz.append(linha)

	return matriz




def optimal_weight(W, w):
    value = cria_matriz(W + 1, len(w) + 1, 0)

    for i in range(1, len(w) + 1):
   	    for j in range(1, W + 1):
   	   	    value[j][i] = value[j][i - 1]
   	   	    if w[i - 1] <= j:
   	   	        val = value[j - w[i - 1]][i - 1] + w[i - 1]
   	   	        if value[j][i] < val:
   	   	            value[j][i] = val
    return value[W][len(w)]




if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
