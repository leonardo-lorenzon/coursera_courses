def lista_grande(n):
	from random import randrange
	lista = []

	for i in range(n):
		lista.append(randrange(n))

	return lista
