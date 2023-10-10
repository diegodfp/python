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

def llenarMatrizDos(mat): ### llenado por filas
    
    
    print(len(mat))
    for f in range(len(mat)):
        contador = 1
        contadorCol = len(mat)
        for c in range(len(mat[f])):
            if f % 2 == 0 :
                mat[f][c]= contador 
                contador += 1
            else:
                mat[f][c]= contadorCol 
                contadorCol -= 1
        print("")
def llenarMatrizTres(mat): ### llenado por filas
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if f == c :
                mat[f][c]= 1 
            else:
                mat[f][c]= 0
        print("")
def llenarMatrizUno(mat): ### llenado por filas
    contador = 1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c]= contador 
            contador += 1
        print("")
def llenarMatrizCuatro(mat): ### llenado por filas
    print(len(mat))
    contador = 0
    contadorCol = len(mat)-1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if f  == contador and c == contadorCol :
                mat[f][c]= 1 
                contador += 1
                contadorCol -=1
            else:
                mat[f][c]= 0 
                
        print("")
def llenarMatrizCinco(mat): ### llenado por filas
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if f >= c :
                mat[f][c]= 1 
            else:
                mat[f][c]= 0
        print("")
def llenarMatrizSeis(mat): ### llenado por filas
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if f <= c :
                mat[f][c]= 1 
            else:
                mat[f][c]= 0
        print("")
def llenarMatrizSiete(mat): ### llenado por columnas
    contador = 1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[c][f]= contador 
            contador += 1
        print("")
def llenarMatrizOcho(mat): ### llenado A y B
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if f >= c and c % 2 == 0:
                mat[f][c]= "A" 
            elif f >= c and c % 2 != 0:
                mat[f][c]= "B"
            else:
                mat[f][c]= " "
        print("")
###### MAIN PROGRAM ######
filas = int(input("ingrese la cantidad de filas"))
columnas = int(input("ingrese la cantidad de columnas"))
if filas == columnas :
    matriz = crearMatrices(filas,columnas)
    llenarMatrizUno(matriz)
    printMatriz(matriz)
    input("")
    llenarMatrizDos(matriz)
    printMatriz(matriz)
    input("")
    llenarMatrizTres(matriz)
    printMatriz(matriz)
    input("")
    llenarMatrizCuatro(matriz)
    printMatriz(matriz)
    input("")
    llenarMatrizCinco(matriz)
    printMatriz(matriz)
    input("")
    llenarMatrizSeis(matriz)
    printMatriz(matriz)
    input("")
    llenarMatrizSiete(matriz)
    printMatriz(matriz)
    input("")
    llenarMatrizOcho(matriz)
    printMatriz(matriz)
    input("")