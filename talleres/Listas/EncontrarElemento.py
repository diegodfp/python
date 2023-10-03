### este programa encuentra la posision de un elemento en una lista, si no lo encuentra, devuelve -1

def findElemListpos(lst,elem):
    for p in range(len(lst)):
        if elem == lst[p]:
            return p
    return -1        

def findElenList(lst, elem):
    #funcion que busca un elemento en la lista
    #si lo encuentra devuelve True, si no, False
    for e in lst:
        if e == elem:
            True
    return False

