# fila encadeada 
# sempre inserimos no final , e retiramos no começo
from Node import Node

class Fila:
    def __init__(self):	
        self.first = None
        self.last = None
        self.size = 0

    def insert(self,elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node      
        if self.first is None:
            self.first = node 
        self.size = self.size + 1
        



    def imprimir(self):
        string = ""
        pointer = self.first
        while(pointer):
            string = string + str(pointer.data) + "->"
            pointer = pointer.next
        return string
    
    
fila = Fila()
fila.insert(5)
fila.insert(6)
fila.insert(7)
fila.insert(8)
fila.insert(9)
fila.insert(10)
print(fila.imprimir())