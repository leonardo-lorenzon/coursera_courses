#Uses python3

import sys

def largest_number(a):
	res = ""
	max_digit = 0

	while len(a) > 0:
		for i in a:
			if int(i[0]) >= max_digit:
				max_digit = int(i)

		res = res + str(max_digit)
		a.remove(str(max_digit))

		max_digit = 0

	return res








if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
