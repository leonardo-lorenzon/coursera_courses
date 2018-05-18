# Uses python3
import sys

def fibonacci_huge(n, m):
    
    x = n % len_pisano_period(n, m)
    
    return fibonacci(x) % m

    

def len_pisano_period(n, m):
    
    pisano1 = 0
    pisano2 = 1
    last_pisano = 0

    len_pisano = 2

    n1 = 0
    n2 = 1
    if n == 0:
        last_fibonacci = 0
    else:
        last_fibonacci = 1
    
    i = 2
    len_max = n * m
    ind = False
    
    while i <= len_max and ind == False:
        last_fibonacci = n2 + n1
        n1 = n2
        n2 = last_fibonacci

        last_pisano = last_fibonacci % m

        len_pisano += 1

        if last_pisano == 1 and pisano2 == 0:
            ind = True
            len_pisano -= 2

        pisano1 = pisano2
        pisano2 = last_pisano

        i += 1
        len_pisano += 1

    return len_pisano



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


    

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_huge(n, m))
