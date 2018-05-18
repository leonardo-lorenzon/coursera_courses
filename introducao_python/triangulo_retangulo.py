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
