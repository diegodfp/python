continuar = 0
valorTotalMatriculas = 0
while continuar == 0:
    codigo = input(" indique su codigo\n")
    nombre = input(" indique su nombre\n")
    programa = int(input("indique el programa al cual pertenece [1: Tecnico en Sistemas,  2: Tec. Desarrollo de video juegos, 3. Animacion Digital]"))
    beca = int(input(" que tipo de beca tiene [seleccione 1. por rendimiento. 2. Beca cultural. 3. no posee :( ]")) 
    if programa == 1:
        tarifaBasica = 800000
    elif programa ==2:
        tarifaBasica = 1000000
    elif programa ==3:
        tarifaBasica = 1200000
    if beca == 1:
        tarifaBasica = tarifaBasica - ( tarifaBasica * 0.5)
    elif beca ==2:
        tarifaBasica = tarifaBasica - ( tarifaBasica * 0.4)
    elif beca ==3:
        tarifaBasica = tarifaBasica
    valorTotalMatriculas = tarifaBasica + valorTotalMatriculas
    print("nombre: ", nombre,"\n")
    print("debe pagar una tarifa basica de  ", tarifaBasica,"\n")

    sigue = input(" desea continuar? [s/S][n/N]")
    if sigue == "n" or sigue == "N":
        continuar = 1
print (" el valor total de las matriculas fue: ",valorTotalMatriculas)
print (" se termino el programa")