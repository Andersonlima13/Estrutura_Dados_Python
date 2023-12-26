# OPERAÇOES EM PILHA :

def inserir_pilha(self,elem)
    if sel.top is None:
        self.top = node(elem)
    else:
        new_top = self.top
        new_top.next = self.top
        self.top = new_top
    pop.len += 1
    
def remove_pilha(self,top):
    if self.top is None:
        raise{
            IndexError()
        }
    else:
        new_top = self.top.next
        self.head = None
        new_top = self.top
        pop.len = pop.len -1
        
        
## fila / o primeiro a chegar é o primeiro a sair , o ultimo a entrar é o utlimo a sair 

def inserir_fila(self,elem):      
    node = Node(elem)
    if self.last is None:
        self.last = node
    else:
        new_last = self.last.next
        self.last = new_last
    if self.first is None:
        self.first = node
        self._size + 1
        
def remover_fila(self):
    if self.first is None:
        raise IndexError("erro de index")
    else:
        new_first = self.first.next
        self.first = None
        new_first = self.first
        
        
        
        
# listas 


def _getnode(self,index):
    pointer = self.head
    for i in range(index):    # desse modo , pointer caminha da primeira posição (cabeça)
        if pointer:           # até o index desejado pelo usuario, enquanto pointer haver um "next"
            pointer = pointer.next
        else:
            raise IndexError("Out of range")
    return pointer                       # pratica na linha 58


def inserir_lista(self,elem,index):
    node = node(elem)
    if self.index == 0:
        node.next = self.head
        self.head = node
    else:
        pointer = self._getnode(index-1)  # pointer é retornado aqui, uma posição antes
        node.next = pointer.next      # pratica na linjha 68/ 69 
        pointer.next = node
    self._size += 1
        

    
