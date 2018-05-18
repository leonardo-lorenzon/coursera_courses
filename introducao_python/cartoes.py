meu_cartao = int(input("Digite o número do seu cartão de crédito: "))

cartao_lido = 1
encontrei_meu_cartao_na_lista = False

while cartao_lido != 0 and not encontrei_meu_cartao_na_lista:
	cartao_lido = int(input("Digite o número do próximo cartão de crédito: "))
	if cartao_lido == meu_cartao:
		encontrei_meu_cartao_na_lista = True

if encontrei_meu_cartao_na_lista:
	print("Meu cartão está lá!")
else:
	print("Meu cartão não está lá.")
