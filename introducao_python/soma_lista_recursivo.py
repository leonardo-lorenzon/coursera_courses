def soma_lista(lista, n = 0):

	if n == len(lista) - 1:
		return lista[n] 
	else:
		return lista[n] + soma_lista(lista, n + 1)