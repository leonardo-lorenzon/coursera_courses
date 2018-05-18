def ordenada(lista):
	anterior = lista[0]
	
	for i in lista:
		if anterior > i:
			return False
		anterior = i
	return True

