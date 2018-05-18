def sao_multiplicaveis(m1, m2):

	num_linhas_m2 = len(m2)
	num_colunas_m1 = len(m1[0])
	
	if num_colunas_m1 == num_linhas_m2:
		return True
	else:
		return False