# DEFINIMOS O NÓ DA ARVORE , O QUAL CORRE A APENAS DUAS DIREÇÕES

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)


# percorrendo uma arvore
class BinaryTree:
    def __init__(self,data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    
    def in_Order(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            self.in_Order(node.left)
        print(node)
        if node.right:
            self.in_Order(node.right)

# PERCORRENDO EM PÓS ORDEM (OLHAMOS A ESQUERDA PRIMEIRO)
# VOCE SÓ VISITA A RAIZ APÓS VISITAR PRIMEIRO A ESQUERDA , E DEPOIS A DIREITA

    def pos_orderm(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            self.pos_ordem(node.left)
        if node.right:
            self.pos_ordem(node.right)
        print(node)
        

# INSERÇÃO EM ARVORE DE BUSCA
    
class BinaySearch(BinaryTree):
    def insert(self,value):
        parent = None
        i = self.root
        while(i):
            parent = i
            if value < i.data:
                i = i.left
            else:
                i = i.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)    
    
    
    def busca(self,value):
        if node == 0:
            node = self.root
        if node is None or node.data == value:
            return BinaryTree(node)
        if value < node.data:
            return self.busca(value, node.left)
        return self.busca(value, node.right)
    
    
    def min(self,node):
        atual = node
        while atual.left:
            atual = atual.left
        return atual
    
    def remove(self,value,node=root):
        if node == root:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value,node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute)
        return node
        
    
        
                
        
        
#tree = BinaryTree(7)
#tree.root.left = Node(18)
#tree.root.right = Node(14)
tree = BinaryTree()
n1 = Node("A")
n2 = Node("+")
n3 = Node("*")
n4 = Node("B")
n5 = Node("-")
n6 = Node("/")
n7 = Node("C")
n8 = Node("D")
n9 = Node("E")

n6.left = n7
n6.right = n8
n5.left = n6
n5.right = n9
n3.left = n4
n3.right = n5
n2.left = n1
n2.right = n3

tree.root = n2

tree.simetric_traversal()