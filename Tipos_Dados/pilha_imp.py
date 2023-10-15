class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class Pilha:
    
# INICIO DA PILHA 
    def __init__(self):
        self.top = None
        self.size = 0


    def esta_vazia(self):
        if self.size == 0:
            return True
        else:
            return False
        

    def tamanho(self):
        return self.__len__()

    def empilhar(self, elemento):
        if self.top:
            new_top = Node(elemento)
            new_top.next = self.top
            self.top = new_top
        else:
            self.top = Node(elemento)
        self.size = self.size + 1
            

    def __len__(self):
        return self.size
        

    def desempilhar(self):
        if self.top:
            pointer = self.top
            self.top = pointer.next
            self.size = self.size - 1
        else:
            raise IndexError("Não existem elementos para remover")
            
    def imprimir(self):
        string = ""
        pointer = self.top
        while(pointer):
            string = string + str(pointer.data) + "->"
            pointer = pointer.next
        return string
            
    def __str__(self):
        return self.imprimir()

pilha = Pilha()
pilha.empilhar(8)
pilha.empilhar(9)
pilha.empilhar(10)
print(pilha.imprimir())
pilha.esta_vazia()