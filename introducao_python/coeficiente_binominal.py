def fatorial(n):
	fatorial = 1
	while n > 1:
		fatorial = fatorial * n
		n = n - 1
	return fatorial

        
n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

coeficiente_binominal = (fatorial(n)) / (fatorial(k) * fatorial(n - k))

print("O coediciente binominal é:", coeficiente_binominal)
