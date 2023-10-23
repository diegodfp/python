import json

def menu():
    print("\n")
    print(" BIBLIOTECA ".center(100,"="))
    print(" MENU ".center(100,"="))
    print("1 - INSERTAR")
    print("2 - CONSULTAR")
    print("3 - MODIFICAR")
    print("4-  ELIMINAR")
    print("5 - LISTAR LIBROS")
    print("6 - SALIR")
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
def ordenarDiccionario(diccLibro):
    diccOrdenado = {}
    for idLibro in sorted(diccLibro, key = lambda x:int(x)):
        diccOrdenado[idLibro] = diccLibro[idLibro]
    return diccOrdenado
def ingresarLibro(diccLibro):
    idLibro = str(validacion("Ingrese la ID del libro: "))
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
    diccOrdenado = ordenarDiccionario(diccLibro)
    escribirEnDisco(ruta,diccOrdenado)
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
def editarLibros(diccLibro):
    idLibro = str(validacion("Ingrese la ID del libro: "))
    existente = comprobarDicc(diccLibro, idLibro)
    
    if not existente:
        print("Elija el campo que desea modificar:")
        print("1 - Título del libro")
        print("2 - Autor del libro")
        print("3 - Precio del libro")
        
        opcion = validacion("Opción: ")
        
        if opcion == 1:
            nuevoValor = validacionTexto("Nuevo título: ")
            diccLibro[idLibro]["titulo"] = nuevoValor
        elif opcion == 2:
            nuevoValor = validacionTexto("Nuevo autor: ")
            diccLibro[idLibro]["autor"] = nuevoValor
        elif opcion == 3:
            nuevoValor = validacion("Nuevo precio: ")
            diccLibro[idLibro]["precio"] = nuevoValor
        else:
            print("Opción inválida.")
            return

        escribirEnDisco(ruta, diccLibro)
        print("El libro ha sido modificado con éxito.")
        input("Presione cualquier tecla para continuar\n")
    else:
        print("No hay un libro con ese ID.")
def listarLibros(diccLibro):
    opcion = validacion("Elija una opción para listar libros:\n1 - Por Autor\n2 - Por Nombre del Libro\n3 - Por Precio\nOpción: ")

    if opcion == 1:
        autor = validacionTexto("Ingrese el autor para listar los libros: ")
        libros_autor = [libro for libro in diccLibro.values() if libro.get("autor", "") == autor]
        if libros_autor:
            libros_autor_ordenados = sorted(libros_autor, key=lambda x: x["autor"])
            for libro in libros_autor_ordenados:
                print(f"ID del Libro: {libro['id']}")
                print(f"Título: {libro['titulo']}")
                print(f"Autor: {libro['autor']}")
                print(f"Precio: {libro['precio']}")
                print("-" * 50)
        else:
            print("No se encontraron libros con ese autor.")

    elif opcion == 2:
        nombre_libro = validacionTexto("Ingrese el nombre del libro para listar los libros: ")
        libros_nombre = [libro for libro in diccLibro.values() if libro.get("titulo", "") == nombre_libro]
        if libros_nombre:
            libros_nombre_ordenados = sorted(libros_nombre, key=lambda x: x["titulo"])
            for libro in libros_nombre_ordenados:
                print(f"ID del Libro: {libro['id']}")
                print(f"Título: {libro['titulo']}")
                print(f"Autor: {libro['autor']}")
                print(f"Precio: {libro['precio']}")
                print("-" * 50)
        else:
            print("No se encontraron libros con ese nombre.")

    elif opcion == 3:
        libros_ordenados_por_precio = sorted(diccLibro.values(), key=lambda x: x.get("precio", 0))
        for libro in libros_ordenados_por_precio:
            print(f"ID del Libro: {libro['id']}")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Precio: {libro['precio']}")
            print("-" * 50)
def eliminarLibro(diccLibro):
    idLibro = str(validacion("Ingrese la ID del libro que desea eliminar: "))
    if idLibro in diccLibro:
        del diccLibro[idLibro]
        escribirEnDisco(ruta, diccLibro)
        print("El libro ha sido eliminado con éxito.")
    else:
        print("No se ha encontrado un libro con ese ID.")
def escoger(opcion,diccBiblio):
    print("\n")
    if opcion == 1:
        print("libros".center(100,"="))
        ingresarLibro(diccBiblio)

    elif opcion == 2:
        print("libros".center(100,"="))
        mostrarLibros(diccBiblio)
    elif opcion == 3:
        print("libros".center(100,"="))
        editarLibros(diccBiblio)
    elif opcion == 4:
        print("libros".center(100,"="))
        eliminarLibro(diccBiblio)
    elif opcion == 5:
        print("libros".center(100,"="))
        mostrarLibros(diccBiblio)

    elif opcion == 6:
        print("¡Hasta luego!".center(100,"="))
        salir = validacionTexto("Presione cualquier tecla para salir o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")



##### MAIN CODE ####
ruta = "/home/spukN01-019/Documents/Diego/python/archivos/json/biblioteca.json"

while True:
    diccBiblioteca = cargarRuta(ruta)
    input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
    menu()
    escoger(validacion("Opcion 1 a 3: "),diccBiblioteca)
    print("\n")