# Uses python3

def fibonacci_sum_last_digit(n):
    
    n1 = 0
    n2 = 1
    if n == 0:
        last_fibonacci = 0
        sum_last_digit = 0
    else:
        last_fibonacci = 1
        sum_last_digit = 1

    
    
    len_max = n + 1
    
    for i in range(2, len_max):
        last_fibonacci = (n2 + n1) % 10
        n1, n2 = n2, last_fibonacci

        sum_last_digit += last_fibonacci

    
    return sum_last_digit
        


if __name__ == '__main__':
    
    n = int(input())
    print(fibonacci_sum_last_digit(n))