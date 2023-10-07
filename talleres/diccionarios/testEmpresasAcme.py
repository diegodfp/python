def menu():
    print("\n","="*30)
    print("*** PRODUCTOS ACME ***")
    print("="*30)
    print("MENU")
    print("1- Agregar Producto")
    print("2- Modificar Producto")
    print("3- Eliminar Producto")
    print("4- Listar Varios Productos")
    print("5- Estrategia de Mercadeo")
    print("6- Salir")
    print("\n")
lista = []
def listar(dicc,lista):
    
    if dicc:
        lista.clear()
        for l in dicc.keys():
            
            lista.append(l)
        total_productos = len(dicc)
        pagina = 1
        contador = 0
        continuar = True
        

        while continuar:
            print(f"\n--- Página {pagina} ---")
            for i in range(contador, contador + 5):
                if i < total_productos:
                    producto = lista[i]
                    nombre = dicc[producto]["nombre"] 
                    precio = dicc[producto]["precio"]  
                    valor = dicc[producto]["cantidad"] 
                    print(f"ID: {producto}")
                    print(f"Nombre: {nombre}")
                    print(f"Horas trabajadas: {precio}")
                    print(f"Valor de la hora: {valor}")
                    print("-" * 50)
                    
                else:
                    break

            contador += 5
            opcion = input("Presione 'Enter' para ver más empleados o ingrese 'M' para volver al menú: ")
            if opcion.lower() == "m":
                break

            if contador >= total_productos:
                opcion = input("No hay mas empleadospara mostrar. ")
                break


            pagina += 1
    else:
        print("No se han ingresado empleados.")

def leerEntero(msg):
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
def mostrar(diccProducto):
    print(diccProducto)
    input("")   
def leerTexto(msg):
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
def agregar(diccProducto):

    idProducto = leerEntero("\nIngrese la id del producto: ")
    nombre = leerTexto("Ingrese el nombre del producto: ")
    precioProducto = leerEntero("Ingrese el precio del producto: ")
    cantidad = leerEntero("Ingrese la cantidad del producto: ")
    diccProducto[idProducto] = {}
    diccProducto[idProducto]["nombre"] = nombre
    diccProducto[idProducto]["precio"] = precioProducto
    diccProducto[idProducto]["cantidad"] = cantidad

    print("-" * 50)
    print("El producto fue ingresado con exito")
    print("-" * 50)
def escoger(opcion,diccProducto,lista):

    if opcion == 1:
        print("AGREGAR PRODUCTO".center(50,"-"))
        agregar(diccProductos)
    elif opcion == 2:
        print("MODIFICAR PRODUCTO".center(50,"-"))
        modificar(diccProducto)
        mostrar(diccProducto)
    elif opcion == 3:
        print("ELIMINAR PRODUCTO".center(50,"-"))
        eliminar(diccProducto)
    elif opcion == 4:
        print("MOSTRAR RODUCTOS".center(50,"-"))
        mostrar(diccProducto)
    elif opcion == 5:
        print("ESTRATEGIA DE MERCADEO".center(50,"-"))
        listar(diccProducto,lista)
    elif opcion == 6:
        print("¡Hasta luego!".center(50,"-"))
        salir = leerTexto("Presione cualquier tecla para volver al menú o ingrese 'S' para salir: ")
        if salir.lower() == "s":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")
        input("Presione cualquier tecla para continuar")
def modificar(diccProducto):
    if diccProducto: ## verifica que el diccionario tenga elementos
        idProducto = leerEntero("\nIngrese el ID del producto a modificar: ")
        encontrado = False
        for producto in diccProducto.keys():
            if producto == idProducto:
                encontrado = True
                
                nombre = leerTexto("Ingrese el nuevo nombre del producto: ")
                horas = leerEntero("Ingrese el nuevo valor del producto: ")
                valor = leerEntero("Ingrese la nueva cantidad de unidades disponibles: ")

                diccProducto[idProducto]["nombre"] = nombre
                diccProducto[idProducto]["precio"] = horas
                diccProducto[idProducto]["cantidad"] = valor

                print("-" * 50)
                print("producto modificado con éxito.")
                print("-" * 50)
                input("Presione cualquier tecla para continuar")
                break
    else:
            print("-" * 50)
            print("No hay productos Registrados, no se puede modificar.")
            print("-" * 50)
            input("Presione cualquier tecla para continuar")


def eliminar(diccProducto):
    if diccProducto:
        idProducto = leerEntero("\nIngrese el ID del empleado a eliminar: ")
        encontrado = False
        for producto in diccProducto.keys():
            if producto == idProducto:
                encontrado = True
                diccProducto.pop(producto)
                print("Empleado eliminado con éxito.")
                break
        if not encontrado:
            print("No se encontró ningún empleado con el ID ingresado.")
    else:
        print("No se han ingresado productos, no hay nada que eliminar.")




###### MAIN PROGRAM ######
diccProductos = {}
lista = []
while True:
    input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
    menu()
    escoger(int(input("Opcion 1 a 6: ")),diccProductos,lista)
    print("\n")