from Node import Node
from remocao_fila import remover

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def empilhar(self,elem):
        node = Node(elem)
        if self.top is None:
            self.top = node
        else:
            new_top = node
            new_top.next = self.top
            self.top = new_top
        self.size = self.size + 1
        
    def impressao(self):
        string=""
        pointer = self.top
        while(pointer):
            string = string + str(pointer.data) + "\n"
            pointer = pointer.next
        return print(string)


pilha = Pilha()
pilha.empilhar("Hello")
pilha.empilhar("friend")
pilha.empilhar("its working")
pilha.impressao()
            
      