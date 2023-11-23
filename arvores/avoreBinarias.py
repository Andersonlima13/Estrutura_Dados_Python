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
    
# inserção em arvore binaria 
# fazemos a verificaçao para encontrar um nó vazio ultilizando da recursao
# depois verificar ambos os lados e fazer a adiçao do valor       
    
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


# BUSCA EM ARVORE
# começamos pela raiz da arvore
# se o dado buscado for encontrado , retornamos a arvore inteira
# se o valor for menor buscamos pela esquerda , retornamos e vamos na direita 


    
    def busca(self,value):
        if node == 0:
            node = self.root
        if node is None or node.data == value:
            return BinaryTree(node)
        if value < node.data:
            return self.busca(value, node.left)
        return self.busca(value, node.right)
    
    
    def min(self,node):   # LOGICA PARA ENCONTRAR O MINIMO _ > ENQUANTO EXISTIR NODE.LEFT , ELE DESCE ATÉ O VALOR MAIS BAIXO
        atual = node
        while atual.left:
            atual = atual.left
        return atual
    
# REMOÇAO ARVORE    
    def remove(self,value,node=root):
        if node == root:            # PRIMEIRA SITUAÇÃO -> SE O NÓ TIVER O VALOR DA RAIZ , ENTAO NODE COMEÇA A PARTIR DA RAIZ
            node = self.root        
        if node is None:             # SE NODE É NONE , ENTAO RETORNAMOS O NÓ
            return node
        if value < node.data:                     # FAZEMOS A VERIFICAÇÃO PARA AMBOS OS LADOS
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value,node.right)
        else:                                      # SE NÃO FOR NEM MAIOR NEM MENOR (IGUAL) AI SIM FAREMOS  A REMOÇÃO
            if node.left is None:                  # PRIMEIRO VERIFICAMOS SE AMBOS OS LADOS POSSUEM O VALOR NONE E RETORNAMOS O OUTRO
                return node.right     
            elif node.right is None:
                return node.left
            else:                                  # SE NENHUM VALOR NONE FOR ENCONTRADO, ENTAOBUSCAMOS O MENOR VALOR (PARA DIREITA)
                substitute = self.min(node.right)   # NODE.DATA RECEBE ESSE MENOR VALOR
                node.data = substitute
                node.right = self.remove(substitute)  # QUE POR SUA VEZ É REMOVIDO
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

    def min(self,node):   # LOGICA PARA ENCONTRAR O MINIMO _ > ENQUANTO EXISTIR NODE.LEFT , ELE DESCE ATÉ O VALOR MAIS BAIXO
        atual = node       # atribuimos uma variavel 
        while atual.left:  # enqual o lado esquerdo existir
            atual = atual.left  # a variavel atuaçiza recebendo o novo valor (que vai sempre ser menor)
        return atual             # retornamos 



    def remover(self,node=root,value):
        if node == root:
            node = self.root
        if node is None:
            return node
        else:
            if value < node.data:
                node.left = self.remove(value,self.left)
            elif value > node.data:
                node.right = self.remove(value,self.right)
            else:
                if node.left is None:
                    return node.left
                elif node.right is None:
                    return node.right
                else:
                    substitue = self.min(node.right)
                    node.data = substitue
                    node.right = self.remover(node.right,substitue)
                    
    
    def add(self):
        self.root = self._add(self.root,value)
    
                
    def _add(self,node,value):
        if node is None:
            return node(value)
        else:       
            if node < node.data:
                node.left = self._add(node.left,value)
            else:
                node.right = self._add(node.rigt,value)
            return node
        
    def busca(self,value):
        if value == 0:
            node = self.root
        if node is None or node.data == value:
            return node(value)
        if node < node.data:
            return self.busca(node.left,value)
        return self.busca(node.right,value)