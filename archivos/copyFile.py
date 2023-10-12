fd = open("/home/spukN01-019/Documents/Diego/python/archivos/nombre.txt","r")

fd2 =  open("/home/spukN01-019/Documents/Diego/python/archivos/nombre-back.txt","w")


for linea in fd:
    fd2.write(linea)

fd.close()
fd2.close()

print("Proceso terminado")