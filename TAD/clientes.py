class Cliente:
    Nome = " "
    Fone = " "
    
# INTEFACE

def NovoCliente():
    cad = Cliente()
    cad.Nome = input("Digite o nome do cliente :  ")
    cad.Fone = input("Digite o numero do cliente:  ")
    return cad

def EscreverCliente(cad):
    print("Nome:", cad.Nome)
    print("Fone: ", cad.Fone, "\n")
    
    
def CriarAgenda(qtd):
    agenda = [Cliente()] * qtd
    for i in range (qtd):
        agenda[i] = NovoCliente()
    return
       