# definindo a classe do nó 

class Node:
  def __init__(self,data):
    self.data = data   # representa qual dado você vai adcionar
    self.next = None   # aponta para o proximo nó        

class Linked_List:
  def __init__(self):
    self.head = None
    self.size = 0

# INSERE ELEMENTOS AO FINAL DA FILA

  def append(self, elem):
    if self.head:      # se tiver elementos , adcione // adcionando ao final da lista 
      pointer = self.head
      while(pointer.next): 
        pointer = pointer.next
      pointer.next = Node(elem)
    else:              # se estiver sem elementos , coloque no topo, primeira inserção
      self.head = Node(elem) # primeiro caso , onde a lista se encotra vazia
    self.size = self.size + 1


# INSERE ELEMENTOS NO INICIOO DA FILA


  def append_init(self,elem):   # A NOVA CABEÇA DA LISTA RECEBE UM NÓ 
    if self.head:               # ENTÃO O PROXIMO DA "NOVA CABEÇA"
      new_head = Node(elem)     # PASSA A SER NOSSO ANTIGO "HEAD"
      new_head.next = self.head
      self.head = new_head
      self.size = self.size + 1
  


  def __len__(self):
      return self.size
    

# ACESSAR O VALOR DO INDEX ESCOLHIDO




# RETORNA A POSIÇÃO DO NÓ 
  def _getnode(self,index):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("Erro de index")
    return pointer
    
  def __getitem__(self,index):
    pointer = self._getnode(index)
    if pointer:
      return pointer.data
    raise IndexError("Erro de index")

      # sobrecargas de operador 
      

# MODIFICAR O ELEMENTO ESCOLHENDO O INDEX
    
  def __setitem__(self,index,elem):
    pointer = self._getnode(index)
    if pointer:
      pointer.data = elem
      
    else:
      raise IndexError("Erro de index")

    #DEVOLVE O ELEMENTO , CASO EXISTA

#busca o indice do elemento da lista
  def search(self, elem):
    pointer = self.head
    i = 0
    while (pointer):  # equanto o pointer nao é vazio
      if pointer.data == elem:  # se o pointer for igual ao elemento buscado
        return i  # retornamos o elemento
      pointer = pointer.next
      i = i + 1
    raise ValueError(f" {elem} não encontrado")



#inserindo em qualquer posição

  def insert(self,index,elem ):
    node = Node(elem)
    if index == 0:
      node.next = self.head
      self.head = node
    else:
      pointer = self._getnode(index-1)
      node.next = pointer.next
      pointer.next = node
    self._size = self._size+1

  
  def remove(self,elem):
    if self.head == None:
      raise ValueError(f"{elem} is not in list")
    elif self.head.data == elem:
      self.head = self.head.next
    else:
      ancestor = self.head
      pointer = self.head
      while(pointer):
          if pointer.data == elem:
            ancestor.next = pointer.next
            pointer.next = None
          ancestor = pointer
          pointer = pointer.next
      return True 
    raise ValueError(f"{elem} is not in list" )
  
  

lista = Linked_List()
lista.append(7)
lista.append(8)
print(lista[3])
