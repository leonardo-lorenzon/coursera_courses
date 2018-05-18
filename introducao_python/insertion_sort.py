def insertion_sort(lista):
	lista_ordenada = []

	for i in lista:
		lista_ordenada.append(i)
		j = len(lista_ordenada) - 1
		lista_atual_ordenada = False
		while j > 0 and lista_atual_ordenada == False:
			if lista_ordenada[j] < lista_ordenada[j - 1]:
				lista_ordenada[j], lista_ordenada[j - 1] = lista_ordenada[j - 1], lista_ordenada[j]
			else:
				lista_atual_ordenada = True
			j -= 1

	return lista_ordenada
