def main():
	n = int(input("Digite o valor de n(negativo para finalizar): "))
	while n >= 0:
		print(fatorial(n))
		n = int(input("Digite o valor de n(negativo para finalizar: "))

def fatorial(n):
	fatorial = 1
	while n > 1:
		fatorial = fatorial * n
		n = n - 1
	return fatorial
