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
def leerNombre(msj):
    while True:
        try:
            nombre = input(msj)
            nombre = nombre.strip()
            if len(nombre) == 0 or not nombre.isalnum():
                print(" nombre invalido")
                continue
            return nombre    
        except Exception as e:
            print(" Error al ingresar el nombre",e)

def leerEstrato(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1 or n > 5:
                print("Valor invalido. Debe ser un numero del 1 al 5")
                continue
            return n
        except ValueError:
            print("error al ingresar el numero")
def calcularTarifaBasica(estrato):
    if estrato ==1:
        return 10000
    elif estrato ==2:
        return 15000
    elif estrato ==3:
        return 20000
    elif estrato ==4:
        return 25000
    elif estrato ==5:
        return 30000



def calcularValorImpulso(impulsos):
    return 100* impulsos

n = leerInt("ingrese la cantidad de usuarios: ")
valTotal = 0
for i in range(1,n+1):
    print("\n datos del usario #")
    nombre = leerNombre(" nombre? \n")
    estrato = leerEstrato(" estrato? \n")
    impulsos = leerInt("impulsos=\n")
    valtbas = calcularTarifaBasica(estrato)
    valImpu = calcularValorImpulso(impulsos)

    print("=" * 30)

    print (" nombre: ", nombre)
    print (" la tarifa basica es ", valtbas)
    print (" valor del impulso ", valImpu)
    print (" valor Total a pagar ",valtbas + valImpu)

    valTotal += valtbas + valImpu

print("\n","**"*30)
print("el valor total a pagar es: ",valTotal )