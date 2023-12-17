def busca_binaria(array,item,inicio=0,fim=None):
    if fim is None:
        fim = len(array)-1
    if inicio <= fim:
        meio = (inicio + fim)//2
        if array[meio] == item:
            return meio
        if item < array[meio]:
            return busca_binaria(array,item,inicio,meio-1)
        else:
            return busca_binaria(array,item,meio+1,fim)
    return None