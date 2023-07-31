# Busca linear e uma lista com alocação sequencial


def busca(lista,elemento):
    """BUSCANDO O INDICE DE UM ELEMENTO , VERIFICANDO SE ESTÁ OU NÃO NA LISTA"""
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

lista = [10,25,30,"anderson",44]
elemento = 10


indice = busca(lista,elemento)

if indice is not None:
    print(f"o indice do elemento {elemento} é {indice}")
else:
    (f"o elemento {elemento} nao esta na lista")