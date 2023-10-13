

####  funciones para crear y llenar matrices #####
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

####### funcion Menu ####
def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar empleado")
            print("2. Modificar empleado")
            print("3. Buscar emplado")
            print("4. Eliminar empleado")
            print("5. Listar empleados")
            print("6. Listar nómina de un empleado")
            print("7. Listar nómina de todos los empleados")
            print("8. Salir")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")
################## funcion para escoger del menu ####
def escoger(opcion):
    if opcion == 1:
        print("AGREGAR".center(50,"-"))
        agregar()
    elif opcion == 2:
        print("MODIFICAR".center(50,"-"))
        modificar()
    elif opcion == 3:
        print("BUSCAR EMPLEADO".center(50,"-"))
        buscar()
    elif opcion == 4:
        print("ELIMINAR".center(50,"-"))
        eliminar()
    elif opcion == 5:
        print("LISTAR EMPLEADO".center(50,"-"))
        listar()
    elif opcion == 6:
        print("LISTAR NOMINA".center(50,"-"))
        listar_nomina()
    elif opcion == 7:
        print("LISTAR NOMINA DE TODOS LOS EMPLEADOS".center(50,"-"))
        listar_nomina_todos()
    elif opcion == 8:
        print("¡Hasta luego!".center(50,"-"))
        salir = validacion_t("Presione cualquier tecla para volver al menú o ingrese 'S' para salir: ")
        if salir.lower() == "s":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")
        input("Presione cualquier tecla para continuar")

### funcion para leer y validar datos(enteros y texto)
def leerValHoraEmpl():
    while True:
        try:
            n = int(input("Ingrese el valor de la hora trabajada del empleado: "))
            if n < 8000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [8000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerHoraTrabEmpl():
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 0 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

def leerNombreEmpl():
    while True:
        try:
            nom = input("Ingrese el nombre del empleado:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerIDEmpl():
    while True:
        try:
            n = int(input("Ingrese el ID del empleado: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
###### funcion para buscar id en diccionario diccionario ####
def buscarEmpleado(dicEmpleados, idEmpl):
    # return dicEmpleados.get(idEmpl) != None
    return idEmpl in dicEmpleados

###### funcion para buscar  en diccionario diccionario ####
def mnubuscarEmpleado(dicEmpleados):
    print("\n\n3. Buscar Empleado\n")
    
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(dicEmpleados, idEmpl)
    if existEmpl == False:
        print("El Empleado con ese código no ha sido ingresado.")
        input()
        return
    
    print("\n", "=" * 30)
    print("Nombre:", dicEmpleados[idEmpl]["nombre"])
    print("Horas trabajadas:", dicEmpleados[idEmpl]["HorasTrabajadas"])
    print("Valor de la hora:", dicEmpleados[idEmpl]["ValorHora"])
    print(f"Salario: ${dicEmpleados[idEmpl]['Salario']:,.2f}")
    input("\n Presione cualquier tecla para volver al menu...")

def modificarEmpleado(dicEmpleados):
    print("\n\n2. Modificar Empleado\n")
    
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(dicEmpleados, idEmpl)
    if existEmpl == False:
        print("El código del empleado no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreEmpl()
        dicEmpleados[idEmpl]["nombre"] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        dicEmpleados[idEmpl]["HorasTrabajadas"] = cantHoras
        
    elif op == 3:
        valHora = leerValHoraEmpl()
        dicEmpleados[idEmpl]["ValorHora"] = valHora
        
    dicEmpleados[idEmpl]["Salario"] = dicEmpleados[idEmpl]["ValorHora"] * dicEmpleados[idEmpl]["HorasTrabajadas"]

###### funcion para agregar en diccionario diccionario ####
def agregarEmpleado(dicEmpleados):
    print("\n\n*** 1. Agregar empleado\n")
    dicDatos = {}
    id = leerIDEmpl()
    if buscarEmpleado(dicEmpleados, id) == True:
        print("El id ya existe en la lista")
        input()
        return
    
    dicDatos["nombre"] = leerNombreEmpl()
    dicDatos["HorasTrabajadas"] = leerHoraTrabEmpl()
    dicDatos["ValorHora"] = leerValHoraEmpl()
    dicDatos["Salario"] = dicDatos["ValorHora"] * dicDatos["HorasTrabajadas"]
    
    dicEmpleados[id] = dicDatos


