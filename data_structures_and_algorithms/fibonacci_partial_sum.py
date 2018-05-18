# Uses python3
import sys

def fibonacci_partial_sum(m, n):
    
    n1 = 0
    n2 = 1
    
    last_fibonacci = 0

    if m < 2:
        sum_last_digit = 1
    else:
        sum_last_digit = 0
    
    len_max = n + 1
    
    for i in range(2, len_max):
        last_fibonacci = (n2 + n1) % 10
        n1, n2 = n2, last_fibonacci

        if i >= m:
            sum_last_digit += last_fibonacci

    
    return sum_last_digit % 10



if __name__ == '__main__':
    input = sys.stdin.read();
    m, n = map(int, input.split())
    print(fibonacci_partial_sum(m, n))
