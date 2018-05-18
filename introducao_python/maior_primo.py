def maior_primo():
	x = int(input("Digite um número:"))
	cont = 1
	cont_primo = 0

	while cont <= x:
		if e_primo(cont) == True:
			cont_primo = cont_primo + 1
		cont = cont + 1
	print(cont_primo)
		
	


def e_primo(valor):
	fator = 2
	while valor % fator != 0 and fator <= valor / 2:
		fator = fator + 1
	if valor % fator == 0:
		return False
	else:
		return True


def test_e_primo():
	assert e_primo(3) == True
	assert e_primo(5) == True
	assert e_primo(7) == True
	assert e_primo(39) == True
	assert e_primo(21) == False
	assert e_primo(25) == False
	assert e_primo(49) == False



maior_primo()
