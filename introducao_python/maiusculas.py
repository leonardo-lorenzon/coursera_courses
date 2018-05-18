# A função abaixo recebe uma frase(string) como parâmetro e devolve um string com as letras maiúsculas que exitem nesta frase, na ordem em que elas aparecem.
def maiusculas(frase):
	tamanho_frase = len(frase) - 1
	i = 0
	so_maiuscula = ""
	
	while i <= tamanho_frase:
		ord_caracter = ord(frase[i])
		
		if ord_caracter >= 65 and ord_caracter <= 90:
			so_maiuscula = so_maiuscula + frase[i]

		i += 1

	return so_maiuscula