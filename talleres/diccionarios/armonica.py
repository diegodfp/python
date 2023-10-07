def calcularArmonica(numero):
    suma=0
    lista=[]
    lista.append(1)
    signo=-1
    for i in range(1,numero+1):
        suma=suma+(1/i)
        lista.append(str(signo*(1/i+1)))
    return suma,lista
def validarEntero():
    while True:
        try:
            numero=int(input("ingrese un numero entero: "))
            if numero<0:
                print("el numero debe ser positivo")
                continue
            return numero
        except ValueError:
            print("error al ingresar el numero")
#main program

numero=validarEntero()
suma,lista=calcularArmonica(numero)
print(f"la suma de la serie es: {suma}")
print(f"la lista de la serie es: {lista}")
