import json

def menu():
    while True:
        try:
            print("\n")
            print("**Registro del Personal***".center(40))
            print("MENU")
            print("1- Agregar")
            print("2- Modificar")
            print("3- Eliminar")
            print("4- Ver")
            print("5- Salir")
            print("\n")
            op = int(input(">>> opcion (1/5)?"))
            if op < 1 or op > 5:
                print ("Opcion no valida, intentelo de nuevo.")
                input(" presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print ("Debe ser un numero entero. Intente de nuevo.")
def cargarInfo(lstPersonal,rutaFile):
    
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error. No se pudo cargar la informacion \n",e)
        return None
    print(lstPersonal)
    fd.close()
    return lstPersonal

def existeId(id,lstPersonal):
    
    for datos in lstPersonal:
        k = int(list(datos.keys())[0])
        if k == id:
            return True
    return False
def guardarEmpleado(lstPersonal,ruta):
    try:
        fd = open(ruta,"w")
    except Exception as e:
        print("Error al abrir el archivo para guardar el empleado \n",e)
        return None
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print(" Error al guardar la informacion del empleado. \n",e)
        return False
    fd.close()
    return True

def agregarPersonal(lstPersonal, ruta):
    print("\n\n1. Agregar Personal")

    id = int(input(" Ingrese el ID: "))
    while existeId(id, lstPersonal):
        print("El Id ya esta registrado en el sistema.\nIngrese uno diferente:")
        input()
        id = int(input(" Ingrese el ID: "))
    nombre =  input(" nombre: ")
    edad =  input(" edad: ")
    sexo =  input(" sexo: (M/F) ")
    telefono =  input(" Telefono: ")
    dicEmpleado = {}
    dicEmpleado[id] = {"nombre":nombre,"edad":edad,"sexo":sexo,"telefono":telefono}
    lstPersonal.append(dicEmpleado)

    if guardarEmpleado(lstPersonal, ruta) == True:
        input(" El empleado ha sido registrado con exito. \n presione cualquier tecla para continuar")
    else:
        input("ocurrio algun error al guardad el empleado")
#### Main Program ####
rutaFile = "/home/spukN01-019/Documents/Diego/python/archivos/json/datPersonal.json"
lstPersonal = []
lstPersonal = cargarInfo(lstPersonal,rutaFile)
while True:
    
    op = menu()
    if op == 1:
        agregarPersonal(lstPersonal,rutaFile)
    if op == 2:
        #modificar
        pass
    if op == 3:
        #eliminar
        pass
    if op == 4:
        #ver
        pass
    else:
        print("¡Hasta luego!".center(50,"-"))
        exit()