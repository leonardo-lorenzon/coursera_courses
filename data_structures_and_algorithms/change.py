# Uses python3
import sys

def get_change(m):
	cont_coins = 0

	cont_coins += (m // 10)
	m = m % 10
	
	cont_coins += (m // 5)
	m = m % 5

	cont_coins += (m // 1)

	return cont_coins








if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
