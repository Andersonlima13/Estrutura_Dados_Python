from Node import Node


class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0
        
# O METODO DEVE PERMITIR QUE O ELEMENTO SEJA INSERIDO EM QUALQUER POSIÇÃO

    def insert(self,elem,index):
        if index == 0:
            node = Node(elem)
            node.next = self.first
            self.first = node
        else:
            pointer = self.first
            for i in range(index-1):
                if pointer:
                    pointer = pointer.next
                    node = Node(elem)
                    node.next = pointer.next
                    pointer.next = node
                else:
                    raise IndexError("elemento nao encontrado")
                
            
            
lista = LinkedList()
lista.insert