def crearGrafo(nCiudades):
    # Inicializar la matriz de adyacencia con ceros
    grafo = [[0] * nCiudades for _ in range(nCiudades)]

    # Solicitar los nombres de las ciudades y construir el grafo
    ciudades = []
    for i in range(nCiudades):
        ciudad = input(f"Ingrese el nombre de la ciudad {i + 1}: ")
        ciudades.append(ciudad)

    for i in range(nCiudades):
        for j in range(i + 1, nCiudades):
            respuesta = input(f"¿{ciudades[i]} tiene acceso directo a {ciudades[j]}? (s/n): ")
            if respuesta.lower() == "s":
                grafo[i][j] = 1
                grafo[j][i] = 1

    return grafo, ciudades

def verificarRutaDirecta(grafo, ciudadOrigen, ciudadDestino, ciudades):
    try:
        indiceOrigen = ciudades.index(ciudadOrigen)
        indiceDestino = ciudades.index(ciudadDestino)
        return grafo[indiceOrigen][indiceDestino] == 1
    except ValueError:
        return False

############ main program ##########

nCiudades = int(input("Ingrese la cantidad de ciudades: "))
grafo, ciudades = crearGrafo(nCiudades)

while True:
    print("\nOpciones:")
    print("1. Verificar si hay ruta directa entre dos ciudades")
    print("2. Salir")
    opcion = input("Elija una opción (1/2): ")

    if opcion == "1":
        ciudadOrigen = input("Ingrese la ciudad de origen: ")
        ciudadDestino = input("Ingrese la ciudad de destino: ")
        if verificarRutaDirecta(grafo, ciudadOrigen, ciudadDestino, ciudades):
            print("¡Hay ruta directa!")
            input("")
        else:
            print("No hay ruta directa.")
    elif opcion == "2":
        break
    else:
        print("Opción no válida. Intente de nuevo.")