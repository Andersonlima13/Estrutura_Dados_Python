# definindo a classe do nó 

class Node:
  def __init__(self,data):
    self.data = data   # representa qual dado você vai adcionar
    self.next = None   # aponta para o proximo nó        

class Linked_List:
  def __init__(self):
    self.head = None
    self.size = 0

  def append(self, elem):
    if self.head:      # se tiver elementos , adcione
      pointer = self.head
      while(pointer.next):
        pointer = pointer.next
      pointer.next = Node(elem)
    else:              # se estiver sem elementos , coloque no topo
      self.head = Node(elem) # primeiro 
    self.size = self.size + 1


    def __len__(self):
      return self.size

    

    




lista = Linked_List()
lista.append(7)
lista.append(8)
print(lista.size)
