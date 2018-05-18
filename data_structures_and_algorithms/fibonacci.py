# Uses python3

def fibonacci(n):

	n1 = 0
	n2 = 1
	if n == 0:
		last_fibonacci = 0
	else:
		last_fibonacci = 1
	i = 2
	
	while i <= n:
		last_fibonacci = n2 + n1
		n1 = n2
		n2 = last_fibonacci
		i += 1

	return last_fibonacci

n = int(input())
print(fibonacci(n))