class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# O ULTIMO ITEM A ENTRAR É O PRIMEIRO A SAIR

class Pilha:
    
# INICIO DA PILHA 
    def __init__(self):
        self.top = None
        self.size = 0

# TESTA SE A FILA ESTÁ OU NÃO VAZIA
    def esta_vazia(self):
        return self.size == 0
        
# VERIFICA O TAMANHO DA PILHA
    def tamanho(self):
        return self.__len__()

# INSERE ELEMENTOS NA PILHA

    def empilhar(self, elemento):
        node = Node(elemento)
        if self.top:
            new_top = node
            new_top.next = self.top
            self.top = new_top
        else:
            self.top = node
        self.size = self.size + 1
            
# MÉTODO ESPECIAL PARA VERIFICAR O TAMANHO
    def __len__(self):
        return self.size
        
# REMOVER ELEMENTO DA PILHA
    def desempilhar(self):
        if self.top:
            pointer = self.top
            self.top = pointer.next
            self.size = self.size - 1
        else:
            raise IndexError("Não existem elementos para remover")
            
# IMPRIMIR A FORMA DE PIILHA    
            
    def imprimir(self):
        string = ""
        pointer = self.top
        while(pointer):
            string = string + str(pointer.data) + "->"
            pointer = pointer.next
        return string
            
    def __str__(self):
        return self.imprimir()
  

# ESVAZIAR A PILHA TOTALMENTE    

    def esvaziar_pilha(self):
        self.top = None
        self.size = 0

# RETORNAR O ELEMENTO DO TOPO

    def retorna_topo(self):
        if self.top:
            return self.top.data       

pilha = Pilha()
pilha.empilhar(8)
pilha.empilhar(9)
pilha.empilhar(10)
pilha.esvaziar_pilha()
pilha.empilhar(10)
pilha.empilhar(14)
pilha.empilhar(11)
print(pilha.retorna_topo())
print(pilha.esta_vazia())
print(pilha.imprimir())