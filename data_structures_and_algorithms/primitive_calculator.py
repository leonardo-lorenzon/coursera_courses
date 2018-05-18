# Uses python3
import sys
import math

def optimal_sequence(n, x= None):
    if n < 1:
        return 1
    

    
    if n % 3 == 0:
        x += optimal_sequence(n // 3, x)
    elif n % 2 == 0:
        x += optimal_sequence(n // 2, x)
    else:
        x += optimal_sequence(n - 1, x)
    return x


    

input = sys.stdin.read()
n = int(input)
#sequence = list(optimal_sequence(n))
#print(len(sequence) - 1)
#for x in sequence:
 #   print(x, end=' ')
print(optimal_sequence(n))