import json
import time

def cargarRuta(ruta):
    try:
        with open(ruta, "r") as archivo:
            listadeRegistros = json.load(archivo)
        return listadeRegistros
    except FileNotFoundError:
        return []
def ordenarGanadores(registros):
    registrosOrdenados = sorted(registros, key=lambda x: (x["movimientos"], x["tiempo"]))
    return registrosOrdenados

def registrarGanador(nombreGanador, tiempoGanador, movimientos, ruta, registros):
    nuevoRegistro = {
        "nombre": nombreGanador,
        "tiempo": tiempoGanador,
        "movimientos": movimientos
    }

    registros.append(nuevoRegistro)
    escribirEnDisco(ruta, registros)
    registrosOrdenados  = ordenarGanadores(registros)
    escribirEnDisco(ruta,registrosOrdenados)
def escribirEnDisco(ruta, registros):
    with open(ruta, "w") as archivo:
        json.dump(registros, archivo)


def menu():
    print("\n")
    print(" TIC-TOC ".center(100,"="))
    print(" MENU ".center(99,"*"))
    print("1 - NUEVO JUEGO".center(100))
    print("2 - TABLA DE PUNTUACIONES".center(100))
    print("3 - SALIR".center(100))
    print("\n")
def crearMatrices():    
    m = []
    for i in range(3):
        fila = [0] * 3
        m.append(fila)
    return m 
def printMatriz(mat):
    
    for f in range(len(mat)):
        print("+------+------+------+")
        print("|      |      |      |")  
        for c in range(len(mat[f])):
            print("| ",mat[f][c], end="   ")
        print("|")
        print("|      |      |      |")
    print("+------+------+------+")

def llenarMatriz(mat): ### llenado por filas
    contador = 1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c]= contador 
            contador += 1
        print("")
def validacion(msg):
    while True:
        try:
            numero = int(input(msg))
            if (numero >= 1 and numero <= 3 ):
                return numero
            else:
                print("recuerde que el valor debe estar entre 1 y 3")
        except ValueError:
            print("-" * 50)
            print("Solo se permiten numeros enteros")
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"{e}")
            print("-" * 50)
def validacionFicha(msg):
    while True:
        try:
            numero = int(input(msg))
            if numero == 1 or numero == 2:
                return numero
            else:
                ("Recuerda que la opcionde debe ser 1 o 2")
        except ValueError:
            print("-" * 50)
            print("Solo se permiten numeros enteros")
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"{e}")
            print("-" * 50)
def validacionPosicion(msg,disponibles):
    while True:
        try:
            numero = int(input(msg))
            if numero in disponibles:
                disponibles.discard(numero)
                return numero, disponibles
            else:
                print ("El numero no se encuentra disponible, intenta con otro")
                continue
        except ValueError:
            print("-" * 50)
            print("Solo se permiten numeros enteros")
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"{e}")
            print("-" * 50)

# def modificarMatrizX(posicion,matriz):
#     if posicion == 1:
#         matriz[0][0] = 'X'
#     elif posicion == 2:
#         matriz[0][1] = 'X'
#     elif posicion == 3:
#         matriz[0][2] = 'X'
#     elif posicion == 4:
#         matriz[1][0] = 'X'
#     elif posicion == 5:
#         matriz[1][1] = 'X'
#     elif posicion == 6:
#         matriz[1][2] = 'X'
#     elif posicion == 7:
#         matriz[2][0] = 'X'
#     elif posicion == 8:
#         matriz[2][1] = 'X'
#     elif posicion == 9:
#         matriz[2][2] = 'X'
# def modificarMatrizY(posicion,matriz):
#     if posicion == 1:
#         matriz[0][0] = 'O'
#     elif posicion == 2:
#         matriz[0][1] = 'O'
#     elif posicion == 3:
#         matriz[0][2] = 'O'
#     elif posicion == 4:
#         matriz[1][0] = 'O'
#     elif posicion == 5:
#         matriz[1][1] = 'O'
#     elif posicion == 6:
#         matriz[1][2] = 'O'
#     elif posicion == 7:
#         matriz[2][0] = 'O'
#     elif posicion == 8:
#         matriz[2][1] = 'O'
#     elif posicion == 9:
        # matriz[2][2] = 'O'
def modificarMatriz(jugador, posicion, matriz):
    marca = '\x1b[1;31mX\x1b[0m' if jugador == 1 else '\x1b[1;34mO\x1b[0m'
    fila = (posicion - 1) // 3
    columna = (posicion - 1) % 3
    matriz[fila][columna] = marca

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

def quienPrimero(jugador1,jugador2):
    print("*** hora de escoger cual jugador iniciara primero:***".center(50))
    ficha = validacionFicha(f"presione  1 si quiere que el jugador: {jugador1} inicie primero o 2 si quiere que inicie de primero el jugador {jugador2}")
    if ficha == 1:
        return jugador1, jugador2
    else:
        return jugador2, jugador1
def verificarGanador(matriz):
    # Verificar filas y columnas
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] :
            return True  # Una fila completa
        if matriz[0][i] == matriz[1][i] == matriz[2][i] :
            return True  # Una columna completa
    
    # Verificar diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] :
        return True  # Diagonal de arriba a la izquierda a abajo a la derecha
    if matriz[0][2] == matriz[1][1] == matriz[2][0] :
        return True  # Diagonal de arriba a la derecha a abajo a la izquierda
    
    return False  # No hay ganador todaví
def jugar(fichaX,FichaO,matriz):
    disponibles = {1,2,3,4,5,6,7,8,9}
    cJugadorX = 0
    cJugadorY = 0
    tiempoTotalX = 0
    tiempoTotalY = 0
    printMatriz(matriz)
    while True:
        inicioTiempoX = time.time()   
        posicionX,disponibles = validacionPosicion(f'|\x1b[1;31m{fichaX}\x1b[0m  Por favor, escoga una casilla para tu ficha X ',disponibles)
        finTiempoX = time.time()
        tiempoX = finTiempoX - inicioTiempoX
        tiempoTotalX += tiempoX
        cJugadorX +=1
        modificarMatriz(1,posicionX,matriz)
        printMatriz(matriz)
        if verificarGanador(matriz) != True:
            if disponibles:
                print(f" Recuerda, solo se encuentran disponibles los numero {disponibles}")
                inicioTiempoY = time.time()  
                posicionY,disponibles = validacionPosicion(f'\x1b[1;34m{FichaO}\x1b[0m Por favor, escoga una casilla para tu ficha O ',disponibles)
                finTiempoY = time.time()
                tiempoY = finTiempoY - inicioTiempoY
                tiempoTotalY += tiempoY
                modificarMatriz(2,posicionY,matriz)
                cJugadorY += 1
                printMatriz(matriz)
                if verificarGanador(matriz) != True:
                    print(f" Recuerda, solo se encuentran disponibles los numero {disponibles}")
                    
                else:
                    print(f" 🎉🎉🎉 felicitaciones  \x1b[1;34m{FichaO}\x1b[0m has ganado!, usaste \x1b[1;34m{cJugadorY}\x1b[0m  movimientos y un tiempo de \x1b[1;34m{tiempoTotalY:.3f}\x1b[0m ".center(100))
                    input("")
                    return FichaO, tiempoTotalX, cJugadorY
            else:
                break
        else:
            print("\n")
            print(f" 🎉🎉🎉felicitaciones  \x1b[1;31m{fichaX}\x1b[0m has ganado!, usaste \x1b[1;31m{cJugadorX}\x1b[0m movimientos y un tiempo de \x1b[1;31m{tiempoTotalX:.3f} \x1b[0m ".center(100))
            input("")
            return fichaX, tiempoTotalX, cJugadorX
        
    input(" hubo un empate , presiona cualquier tecla para volver al menu")
def imprimirTabla(lista):
    print("+-------------TABLA DE POSICIONES-----------------+")
    print("+------+--------------+-------------+-------------+")  
    print("| #    | Nombre       | Movimientos | Tiempo      |")  
    print("+------+--------------+-------------+-------------+")  
    contador = 0
    for i, registro in enumerate(lista):
        numero = i + 1
        nombre = registro["nombre"]
        movimientos = registro["movimientos"]
        tiempo = registro["tiempo"]
        print(f"| {numero:<4} | {nombre:<12} | {movimientos:<11} | {tiempo:<5.2f}       |")
        print("+------+--------------+-------------+-------------+")
        contador += 1
        if contador % 3 == 0:
            opcion = input("Presiona 'q' para salir, o cualquier otra tecla si quieres ver mas registros")
            if opcion.lower() == "q":
                break
def escoger(opcion,matriz,ruta,registros):
    print("\n")
    if opcion == 1:
        print("INICIAR JUEGO".center(100,"="))
        jugador1 = leerTexto("ingrese el nombre del jugador Numero 1:  ")
        jugador2 = leerTexto("ingrese el nombre del jugador Numero 2:  ")
        fichaX,FichaO = quienPrimero(jugador1,jugador2)
        try:
            nombreGanador,tiempoGanador,movimientos = jugar(fichaX,FichaO,matriz)
            registrarGanador(nombreGanador,tiempoGanador,movimientos,ruta,registros)
        except:
            pass
    elif opcion ==2 :
        imprimirTabla(registros)
        input("presione cualquier tecla para volver al menu de inicio")
        pass
    elif opcion == 3:
        print("¡Hasta luego!".center(100,"="))
        salir = leerTexto("Presione cualquier tecla para salir o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            exit()




ruta = "matrices\\puntajes.json"

while True:
    registros = cargarRuta(ruta)
    matriz = crearMatrices()
    llenarMatriz(matriz)
    menu()
    escoger(validacion("Opcion 1 a 3: "),matriz,ruta,registros)
    print("\n")
    

