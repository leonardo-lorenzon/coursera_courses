def incomodam(n):
	if n <= 0:
		return ""
	else:
		return "incomodam " + incomodam(n - 1)

def elefantes(n, i = int(1)):
	if i == n or n < 1:
		return ""
	else:
		if i > 1:
			j = i + 1
			str_j = str(j)
			str_i = str(i)
			return str_i + " elefantes " + incomodam(i) + "muita gente "\
			+ str_j + " elefantes " + incomodam(j) + "muito mais "\
			+ elefantes(n, i + 1)
			
		else:
			j = i + 1
			str_j = str(j)
			str_i = str(i)
			return "Um elefante incomoda muita gente " + str_j + " elefantes " + incomodam(j) + "muito mais " + elefantes(n, i + 1)
			