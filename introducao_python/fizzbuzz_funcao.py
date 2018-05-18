def fizzbuzz(valor):
	if (valor % 3 == 0) and not(valor % 5 == 0):
		return "Fizz"
	else:
		if (valor % 5 == 0) and not(valor % 3 == 0):
			return "Buzz"
		else:
			if (valor % 3 == 0) and (valor % 5 == 0):
				return "FizzBuzz"
			else:
				return valor
