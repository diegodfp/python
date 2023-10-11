
archivo = open("/home/spukN01-019/Documents/Diego/python/archivos/salas.txt","w")

# texto = archivo.read()

# print(texto)
# input("")

# archivo.seek(0)
# texto2 = archivo.readline()
# print(texto2)


# texto3 = archivo.readlines()
# print(texto3)

archivo.write("sputnik\n\t")
archivo.write("apolo\n")
archivo.writelines(["houston\n","artemis\n"])

archivo.close()