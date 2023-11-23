class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            # Atualiza a altura do nó com base nas alturas das subárvores esquerda e direita
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        # Calcula o fator de balanceamento: altura da subárvore esquerda - altura da subárvore direita
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Realiza a rotação para a esquerda
        y.left = z
        z.right = T2

        # Atualiza as alturas após a rotação
        self.update_height(z)
        self.update_height(y)

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Realiza a rotação para a direita
        x.right = y
        y.left = T2

        # Atualiza as alturas após a rotação
        self.update_height(y)
        self.update_height(x)

        return x

    def insert(self, root, key):
        if root is None:
            # Se atingimos uma folha, criamos um novo nó
            return Node(key)

        if key < root.key:
            # Insere na subárvore esquerda
            root.left = self.insert(root.left, key)
        else:
            # Insere na subárvore direita
            root.right = self.insert(root.right, key)

        # Atualiza a altura do nó atual
        self.update_height(root)

        # Obtém o fator de balanceamento deste nó para verificar se ele ficou desequilibrado
        balance = self.balance_factor(root)

        # Casos de desequilíbrio

        # Caso Esquerda-Esquerda
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Caso Direita-Direita
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Caso Esquerda-Direita
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Caso Direita-Esquerda
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def insert_key(self, key):
        # Função de conveniência para inserir uma chave
        self.root = self.insert(self.root, key)
        
        
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Nó com uma ou nenhuma subárvore
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Nó com duas subárvores: Obtém o sucessor in-order (menor nó da subárvore direita)
            temp = self.get_min_value_node(root.right)

            # Copia o sucessor in-order para este nó
            root.key = temp.key

            # Remove o sucessor in-order
            root.right = self.delete(root.right, temp.key)

        # Atualiza a altura do nó atual
        self.update_height(root)

        # Obtém o fator de balanceamento deste nó para verificar se ele ficou desequilibrado
        balance = self.balance_factor(root)

        # Casos de desequilíbrio

        # Caso Esquerda-Esquerda
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        # Caso Direita-Direita
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        # Caso Esquerda-Direita
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Caso Direita-Esquerda
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete_key(self, key):
        self.root = self.delete(self.root, key)


# Exemplo de uso
avl_tree = AVLTree()
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    avl_tree.insert_key(key)
