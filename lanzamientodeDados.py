#Contar cuantas veces sacaste 5, en un lanzamiento de dados:
import random

cae5 = 0 # variable tipo contador
for i in range (100):
    dado = random.randrange(1,7)
    if dado == 5:
        cae5 += 1
print ("de los 100 lanzamientos ", cae5, " cayeron en 5")

