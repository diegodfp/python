import json
def cargarRuta(ruta):    
    dicc = {}
    try:
        with open(ruta, "r") as archivo:
            dicc = json.load(archivo)
        archivo.close()
        return dicc
    except:
        with open(ruta, "w") as archivo:
            return dicc 
    

ruta = "/home/spukN01-019/Documents/Diego/python/matrices/puntajes.json"


dicc = cargarRuta(ruta)
def imprimirTabla(dicc):
    print("+------+--------------+-------------+------------+")  # Línea superior de la tabla
    print("| #    | Nombre       | Movimientos | Tiempo     |")  # Encabezados de columna
    print("+------+--------------+-------------+------------+")  # Línea divisoria

    for i, registro in enumerate(dicc):
        numero = i + 1
        nombre = registro["nombre"]
        movimientos = registro["movimientos"]
        tiempo = registro["tiempo"]

        # Formatear los valores en columnas usando f-strings
        print(f"| {numero:<4} | {nombre:<12} | {movimientos:<11} | {tiempo:.3f}      |")

    print("+------+--------------+-------------+------------+"  )# Línea inferior de la tabla

imprimirTabla(dicc)