class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
  
  
# O PRIMEIRO ELEMENTO A ENTRAR É O PRIMEIRO A SAIR 
# INSERIMOS NO FINAL E REMOVEMOS DO INICIO

class Fila:
	def __init__(self):
		self.first = None
		self.last = None
		self._size = 0
	
	def index(self,elem):
		pass
 
	
	def remove(self):
		if self.first is not None:
			elem = self.first.data
			self.first = self.first.next
			self._size = self._size - 1
			return elem
		raise IndexError("A fila está vazia")

	
	def insert(self,elem):
		node = Node(elem)
		if self.last is None:
			self.last = node
		else:							 # CASO JA TENHA ELEMENTO NA POSIÇÃO LAST , FAREMOS O PROXIMO DO ULTIMO ELEMENTO
			self.last.next = node		 # SABER QUE UM NOVO NODE FOI ADCIONADO , RECEBENDO ESSE VALOR, ASSIIM SELF.LAST
			self.last = node			 # PASSA A SER O ELEMENTO QUE ACABOU DE CHEGAR 
		if self.first is None:
			self.first = node
		self._size = self._size + 1
  
	def __repr__(self) -> str:
		string = ""
		pointer = self.first
		while(pointer):
			string = string + str(f" [{pointer.data}]") + "|"
			pointer = pointer.next
		return string
   
	def modify(self,elem):
		pass

	def impress(self):
		return self.__repr__()


	def __len__(self):
		return self._size

	def is_empty(self):
		return len(self) == 0


fila = Fila()
fila.insert(4)
fila.insert("anderson")
fila.insert(False)
print(fila.impress())
print(fila.__len__())
fila.remove()
print(fila.impress())
fila.remove()
print(fila.impress())