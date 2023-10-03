# Ejercicio
# Hacer un programa que lea N estudiantes ( nombre y nota). y nos muestra el promedio de la clase, el 
# estudiante con mayor nota y el estudiante con menor nota.

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
def leerFloat(msj):
    while True:
        try:
            n = float(input(msj))
            if n < 0:
                print("nota invalida. Debe ser mayor o igual a 0")
                continue
            return n
        except ValueError:
            print("error al ingresar el numero")

# main program
n = leerInt("cuantos estudiantes son")
lstNombres=[]
lstNotas=[]
for i in range(1, n+1):
    
    lstNombres.append(leerTexto("nombre?"))
    lstNotas.append(leerFloat("cual es su nota"))

prom = sum(lstNotas)/n
print("\n ", "=="*30)
print(" el promedio del curso es:  ",prom)

# encontrar y mostrar el estudiante con mayor nota
notaMayor = max(lstNotas)
posEstMayor = lstNotas.index(notaMayor)
nomEstMayor = lstNombres[posEstMayor]
print( "\n el estudiante", nomEstMayor," tiene la mayor nota : ",notaMayor)

# encontrar y mostar el estudiante con menor nota:
notaMenor = min(lstNotas)
posEstMenor = lstNotas.index(notaMenor)
nomEstMenor = lstNombres[posEstMenor]
print( "\n el estudiante", nomEstMenor," tiene la mayor nota : ",notaMenor)