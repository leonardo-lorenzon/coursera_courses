# A função abaixo recebe uma lista de nomes como parâmetros e devolve o primeiro nome mais curto da presente na lista, de forma capitalizada.
def menor_nome(lista_de_nomes):

	menor_nome = lista_de_nomes[0].strip()

	for i in lista_de_nomes:
		nome_atual = i.strip()

		if len(nome_atual) < len(menor_nome):
			menor_nome = nome_atual
	
	return menor_nome.capitalize()


