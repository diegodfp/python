def leerRuta():
    while True:
        try:
            nom = input("Ingrese el nombre del archivo:  ")
            nom = nom.strip()
            if len(nom) == 0:
                print("Nombre del archivo inválido, no puede ir vacio")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre del archivo.", e)
def calcularPromedio(lstspam,c):
    prom = sum(lstspam)/c
    return prom







##### main program ####
while True:
    ruta = leerRuta()
    try:
        fd = open("/home/spukN01-019/Documents/Diego/python/archivos/"+ruta,"r")
        break
    except:
        print("Error. archivo no encontrado, asegurese que lo digito bien \n")
        continue

lstspam= []
c = 0
for linea in fd:
    if linea.startswith("X-DSPAM-Confidence:"):
        c += 1
        spam = float(linea.split()[1])
        lstspam.append(spam)
fd.close()
promedio =  calcularPromedio(lstspam,c)
print(f" el promedio de spam es: {promedio} ")

    # print("el promedio de spam es ", sum(lstspam)/c)


