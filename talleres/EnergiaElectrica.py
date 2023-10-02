
continuar = 0
while continuar == 0:
    nombre = input(" indique su nombre\n")
    estrato = int(input(" indique su estrato \n"))
    if estrato == 1:
        tarifaBasica = 10000
    elif estrato ==2:
        tarifaBasica = 15000
    elif estrato ==3:
        tarifaBasica = 30000
    elif estrato ==4:
        tarifaBasica = 50000
    elif estrato ==5:
        tarifaBasica = 65000
    print("nombre: ", nombre,"\n")
    print("debe pagar una tarifa basica de  ", tarifaBasica," por ser estrato ", estrato, "\n")

    sigue = input(" desea continuar? [s/S][n/N]")
    if sigue == "n" or sigue == "N":
        continuar = 1
print (" se termino el programa")