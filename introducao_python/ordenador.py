class Ordenador:

	def selection_sort(self, lista):

		for i in range(len(lista)):
			for j in range(i,len(lista)):
				if lista[i] > lista[j]:
					lista[i], lista[j] = lista[j], lista[i]

		return lista

	def bubble_sort(self, lista):
		tamanho = len(lista) - 1

		for i in range(tamanho, 0, -1):
			trocou = False
			for j in range(i):
				if lista[j] > lista[j + 1]:
					lista[j], lista[j + 1] = lista[j + 1], lista[j] 
					trocou = True
			if not trocou:
				return lista

		return lista