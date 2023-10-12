fd = open("/home/spukN01-019/Documents/Diego/python/archivos/mbox-short.txt","r")

cl = 0
cp=0
for linea in fd:
    linea.strip()
    cp += len(linea.split(" "))
    # for lin in linea.split(" "):
    #     if lin.isalnum():
    #         cp +=1
    cl+=1
fd.close ###### Apenas cerrar el archivo cuando no lo necesite.

print("Cantidad de lineas:  ", cl  )   
print("cantidad de palabras ", cp)