def max_funcao(valor1, valor2, restricao1_quantidade, restricao2_quantidade, tempo1, tempo2, restricao_tempo):
	lucro_maximo = 0
	receita = 0
	produto1 = 0
	produto2 = 0
	q1_max = 0
	q2_max = 0

	while produto1 <= restricao1_quantidade:
		while produto2 <= restricao2_quantidade:
			if tempo1 * produto1 + tempo2 * produto2 <= restricao_tempo:
				receita = produto1 * valor1 + produto2 * valor2
				if receita > lucro_maximo:
					lucro_maximo = receita
					q1_max = produto1
					q2_max = produto2
			produto2 += 1
		produto2 = 0
		produto1 +=1

	return lucro_maximo, q1_max, q2_max
