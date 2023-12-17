def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quick_sort(lista, inicio, p - 1)  # Chama recursivamente para a sub-lista à esquerda do pivô
        quick_sort(lista, p + 1, fim)      # Chama recursivamente para a sub-lista à direita do pivô



def partition(lista, inicio, fim):
    pivot = lista[fim]  # Escolhe o último elemento da lista como pivô
    i = inicio  # Inicializa o índice i para a posição inicial da sub-lista

    for j in range(inicio, fim):  # Itera sobre a sub-lista da função
        if lista[j] <= pivot:  # Compara cada elemento com o pivô
            lista[j], lista[i] = lista[i], lista[j]  # Troca os elementos nas posições i e j se necessário
            i = i + 1  # Atualiza o índice i

    lista[i], lista[fim] = lista[fim], lista[i]  # Coloca o pivô na posição correta na lista ordenada
    return i  # Retorna a posição final do pivô