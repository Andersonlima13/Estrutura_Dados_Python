

def insert_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and list[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave