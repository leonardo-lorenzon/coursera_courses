# Uses python3

def fibonacci_last_digit(n):

    list_fibonacci = list(range(n + 2))

    list_fibonacci[0] = 0
    list_fibonacci[1] = 1

    for i in range(2,n + 1):
        list_fibonacci[i] = (list_fibonacci[i - 1] + list_fibonacci[i - 2]) % 10

    return list_fibonacci[n] % 10

if __name__ == '__main__':

    n = int(input())
    print(fibonacci_last_digit(n))
