#A função abaixo recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica.
def primeiro_lex(lista_palavras):

	primeiro = lista_palavras[0]

	for i in lista_palavras:
		if i < primeiro:
			primeiro = i

	return primeiro
