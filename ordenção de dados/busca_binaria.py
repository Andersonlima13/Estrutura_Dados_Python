def busca_binaria(array,item,inicio=0,fim=None):
    if fim is None:   # fazemos a verificação do 
        fim = len(array)-1 
    if inicio <= fim:    # se a sublista é valida , vamos calcular o meio
        meio = (inicio + fim)//2  # logo o meio será o valor de inicio + fim / 2
        if array[meio] == item: # primeira verificação , se o item do meio for o que estamos procurando
            return meio             # retornamos
        if item < array[meio]:   # se não , faremos a busca pela esquerda 
            return busca_binaria(array,item,inicio,meio-1)  # aqui , o fim será o começo -1
        else:
            return busca_binaria(array,item,meio+1,fim)  # enquanto aqui , modificamos o inicio, começado pelo meio +1
    return None