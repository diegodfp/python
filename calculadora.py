

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1,num2):
    return num1- num2

def multipliacion(num1,num2):
    return num1 * num2

def division (num1,num2):
    try:
        resultado = num1/num2
    except ZeroDivisionError:
        resultado = None
    return resultado
def menu():
    while True:
        try:
            print("*** MENU CALCULADORA ***")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            op = int(input(">>>> Opcion (1-5)?"))
            if op < 1 or op > 5:
                print(" opcion no valida. Escoja del 1 al 5")
                input(" presione cualquier tecla para continuar")
                continue
            return op
        except ValueError:
            print("opcion no valida, escoja del 1 al 5")
            input(" presione cualquier tecla para continuar")
        return op
def leerNum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("error. numero invalido")
            input("presione cualquier tecla para continuar")

#main PROGRAM
while True:
    opcion = menu()

    if opcion == 1:
        print("\n\n1. Sumar")
        num1 = leerNum("ingrese el primer numero:  ")
        num2 = leerNum("ingrese el segundo numero:  ")
        print(f" el resultado de la suma es\n:{suma(num1,num2):.3f} ")
    elif opcion == 2:
        print("\n\n1. Restar")
        num1 = leerNum("ingrese el primer numero:  ")
        num2 = leerNum("ingrese el segundo numero:  ")
        print(f" el resultado de la resta es\n:{resta(num1,num2):.3f} ")
    elif opcion == 3:
        num1 = leerNum("ingrese el primer numero:  ")
        num2 = leerNum("ingrese el segundo numero:  ")
        print("\n\n1. Multiplicacion")
        print(f" el resultado de la multiplicacion es\n:{multipliacion(num1,num2):.3f} ")
    elif opcion ==4:
        num1 = leerNum("ingrese el primer numero:  ")
        num2 = leerNum("ingrese el segundo numero:  ")
        res =division(num1,num2)
        if res != None:
            print(f" el resultado de la division es: {res:.3f}")
        else:
            print("division entre 0 es indeterminada")
    elif opcion == 5:
        print("\n\n Gracias por usar la calculadora\n")
        print("Adios")
        input("presione cualquier tecla para salir...")
        break
    input("presione cualquier tecla para volver al menu...")
