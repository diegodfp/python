bandera = 0
cCategoriaA =0
cCategoriaB =0
cCategoriaC =0

valorTotalPagar =0
numeroDocentes = int(input(" ingrese el numero de docentes que desea liquidar\n"))
while bandera < numeroDocentes:
    try:
        cc = int(input(" ingrese su documento\n"))
        nombre = input(" ingrese su nombre\n")
        tipoDocente = (input(" ingrese su  categoria[A. B. C.]\n"))
        horasLaboradas= int(input(" ingrese la cantidad de horas que trabajo este mes\n"))
        if tipoDocente == "A" or  tipoDocente == "a":
            liquidacion = horasLaboradas * 25000
            cCategoriaA +=1
        
        if tipoDocente == "b" or  tipoDocente == "B":
            liquidacion = horasLaboradas * 35000
            cCategoriaB +=1
        if tipoDocente == "C" or  tipoDocente == "c":
            liquidacion = horasLaboradas * 50000
            cCategoriaC +=1
        valorTotalPagar = valorTotalPagar + liquidacion
        print ( " el docente", nombre, f" a ganado de honorarios $ {liquidacion:,}, por se categoria ",tipoDocente,"\n ")
        bandera += 1
    except:
        print("error")
print("\n","=="*30)
print(f" el valor total de las liquidaciones de todos los docentes, este mes es de {valorTotalPagar} \n")
print(" y hay ", cCategoriaA," docentes  categoria A, ",cCategoriaB," docentes categoria B y ",cCategoriaC," docentes categoria C")
