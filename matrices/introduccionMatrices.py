def crearMatrices(fil,col):
    m = []
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m 
def printMatriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end=" ")
        print("")


def llenarMatriz(mat): ### llenado por filas
    for f in range(len(mat)):
        print("\n Fila #",f+1)
        for c in range(len(mat[f])):
            mat[f][c]= int(input(f"mat[{f+1}][{c+1}]?  "))
        print("")
matriz = crearMatrices(4,5)
llenarMatriz(matriz)
printMatriz(matriz)




