import math

def soma_hipotenusas(n):
	cont = 1
	soma_h = 0
	while cont <= n:
		if e_hipotenusa(cont) == True:
			soma_h = soma_h + cont
		cont = cont + 1
	return soma_h


def e_hipotenusa(h):
	cateto_1 = 1
	cateto_2 = 1
	achou_hipotenusa = False
	while cateto_1 <= h and achou_hipotenusa == False:
		
		while cateto_2 <= h and achou_hipotenusa == False:
			hipotenusa = math.sqrt(cateto_1 ** 2 + cateto_2 ** 2)
			if hipotenusa == h:
				achou_hipotenusa = True
			cateto_2 = cateto_2 + 1

		cateto_1 = cateto_1 + 1
		cateto_2 = 1

	return achou_hipotenusa




def test_e_hipotenusa():
	assert e_hipotenusa(5) == True
	assert e_hipotenusa(10) == True
	assert e_hipotenusa(13) == True
	assert e_hipotenusa(15) == True
	assert e_hipotenusa(17) == True
	assert e_hipotenusa(20) == True
	assert e_hipotenusa(25) == True
	assert e_hipotenusa(4) == False
	assert e_hipotenusa(16) == False
	assert e_hipotenusa(24) == False



