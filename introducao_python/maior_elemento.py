def maior_elemento(lista):
	maior_elemento = lista[0]
	for elemento in lista:
		if  elemento > maior_elemento:
			maior_elemento = elemento

	return maior_elemento

