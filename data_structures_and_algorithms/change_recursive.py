def change(n, coin_array):
	if n == 0:
		return 0

	best = - 1

	for coin in coin_array:
		if coin <= n:
			next_try = change(n - coin, coin_array)

		if best < 0 or best > next_try + 1:
			best = next_try + 1

	return best