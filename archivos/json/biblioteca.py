import json

def menu():
    print("\n")
    print(" BIBLIOTECA ".center(100,"="))
    print(" MENU ".center(100,"="))
    print("1 - INSERTAR")
    print("2 - CONSULTAR")
    print("3 - SALIR")
    print("\n")

def cargarRuta(ruta):    
    dicc = {}
    try:
        with open(ruta, "r") as archivo:
            dicc = json.load(archivo)
        return dicc
    except:
        with open(ruta, "w") as archivo:
            return dicc
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
def comprobarDicc(dicc, id_cliente):
    try:
        if dicc[id_cliente]:
            return False
        else:
            dicc[id_cliente] = {}
    except:
        dicc[id_cliente] = {}

    return dicc
def escribirEnDisco(ruta, dicc):
    with open(ruta, "w") as archivo:
        json.dump(dicc, archivo)
    if not archivo.closed:
        archivo.close()
def ingresarLibro(diccLibro):
    idLibro = validacion("Ingrese la ID del libro: ")
    existente = True
    existente = comprobarDicc(diccLibro, idLibro)
    if not existente:
        return print("*****Ya se ha ingresado este ID del libro*****")
    tituloLibro = validacionTexto("Ingrese el Titulo del libro: ") 
    autorLibro = validacionTexto("Ingrese el Titulo del libro: ")
    precio = validacion("Ingrese el precio del libro: ")
    diccLibro[idLibro]["titulo"] = tituloLibro
    diccLibro[idLibro]["autor"] = autorLibro
    diccLibro[idLibro]["precio"] = precio
    escribirEnDisco(ruta, diccLibro)
    print("Proceso realizado".center(50, "-"))

def mostrarLibros(diccLibro):
    
    if diccLibro:
        
        idBuscar = str(validacion("Ingrese el ID del libro que desea buscar: "))
        if idBuscar in diccLibro:
            libro = diccLibro[idBuscar]
            print(f"ID del Libro: {idBuscar}")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Precio: {libro['precio']}")
            print("-" * 50)
    else:
        print("no se han encontrado libros")
def escoger(opcion,diccBiblio):
    print("\n")
    if opcion == 1:
        print("libros".center(100,"="))
        ingresarLibro(diccBiblio)

    elif opcion == 2:
        print("libros".center(100,"="))
        mostrarLibros(diccBiblio)

    elif opcion == 3:
        print("¡Hasta luego!".center(100,"="))
        salir = validacionTexto("Presione cualquier tecla para salir o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")



##### MAIN CODE ####
ruta = "C:\\Users\\campus\\Documents\\python\\biblioteca.json"

while True:
  diccBiblioteca = cargarRuta(ruta)
  input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
  menu()
  escoger(validacion("Opcion 1 a 4: "),diccBiblioteca)
  print("\n")