from array_ifpb import Array

class PilhaException(Exception):
    pass

    
class Pilha:

    def __init__(self):
        ...

    def esta_vazia(self):
        ...

    def tamanho(self):
        ...

    def empilhar(self, elemento):
        ...

    def desempilhar(self):
        ...

    def imprimir(self):
        ...
    
    def __str__(self):
        ...


class PilhaSequencial:

    def __init__(self):
        self._dados = []

    def esta_vazia(self):
        return self.tamanho() == 0

    def tamanho(self):
        return len(self._dados)

    def empilhar(self, elemento):
        self._dados.append(elemento)

    def desempilhar(self):
        if self.esta_vazia():
            raise PilhaException()
            
        return self._dados.pop()

    def imprimir(self):
        print(self._dados)
    
    def __str__(self):
        return f'Pilha()'
    

class PilhaSequencialArray:

    def __init__(self):
        self.__topo = 0
        self.__dados = Array(3)

    def esta_vazia(self):
        return self.__dados.vazio

    def tamanho(self):
        return self.__dados.tamanho

    def empilhar(self, elemento):
        if self.__dados.cheio:
            novo = Array(self.__dados.capacidade * 2)
            novo.copiar_de(self.__dados)
            self.__dados = novo

        self.__dados[self.__topo] = elemento
        self.__topo += 1

    def desempilhar(self):
        if self.esta_vazia():
            raise PilhaException()

        posicao = self.__topo - 1
        valor = self.__dados[posicao]
        del self.__dados[posicao]

        porcentagem_uso = (self.__dados.tamanho // self.__dados.capacidade) * 100
        if porcentagem_uso < 50:
            novo = Array(self.__dados.capacidade // 2)
            novo.copiar_de(self.__dados)
            self.__dados = novo

        self.__topo -= 1
        return valor

    def imprimir(self):
        print(self.__dados[0:self.__topo])
    
    def __str__(self):
        return 'Pilha()'
    

class Node:
    
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: 'Node' | None = proximo


class PilhaEncadeada:
    def __init__(self):
        self.__tamanho: int = 0
        self.__topo: Node | None = None

    def esta_vazia(self):
        return self.__topo is None

    def tamanho(self):
        return self.__tamanho

    def empilhar(self, elemento):
        self.__topo = Node(elemento, proximo=self.__topo)
        # if self.esta_vazia():
        #     self.__topo = Node(elemento)
        # else:
        #     novo_no = Node(elemento)
        #     novo_no.proximo = self.__topo
        #     self.__topo = novo_no
        self.__tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            raise PilhaException()
        
        valor = self.__topo.valor
        self.__topo = self.__topo.proximo
        self.__tamanho -= 1
        return valor

    def imprimir(self):
        no: Node = self.__topo
        print("[", end="")
        while no:
            print(f"{no.valor} ", end="")
            no = no.proximo
        print("]")
    
    def __str__(self):
        return 'Pilha()'
    
    def desempilhar_n(self, n):
        if n < 0 or n > self.tamanho:
            return False
        
        for x in range(n):
            self.desempilhar()
        return True
    
    def esvaziar(self):
        self.__topo = None
        self.__tamanho -= 1

    def obtem_base(self):
        no = self.__topo
        while no != None:
            if no.proximo == None:
                return no.valor
            no = no.proximo

    def inverter(self):
        pilha = PilhaEncadeada()
        while not self.esta_vazia():
            pilha.empilhar(self.desempilhar())
        
        self.__topo = pilha.__topo

    def concatenar(self, outra_pilha) -> 'PilhaEncadeada':
        pilha = PilhaEncadeada()
        while not self.esta_vazia():
            pilha.empilhar(self.desempilhar())

        while not outra_pilha.esta_vazia():
            pilha.empilhar(outra_pilha.desempilhar())
        
        pilha.inverter()
        return pilha