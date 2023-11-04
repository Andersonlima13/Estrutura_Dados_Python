def menores_rec(lista, key):
    # Caso base: se a lista estiver vazia, não há elementos menores que key.
    if not lista:
        return 0
    # Verifica se o primeiro elemento da lista é menor que key.
    # Se for, incrementa o contador em 1 e chama a função recursivamente
    # com a lista sem o primeiro elemento.
    if lista[0] < key:
        return 1 + menores_rec(lista[1:], key)
    else:
        # Se o primeiro elemento não for menor que key, apenas chama a função recursivamente
        # com a lista sem o primeiro elemento.
        return menores_rec(lista[1:], key)

# Exemplo de uso:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 5

resultado = menores_rec(lista, key)
print("Quantidade de elementos menores que", key, "na lista:", resultado)
