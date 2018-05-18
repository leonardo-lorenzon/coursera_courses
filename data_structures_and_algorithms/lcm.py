# Uses python3
import sys

def euclid_gcd(a, b):

	if b == 0:
		return a

	a_rem = a % b

	return euclid_gcd(b, a_rem)

def euclid_lcm(a, b):
	gcd = euclid_gcd(a, b)
	lcm = (a * b) // gcd

	return lcm

    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(euclid_lcm(a, b))

