def printstr(s):
    # Caso base: se a string estiver vazia, a recursão termina
    if s == "":
        return
    else:
        # Imprime o primeiro caractere da string
        print(s[0], end='')
        # Chama a função recursivamente com o restante da string
        printstr(s[1:])

printstr("hello")