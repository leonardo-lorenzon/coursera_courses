# A função abaixo recebe como parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string opcional com valor padrão sendo "vogais". Quando o segundo parâmetro for definido como "vogais", a função devolve o número de vogais presente na frase, quando for definido como "consoantes", develve o número de consoantes na frase.
def conta_letras(frase, contar = "vogais"):
	assert contar == "vogais" or contar == "consoantes"

	tamanho_frase = len(frase) - 1
	letra_atual = frase[0]
	i = 0

	if contar == "vogais":
		cont_vogais = 0

		while i <= tamanho_frase:
			letra_atual = frase[i].lower()
			if letra_atual == "a" or letra_atual == "e" or letra_atual == "i" or letra_atual == "o" or letra_atual == "u":
				cont_vogais += 1

			i += 1

		return cont_vogais
	
	else:
		cont_consoantes = 0

		while i <= tamanho_frase:
			letra_atual = frase[i].lower()
			
			if letra_atual != "a" and letra_atual != "e" and letra_atual != "i" and letra_atual != "o" and letra_atual != "u" and letra_atual != " ":
				cont_consoantes += 1
			i += 1

		return cont_consoantes
