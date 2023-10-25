import json
def leerRuta():
    while True:
        try:
            nom = input("Ingrese el nombre del archivo del cual cargara la informacion:  ")
            nom = nom.strip()
            if len(nom) == 0:
                print("Nombre del archivo inválido, no puede ir vacio")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre del archivo.", e)
def menu():
    print("\n")
    print(" BIBLIOTECA ".center(100,"="))
    print(" MENU ".center(100,"="))
    print("1 - INSERTAR REGISTRO")
    print("2 - CONSULTAR Y LISTAR OBSERVATORIOS")
    print("3 - AÑADIR UN REGISTRO DE TEMPERATURA")
    print("4 - LISTAR OBSERVACIONES DE TEMPERATURA POR DIA, MES O AÑO")
    print("5 - LISTAR TEMP MAX, MIN  Y PROMEDIO")
    print("6 - LISTADO DE TODAS LAS OBSERVACIONES A NIVEL NACIONAL")
    print("7 - Listado de las observaciones a nivel nacional agrupadas porbservatorio.")
    print("8 - salir.")
    print("\n")

def cargarRuta(ruta):
    try:
        with open(ruta, "r") as archivo:
            listadeRegistros = json.load(archivo)
        return listadeRegistros
    except FileNotFoundError:
        return []
    
def validacionTexto(msg):
    while True:
        try:
            texto = input(msg)
            if texto.isalpha() or not texto.isspace():
                return texto
            else:
                print("-" * 50)
                print("Solo se permiten letras")
                print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"{e}")
            print("-" * 50)
def validarFecha(msg):
    
    while True:
        fechaReporte = input(msg)
        try:
            partes = fechaReporte.split("/")
            if len(partes[0])==2 and len(partes[1])==2 and len(partes[2])==4:
                valido = True   
                for p in partes:
                    if not p.isdigit():
                        valido = False
                        break
                if valido:
                    return fechaReporte
                else:
                    print("formato no valido")       
            else:
                print("formato no valido")
        except Exception as e:
            print("Error al ingresar la fecha .", e)
def validacion(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero

        except ValueError:
            print("-" * 50)
            print("Solo se permiten numeros enteros")
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"{e}")
            print("-" * 50)

def escribirEnDisco(ruta, dicc):
    with open(ruta, "w") as archivo:
        json.dump(dicc, archivo)
    if not archivo.closed:
        archivo.close()
def existeId(id, lstPersonal):

    for i, datos in enumerate(lstPersonal):
        k = datos['id']
        if k == id:
            return i
    return -1

def buscarId(id, lstPersonal):

    for i, datos in enumerate(lstPersonal):
        
        k = datos['id']
        if k == id:
            return i
    return -1
def registrarObservatorio(ruta, registros):
    idObservatorio = str(validacion("Ingrese la ID del observatorio: "))
    while existeId(idObservatorio, registros) != -1:
        print("--> Ya existe un registro con ese ID")
        input("Presione cualquier tecla para continuar\n")
        idObservatorio = str(validacion("Ingrese la ID del observatorio: "))
    nombreObservatorio = validacionTexto("Ingrese el nombre del observatorio ") 
    registrosTemp = []

    nuevoRegistro = {
        "id": idObservatorio,
        "nombre": nombreObservatorio,
        "reporte": registrosTemp,
    }

    registros.append(nuevoRegistro)
    escribirEnDisco(ruta, registros)
    
def ingresarRegistro(ruta, registros):
    id = str(input("Ingrese el ID del observatorio donde agregara el registro: "))
    
    index = buscarId(id, registros)
    if index == -1:
        print("No existe un observatorio con ese ID")
        input("Presione cualquier tecla para continuar\n")
    else:
        while True:
            ruta = leerRuta()
            try:
                fd = open("/home/spukN01-019/Documents/Diego/python/archivos/json/"+ruta,"r")
                ##fd = open("/home/spukN01-019/Documents/Diego/python/archivos/json/registro.csv","r")
                break
            except:
                print("Error. archivo no encontrado, asegurese que lo digito bien \n")
                continue
        fechaRegistro = validarFecha(" ingrese la fecha del reporte:  ")
        for registroTmp in fd:
            if not registroTmp.startswith("ID"):
                listRegistros = registroTmp.split(";")
                
                if registros[index]["nombre"] ==  listRegistros[1].lower():
                    
                    nuevoRegistro = {
                        "fechaReporte": fechaRegistro,
                        "tempMaxima": listRegistros[0],
                        "tempMinima":listRegistros[2]}
                    registros[index]["reporte"].append(nuevoRegistro)
                    escribirEnDisco(ruta, registros)
        print("proceso logrado") 
        fd.close()                  
def listarObservatorios(registros):
    opcion = validacion("Elija una opción para listar los observatorios:\n1 - ascendentemente por sus códigos \n2 - ascendentemente por su nombre\nOpción: ")

    if opcion == 1:
        if registros:
            
            observatoriosOrdenados = sorted(registros, key=lambda x: (x["id"]))
            print("--------Lista Ordenada por ID----------")
            for idOb in observatoriosOrdenados:
                
                print(f"ID: {idOb['id']}")
                print("-"*40)
                print(f"Nombre observatorio: {idOb['nombre']}")  
                print("-"*40)
    if opcion == 2:
        if registros:
            observatoriosOrdenados = sorted(registros, key=lambda x: (x["nombre"]))
            print("--------Lista Ordenada por nombre---------")
            for idOb in observatoriosOrdenados:
                print(f"ID: {idOb['id']}")
                print(f"Nombre observatorio: {idOb['nombre']}") 
def listarObservaciones(registros):
    print(" Listado de observaciones de un observatorio en particular")
    opcion2 = validacion(" Eliga una opcion para ordenar los reportes \n1- Para ordenarlos por dia \n2. Ordenadas por mes \n3. ordenarlas por año \n Opcion: ")
    if opcion2 ==1:
        if registros:
            id = str(input("Ingrese el ID del observatorio del cual quiere ver los reportes "))
            
            index = buscarId(id, registros)
            if index == -1:
                print("No existe un observatorio con ese ID")
                input("Presione cualquier tecla para continuar\n")
            else:
                observatoriosOrdenados = sorted(registros[index]["reporte"], key=lambda x: (x["fechaReporte"].split("/")[0]))
                for idOb in observatoriosOrdenados:
                    print(f"Fecha del reporte: {idOb['fechaReporte']}")
                    print("--------------------------------")
                    print(f"Temperatura Maxima: {idOb['tempMaxima']}")
                    print("--------------------------------")
                    print(f"Temperatura Minima: {idOb['tempMinima']}")
                    print("--------------------------------")
    if opcion2 ==2:
        if registros:
            id = str(input("Ingrese el ID del observatorio del cual quiere ver los reportes "))
            
            index = buscarId(id, registros)
            if index == -1:
                print("No existe un observatorio con ese ID")
                input("Presione cualquier tecla para continuar\n")
            else:
                observatoriosOrdenados = sorted(registros[index]["reporte"], key=lambda x: (x["fechaReporte"].split("/")[1]))
                for idOb in observatoriosOrdenados:
                    print(f"Fecha del reporte: {idOb['fechaReporte']}")
                    print("--------------------------------")
                    print(f"Temperatura Maxima: {idOb['tempMaxima']}")
                    print("--------------------------------")
                    print(f"Temperatura Minima: {idOb['tempMinima']}")   
                    print("--------------------------------")
    if opcion2 ==3:
        if registros:
            id = str(input("Ingrese el ID del observatorio del cual quiere ver los reportes: "))
            
            index = buscarId(id, registros)
            if index == -1:
                print("No existe un observatorio con ese ID")
                input("Presione cualquier tecla para continuar\n")
            else:
                observatoriosOrdenados = sorted(registros[index]["reporte"], key=lambda x: (x["fechaReporte"].split("/")[3]))
                for idOb in observatoriosOrdenados:
                    print(f"Fecha del reporte: {idOb['fechaReporte']}")
                    print("--------------------------------")
                    print(f"Temperatura Maxima: {idOb['tempMaxima']}")
                    print("--------------------------------")
                    print(f"Temperatura Minima: {idOb['tempMinima']}")      
                    print("--------------------------------")
def listarPromedios(registros):
    id = str(input("Ingrese el ID del observatorio del cual quiere ver los reportes "))   
    index = buscarId(id, registros)
    if index == -1:
        print("No existe un observatorio con ese ID")
        input("Presione cualquier tecla para continuar\n")
    else:
        cReportes= 0
        tempMax = 0
        tempMin = 0
        for idOb in registros[index]["reporte"]:
            if tempMax <= float(idOb["tempMaxima"]):
                tempMax = float(idOb["tempMaxima"])
            tempMinima = idOb["tempMinima"].strip("\n")
            if tempMin <= float(tempMinima)  :
                tempMin = float(tempMinima)
            cReportes +=1 
    promedio = (tempMax + tempMin)/2
    print("--------------------------------")
    print(f"cantidad de reportes: {cReportes}")
    print("--------------------------------")
    print(f"temperatura maxima: {tempMax}  ")
    print("--------------------------------")
    print(f"temperatura minima: {tempMin}  ")
    print("--------------------------------")
    print(f"el promedio de la temperatura es: {promedio}")
    print("--------------------------------")

def listarTodasObservaciones(registros):
    if registros:
            observatoriosOrdenados = sorted(registros, key=lambda x: (x["id"]))
            for idOb in observatoriosOrdenados:
                print(f"ID: {idOb['id']}")
                print(f"Nombre observatorio: {idOb['nombre']}")  
                tempMaxima = float(idOb['reporte'][1]["tempMaxima"])
                tempMinima = float(idOb['reporte'][1]["tempMinima"])
                promedio = (tempMaxima+tempMinima)/2
                print(f"Temperatura Maxima: {tempMaxima}")
                print("--------------------------------")
                print(f"Temperatura Minima: {tempMinima}")
                print("--------------------------------")
                print(f"Temperatura Minima: {promedio}") 
                print("--------------------------------") 
def listarTodasAgrupadas(registros):
    if registros:
            observatoriosOrdenados = sorted(registros, key=lambda x: (x["id"]))
            for idOb in observatoriosOrdenados:
                print(f"ID: {idOb['id']}")
                print(f"Nombre observatorio: {idOb['nombre']}")  
                tempMaxima = float(idOb['reporte'][1]["tempMaxima"])
                tempMinima = float(idOb['reporte'][1]["tempMinima"])
                promedio = (tempMaxima+tempMinima)/2
                print(f"Temperatura Maxima: {tempMaxima}")
                print("--------------------------------")
                print(f"Temperatura Minima: {tempMinima}")
                print("--------------------------------")
                print(f"Temperatura Minima: {promedio}") 
                print("--------------------------------") 
def escoger(opcion,registros,ruta):
    print("\n")
    if opcion == 1:
        print("Ingresar Observatorio".center(100,"="))
        registrarObservatorio(ruta,registros)

    elif opcion == 2:
        print("Listar Observatorios".center(100,"="))
        listarObservatorios(registros)
    elif opcion == 3:
        print("registrar Reporte de temperatura".center(100,"="))
        ingresarRegistro(ruta,registros)
    elif opcion == 4:
        print("Listado de observaciones de un observatorio en particular ".center(100,"="))
        listarObservaciones(registros)
    elif opcion == 5:
        print("Listado de cantidades de observaciones".center(100,"="))
        listarPromedios(registros)
    elif opcion == 6:
        print("Listado de todas las observaciones a nivel nacional ".center(100,"="))
        listarTodasObservaciones(registros)
    elif opcion == 7:
        print("Listado de las observaciones a nivel nacional agrupadas por observatorio.  ".center(100,"="))
        listarTodasAgrupadas(registros)
    elif opcion == 8:
        print("¡Hasta luego!".center(100,"="))
        salir = validacionTexto("Presione cualquier tecla para salir o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")















##### MAIN CODE ####
ruta = "/home/spukN01-019/Documents/Diego/python/archivos/json/registrosMetereologicos.json"

while True:
    diccMetereologico = cargarRuta(ruta)
    input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
    menu()
    escoger(validacion("Opcion 1 a 8: "),diccMetereologico,ruta)
    print("\n")

