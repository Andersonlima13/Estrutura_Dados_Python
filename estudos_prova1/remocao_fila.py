

def remover(self):                       # PRIMEIRO CASO , SE A FILA ESIVER VAZIA , É IMPOSSIVEL DE REMOVER
    if self.fist and self.last is None:
        raise IndexError(f"A fila está vazia")
    else:
        pointer = self.first            # CRIAMOS A VAR DE PONTEIRO PARA APONTAR NO PRIMEIRO ELEMENTO,
        self.first = pointer.next       # AGORA, O PRIMEIRO ELEMENTO RECEBE O PRIMO ELEMENTO DO PONTEIRO
    self.size - 1                       # LOGO O ELEMENTO ANTIGO NÃO TEM MAIS CONEXÃO COM NINGUEM
    
def impress(self):
    string = ""
    pointer = self.first
    while(pointer):
        string = string + str(self.data) + "--"
        pointer = pointer.next
    return print(string)

     