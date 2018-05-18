def bubble_sort(lista):
    tamanho = len(lista) - 1

    for i in range(tamanho, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista) 

    return lista