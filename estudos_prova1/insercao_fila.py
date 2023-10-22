# fila encadeada 
# sempre inserimos no final , e retiramos no começo
from Node import Node


class Fila:
    def __init__(self):	
        self.first = None
        self.last = None
        self.size = 0

    def insert(self,elem):        # LOGICA DE INSERÇÃO EM FILAS
        node = Node(elem)         # CRIAMOS O NÓ
        if self.last is None:     # SE O ULTIMO ELEMENTO NAO EXISTE , ENTÃO ELE RECEBE O NÓ CRIADO
            self.last = node
        else:                       # NA OUTRA SITUAÇÃO , SE O ELEMENTO JÁ EXISTE...
            self.last.next = node   # ENTÃO O PROXIMO DO NOSSO ULTIMO ELEMENTO, QUE TINHA COMO PROXIMO O VALOR "NONE" PASSA A TER O VALOR DE NODE
            self.last = node        # AGORA , O SELF.LAST PASSA A SER O NÓ QUE ACABA DE SER INSERIDO
        if self.first is None:      # NO ULTIMO CASO, NÃO EXISTE UM PRIMEIRO ELEMENTO
            self.first = node       # LOGO ADCIONAMOS NA PRIMEIRA POSIÇÃO , QUE TAMBÉM É ULTIMA
        self.size = self.size + 1
        


                                 # LOGICA DA IMPRESSÃO:
    def imprimir(self):          
        string = ""              # DEFINIR UMA STRING VAZIA
        pointer = self.first     # CRIAMOS UMA VARIAVEL DE PONTEIRO QUE COMEÇA APONTANDO PARA O PRIMEIRO ELEMENTO
        while(pointer):          # ENQUNTO O POTEIRO FOR DIFERENTE D NONE , OU SEJA , ENQUANTO N FOR O ULTIMO
            string = string + str(pointer.data) + "->" # CONCATENAMOS A STRIG COM POINTER.DATA 
            pointer = pointer.next                     # INDICAMOS QUE VARIAVEL POINTER VAI APONTAR SEMPRE AO PROXIMO ELEMENTO
        return print(string)
    
    def remover(self):
        if self.first and self.last is None:
            raise IndexError(f"A fila está vazia")
        else:
            pointer = self.first
            self.first = pointer.next         
        self.size - 1
    
    
fila = Fila()
fila.insert("PRIMEIRO ELEMENTO")
fila.insert("SEGUNDO ELEMENTO")
fila.insert("TERCEIRO ELEMENTO")
fila.insert("QUARTO ELEMENTO")
fila.insert("QUINTO ELEMENTO")
fila.insert("SEXTO ELEMENTO")
fila.remover()
fila.remover()
fila.imprimir()