numero = int(input("Digite um número inteiro: "))

aux = numero	#utilizada para atualizar o número no processo da soma
soma = 0
ultimo_numero = 0

while aux != 0:
	ultimo_numero = aux % 10
	soma = soma + ultimo_numero
	aux = aux // 10

print(soma)
