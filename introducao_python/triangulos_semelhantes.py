import math
class Triangulo:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def perimetro(self):
		return self.a + self.b + self.c

	def tipo_lado(self):
		if self.a == self.b and self.b == self.c:
			return "equilátero"
		else:
			if self.a != self.b and self.a != self.c and self.b != self.c:
				return "escaleno"
			else:
				return "isósceles"

	def retangulo(self):
		a = self.a
		b = self.b
		c = self.c

		if a == math.sqrt(b ** 2 + c ** 2):
			return True
		else:
			if b == math.sqrt(a ** 2 + c ** 2):
				return True
			else:
				if c == math.sqrt(a ** 2 + b ** 2):
					return True
				else:
					return False

	def semelhantes(self, triangulo):
		lista1 = [self.a, self.b, self.c]
		lista2 = [triangulo.a, triangulo.b, triangulo.c]
		tamanho_lista = len(lista1) - 1
		cont = 0
		indicador = True
		semelhanca = lista1[0] / lista2[0]
		
		while cont <= tamanho_lista and indicador == True:
			if lista1[cont] / lista2[cont] == semelhanca:
				indicador = True
			else:
				indicador = False
			cont += 1

		return indicador


