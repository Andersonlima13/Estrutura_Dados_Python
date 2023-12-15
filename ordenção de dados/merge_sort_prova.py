# QUESTÃO DE PROVA ! "MERGE = DIVIDIR PARA CONQUISTAR"
# O ALGORITIMO É BASEADO EM DIVIDIR SUA LISTA AO PONTO QUE TRANSFORME
# UMA LISTA EM VARIAS SUB-LISTAS (COM UM VALOR APENAS)
# LOGO LISTA = [7,5,1,4,6,4] VIRA = [7] [5] [2] [4] [6] [4]


def merge_sort(lista,inicio=0,fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio < 1):
        meio = (fim + inicio)//2    # DIVIDIMOS AQUI A LISTA
        merge_sort(lista,inicio,meio)  # UMA LISTA VAI DO INICIO AO MEIO (QUE VAI SER ENTENDIDO COMO FIM
        merge_sort(lista,meio,fim)     # DEPOIS , DO MEIO ATÉ O FINAL
        merge(lista,inicio,meio,fim)   # AQUI , IREMOS JUNTAR A LISTA
        


def merge(lista,inicio,meio,fim):
    left = lista[inicio:meio] # DIVIDIMOS A LISTA ENTRE ESQUERDA E DIREITA 
    right = lista[meio:fim]
    top_left,top_right = 0,0  # ATRIBUIMOS O VALOR DO TOPO INCIANDO COM "0" PARA AMBAS AS LISTAS
    for i in range(inicio,fim):
        if top_left >= len(left):
            lista[i] = right[top_right]
            top_right = top_right + 1
        if top_right >= len(right):
            lista[i] = left[top_left]
            top_left = top_left + 1
        if left[top_left] < right[top_right]:
            lista[i] = left[top_left]
            top_left =  top_left + 1
        else:
            lista[i] = right[top_right]
            top_right = top_right + 1
    