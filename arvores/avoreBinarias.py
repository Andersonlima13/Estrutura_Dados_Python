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
    def __init__(self,data=None):
        if data:
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