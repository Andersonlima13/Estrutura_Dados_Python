lista = [7,5,1,8,3]

# PRIMEIRO PASSO -> ENCONTRAR O MENOR VALOR DA LISTA 


print(minimo)


def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j,n):
            if lista[i] < lista[min_index]:
                min_index = i
            if lista[j] > lista[min_index]:
                aux = lista[j]
                lista[j] = lista[min_index]
                lista[min_index] = aux