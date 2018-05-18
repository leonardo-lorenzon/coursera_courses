# Uses python3
import sys

def binary_search(a, x, min = 0, max = None):
    if max == None:
        max = len(a)-1

    if max < min:
        return -1
    else:
        meio = min + (max-min)//2

    if a[meio] > x:
        return binary_search(a, x, min, meio - 1)
    elif a[meio] < x:
        return binary_search(a, x, meio + 1, max)
    else:
        return meio






def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
