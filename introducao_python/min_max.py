def min_max(temperatura):
	print("A menor temperatura mínima do mês foi: ", minima(temperatura), "C.")
	print("A menor temperatura maxima do mês foi: ", maxima(temperatura), "C.")


def minima(temps):
	min = temps[0]
	i = 0
	while i < len(temps):
		if temps[i] < min:
			min = temps[i]
		i += 1

	return min

def maxima(temps):
	max = temps[0]
	i = 0
	while i < len(temps):
		if temps[i] > max:
			max = temps[i]
		i += 1

	return max
