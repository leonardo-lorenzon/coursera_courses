def min_funcao(valor1, valor2, restricao1_quantidade, restricao2_quantidade, tempo1, tempo2, restricao_tempo):
	custo_minimo = produto1 * valor1 + produto2 * valor2
	receita = 0
	produto1 = 0
	produto2 = 0
	q1_min = 0
	q2_min = 0

	while produto1 <= restricao1_quantidade:
		while produto2 <= restricao2_quantidade:
			if tempo1 * produto1 + tempo2 * produto2 <= restricao_tempo:
				receita = produto1 * valor1 + produto2 * valor2
				if receita < custo_minimo:
					custo_minimo = receita
					q1_min = produto1
					q2_min = produto2
			produto2 += 1
		produto2 = 0
		produto1 +=1

	return custo_minimo, q1_min, q2_min
