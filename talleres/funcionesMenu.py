# Funciones


def factorial(n):
    dev = 1
    while True:
        if n < 2:
            return dev
        dev *= n
        n -= 1

def combinaciones (m,n):
    return factorial(m)/(factorial(n)*factorial(m-n))


def menu():
    while True:
        try:
            print("*** QUE DESEA HACER***")
            print("1. Hacer la combinatoria de un numero")
            print("2. conveertir texto a numero")
            print("3. Calcular el iva de una factura")
            print("4. Salir")
            op = int(input(">>> Escoga una Opción (1-4)? "))
            if op < 1 or op > 4:
                print("Opción no válida. Escoja de 1 a 4.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")

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

def leerFloat(msj):
    while True:
        try:
            n = float(input(msj))
            if n < 1:
                print("Valor invalido. Debe ser mayor a 0")
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
def eliminarLetras(texto):
    sinNumeros =""
    for e in texto:
        if e.isdigit() == True:
            sinNumeros = sinNumeros + e
        else:
            continue
    return sinNumeros

def calcularIva(n1,n2):
    precioFinal = n1 + (n1 * n2) / 100
    return precioFinal
####### main progra #####

while True:
    opcion = menu()
    if opcion == 1:
        print("\n\n1. COMBINATORIA")
        num1 = leerInt("Seleccione los k items  de la combinatoria")
        num2 = leerInt("Seleccione los n items  de la combinatoria")
        print(f"la combinatoria  del numero es: {combinaciones(num1,num2)}")
    elif opcion == 2:
        print("\n\n2. ELIMINAR letrS DE UN TEXTO")
        texto = leerTexto("Ingrese la cadena a la que le quiere eliminar los LETRAS")
        print(f" {eliminarLetras(texto)}")
    elif opcion == 3:
        num1 = leerFloat("indique  el valor del altirculo sin IVA  :")
        num2 = leerFloat("indique la cantidad de iva a aplicar}  :")
        print(f"El valor con iva es: {calcularIva(num1, num2):.1f}  pesos ")
    elif opcion == 4:
        print("\n\nGracias por usar nuestro programa")
        print("Adios")
        input("Presione cualquier tecla para salir ...")
        break
    input("Presione cualquier tecla para volver al MENU...")