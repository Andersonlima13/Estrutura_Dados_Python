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
        
        
## fila / o primeiro a chegar é o primeiro a sair , o ultimo a entrar é o utlimo a sair a sair

def inserir_fila(self,elem):
    node = Node(elem)
    if self.first is None:
        self.first = elem
        self.last = self.first
    else:
        pointer = self.first.next
        while pointer:
            if pointer.next is None:
                self.last = pointer.next
            
        

    