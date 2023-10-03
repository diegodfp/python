##### FUNCIONES #######
def leerInt(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1:
                print("Valor invalido. Debe ser mayo a 0")
                continue
            return n
        except ValueError:
            print("error al ingresar el numero")
def leerTexto(msj):
    while True:
        try:
            texto = input(msj)
            if len(texto) < 1:
                print("Recuerde que el texto no pude ir vacio")
                continue
            return texto
        except ValueError:
            print("error.")
def leerFloat(msj):
    while True:
        try:
            n = float(input(msj))
            if n < 0:
                print("nota invalida. Debe ser mayor o igual a 0")
                continue
            return n
        except ValueError:
            print("error al ingresar el numero")
def menu():
    while True:
        try:
            print("*** QUE DESEA HACER***")
            print("1. Agregar Empleado")
            print("2. Modificar Empleado")
            print("3. Buscar Empleado")
            print("4. Eliminar Empleado")
            print("5. Listar Empleado")
            print("6. Listar Nomina de un Empleado")
            print("7. Listar Nomina de Todos los Empleados")
            print("8. salir")
            op = int(input(">>> Escoga una Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")

#####  MAIN PROGRAM #####
lstEmpleados = []
lstid = []
lsthoras = []
lstValor = []

while True:
    opcion = menu()
    if opcion == 1:
        print("\n\n1. Agregar Empleado")
        contador = len(lstid)
        print(len(lstid))
        for i in range(0,contador+1):
            lstid.append(i)
            lstEmpleados.append(leerTexto("nombre?"))
            lsthoras.append(leerInt("horas trabajadas?"))
            lstValor.append(leerFloat("valor de la hora?"))
            op = input("\n desea continuar s o n")
            if op.lower() == "s":
                contador += 1
            else:
                break
                    
    elif opcion == 2:
        print("\n\n2. Modificar Campos de un empleado")
        id = leerInt("ingrese el id del empleado que desea modificar")
        lstEmpleados[id+1]= leerTexto("ingrese el nuevo nombre del empleado")
        lsthoras[id+1]= leerInt("ingrese las nuevas horas del empleado")
        lstValor[id+1]= leerFloat("ingrese el nuevo valor de las horas del empleado")
    elif opcion == 3:
        print("\n\n3. Eliminar Empleados")
        id = leerInt("ingrese el id del empleado que desea modificar")
        lstEmpleados.remove(id)
        lsthoras.remove(id)
        lstValor.remove(id)
        lstid.remove(id)
    elif opcion == 4:
        print(id)
        print(lstEmpleados)
        print(lsthoras)
        print(lstValor)
    elif opcion == 8:
        print("\n\nGracias por usar nuestro programa")
        print("Adios")
        input("Presione cualquier tecla para salir ...")
        break
    input("Presione cualquier tecla para volver al MENU...")







