def calcularNota(n1,n2,n3):
    dicNota = {}
    nota = (n1*0.3)+(n2*0.3)+(n3*0.4)
    if (nota)>=3.0:
        dicNota["mensaje"] = "felicidades aprobo" 
        dicNota["nota"] = nota
    else:
        dicNota["mensaje"] = "lo siento reprobo" 
        dicNota["nota"] = nota
    return dicNota


dicAlumnos = {}
bandera = 1
while bandera == 1:
    dicAlumnos["codigo"] = int(input("codigo: "))
    if dicAlumnos["codigo"] != 999:    
        dicAlumnos["nombre"] = input("Nombre: ")
        dicAlumnos["nota1"] = float(input("nota 1: (0 al 5)"))
        dicAlumnos["nota2"] = float(input("nota 2: (0 al 5)"))
        dicAlumnos["nota3"] = float(input("nota 3: (0 al 5)"))
        print(calcularNota(dicAlumnos["nota1"],dicAlumnos["nota2"],dicAlumnos["nota3"]))
    else:
        bandera =0