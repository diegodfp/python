from random import *

def generarAleatorio():
    return randint(1, 1000)
def listarJugadores(jugadores):
    for nombre, vidas in jugadores.items():
        print(f"El jugador {nombre} tuvo {vidas} vidas")


def juego(jugadores):
    
    nombre = input("Ingrese su nombre")
    aleatorio = generarAleatorio()
    vidas=10
    print("Adivina el numero entre 1 y 1000")
    print(f"Tienes {vidas} vidas")
    num = int(input("Introduce un numero: "))
    while vidas > 1:
        if num != aleatorio:
            if num > aleatorio:
                print("El numero es menor")    
            else:
                print("El numero es mayor")
            print(aleatorio)
            vidas  -= 1
            print(f"le quedan:  {vidas} vidas") 
            print("\n")
            num = int(input("Introduce un numero: "))
        else:
            print("has acertado")
            jugadores[nombre]= vidas
            listarJugadores(jugadores)
            break
    if vidas  == 1 :
        print("has perdido, te quedaste sin vidas")
        print(f"el numero era: {aleatorio}")
    

###### MAIN PROGRAM ####
jugadores = {}
while True:
    juego(jugadores)
    print("----------------------------------------------------------")
    opcion = input("Quieres volver a jugar? (si/no)")
    if opcion.lower() == "no":
        break
