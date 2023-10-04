numeroEstudiantes = int(input(" total de estudiantes que estan suscritos al periodico ingles"))
listaingles = []
numeroEstudiantesFrances = int(input(" total de estudiantes que estan suscritos al periodico ingles"))
listaFrances = []
for i in range(numeroEstudiantes):
    listaingles.append(int(input("ingrese el codigo del estudiante ingles")))
for l in range(numeroEstudiantesFrances):
    listaFrances.append(int(input("ingrese el codigo del estudiante frances")))
print(listaingles)

conjuntoIngles= set(listaingles)
print(conjuntoIngles)

conjuntoFrances= set(listaFrances)
print(conjuntoFrances)

e=conjuntoIngles-conjuntoFrances
print(e)
print(len(e))

