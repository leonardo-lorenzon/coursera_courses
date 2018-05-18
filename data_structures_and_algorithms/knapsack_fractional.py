# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0
	len_weights = len(weights)
	max_value = 0
	value_per_weights = 0
	product = 0
	i = 1
	
	while i <= len_weights and capacity > 0:
		for k in range(len_weights):
			value_per_weights = values[k] / weights[k]
			
			if value_per_weights > max_value:
				max_value = value_per_weights
				product = k

		if weights[product] < capacity:
			value += max_value * weights[product]
			capacity -= weights[product]
		else:
			value += max_value * capacity
			capacity = 0

		values[product] = 0
		max_value = 0
		i += 1

	return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
