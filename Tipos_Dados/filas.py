class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Fila:
	def __init__(self):
		self.first = None
		self.last = None
		self._size = 0

	def push(self,elem):
		pass


	def __len__(self):
		return self._size

	def empty(self):
		return len(self) == 0