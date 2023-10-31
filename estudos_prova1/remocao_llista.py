from Node import Node

# REMOVEMOS O ELEMENTO QUE FOI RECEBIDO COMO PARAMETRO

def remover(self,elem):
    pointer = self.head
    while(pointer):
        if pointer.data == elem:
            a