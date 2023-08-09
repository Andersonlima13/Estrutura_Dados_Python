from clientes import *

print("TESTE DO TAD CLIENTE")
print("NOMES \n")
qtd = int(input("Digite a quantidade de clientes:  "))
agenda = CriarAgenda(qtd)

print("-----------------------------------")
print("AGENDA DOS CLIENTES \n")
for cliente in agenda:
    EscreverCliente(cliente)
    
    
print("-----------------------------------")

for cliente in agenda:
    if cliente.Fone[:2] == "83":
        EscreverCliente(cliente)
    else:
        print("Nenhum cliente encontrado-")
    



