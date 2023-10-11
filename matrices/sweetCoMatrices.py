def calcdia(matVtas, matPrecios):
    fil = len(matVtas)
    lstTotVtas = [0]*fil
    for f in range(fil):
        lstTotVtas[f] = sum(matVtas[f])* matPrecios[f]
    maxVtas = max(lstTotVtas)
    prodMaxVtas = lstTotVtas.index(maxVtas) + 1
    return prodMaxVtas
#def calDiaMaxIngresos(matVtas, matPrecios):

def calcProdMaxIngresosSem(matVtas, matPrecios):
    fil = len(matVtas)
    listaDias= [0]*7
    
    for c in range(7):
        sumatoriaDia = 0
        for f in range(5):
            sumatoriaDia= sumatoriaDia + (matVtas[f][c] * matPrecios[f])
        listaDias[c]= sumatoriaDia
    print(listaDias)
    maxVtas = max(listaDias)
    prodMaxVtas = listaDias.index(maxVtas) + 1
    return prodMaxVtas


matVtas = [[100, 88, 92, 94, 85, 110, 118],
           [30, 42, 31, 32, 38, 40, 37],
           [23, 35, 39, 45, 55, 60, 61],
           [45, 50, 56, 65, 47, 57, 68],
           [18, 25, 33, 21, 22, 28, 32]
           ]
matPrecios = [1500, 5000, 6500, 2500, 22500]
prodMaxIngSem = calcdia(matVtas,matPrecios)
diaMaxIngreso =  calcProdMaxIngresosSem(matVtas,matPrecios)
print(f"El producto que mas vende de la semana es: {prodMaxIngSem}")
print(f"El dia que mas vende de la semana es: {diaMaxIngreso}")