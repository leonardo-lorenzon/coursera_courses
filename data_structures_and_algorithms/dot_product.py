#Uses python3

import sys


def insertion_sort(lista):
    lista_ordenada = []

    for i in lista:
        lista_ordenada.append(i)
        j = len(lista_ordenada) - 1
        lista_atual_ordenada = False
        while j > 0 and lista_atual_ordenada == False:
            if lista_ordenada[j] < lista_ordenada[j - 1]:
                lista_ordenada[j], lista_ordenada[j - 1] = lista_ordenada[j - 1], lista_ordenada[j]
            else:
                lista_atual_ordenada = True
            j -= 1

    return lista_ordenada


def max_dot_product(a, b):
    a = insertion_sort(a)
    b = insertion_sort(b)

    res = 0

    for i in range(len(a)):
        res += a[i] * b[i]

    return res





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
