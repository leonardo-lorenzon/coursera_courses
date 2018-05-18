import random
import time
import ordenador
class ContaTempos:
	def lista_aleatoria(self, n):
		lista = [0 for x in range(n)]

		for i in range(n):
			lista[i] = random.randrange(1000)

		return lista
	
	def lista_quase_ordenada(self, n):
		lista = [x for x in range(n)]
		lista[n//10] = - 500
		return lista
                

	def compara (self, n):
		lista1 = self.lista_aleatoria(n)
		lista2 = lista1[:]

		o = ordenador.Ordenador()

		antes = time.time()
		o.bubble_sort(lista1)
		depois = time.time()
		print("Método bubble_sort demorou:", depois - antes)

		antes = time.time()
		o.selection_sort(lista2)
		depois = time.time()
		print("Método selection_sort demorou:", depois - antes)
