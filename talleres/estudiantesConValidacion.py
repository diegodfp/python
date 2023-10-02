bandera = 1
while bandera ==1 :
    while True:
        try:
            codigo = input(" ingrese el codigo\n")
            if len(codigo) == 0 or codigo.isalnum()==False:
                print(" el espacio no puede estar vacio, intente")
                continue
            break
        except ValueError:
            print("Error. intentelo nuevamente")
    while True:
        try:
            nombre = input(" ingrese el nombre\n")
            if len(nombre) == 0 or nombre.isalnum()== False:
                print(" el espacio no puede estar vacio, intente otra vez")
                continue
            break
        except ValueError:
            print("Error. intentelo nuevamente")
    while True:
        try:
            programa = int(input(" ingrese el programa que esta cursando 1. por tec. en sistemas,2. Tec. VideoJuegos 3.Tec. en Animacion Digital\n"))
            if programa<1 or programa>3:
                print("error. debe ingresar un numero de 1 a 3")
                continue
            break
        except ValueError:
            print("Error. intentelo nuevamente")
    while True:
        try:
            beca = int(input(" ingrese la beca de la cual es beneficiario 1. para Excelencia, 2. para Deporte y 3. si no tiene\n"))
            if beca<1 or beca>3:
                print("error. debe ingresar un numero de 1 a 3")
                continue
            break
        except ValueError:
            print("Error. intentelo nuevamente")
    if programa == 1:
        matricula = 800000
    elif programa == 2:
        matricula =  1000000
    else:
        matricula = 1200000
    if beca == 1:
        matricula = matricula - (matricula*0.5)
    elif beca ==2:
        matricula = matricula - (matricula*0.4)
    else:
        matricula = matricula
    print (" el estudiante ",nombre, f"pagara de matricula {matricula:,}\n")
    while True:
        try:
            continuar = input(" si desea continuar escriba S/s, si no escriba N/n")
            
            if len(continuar) != 1 or continuar.isalpha == False:
                print(" ingreso una opcion invalida intente nuevamente")
                continue
            break
        except ValueError:
            print(" error.")

    if continuar == "n" or continuar =="N":
        bandera = 0
    elif continuar == "s" or continuar =="S":
        bandera = 1              
  
print("el programa ha terminado")