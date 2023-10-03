milista =  [] #lista vacia
milista2 = list() #lista vacia

nomCampers = ["Juan","Yulieth","Lorenzo","Manuel","David"]

print(nomCampers)        
nomCampers[1] = "julieth"
print(nomCampers[1])

### Slices ##
print(nomCampers[2:4]) ##la ultima posicion no se incluye
print(nomCampers[::-1]) # invertida 

nomCampers_Juan = ["daniela", "Maria", "Julliana", "Sandra","Carolina"]

print (nomCampers)
nomCampers += nomCampers_Juan
print(nomCampers)
nomCampers.append("Kevin")
print(nomCampers)  

nomCampers.extend(nomCampers_Juan)
print(nomCampers)

nomCampers.insert(1,"carlos")
print(nomCampers)


nomCampers.pop()
print(nomCampers)
nomCampers.pop(-3)
print(nomCampers)

nomCampers.remove("Sandra")
print(nomCampers)

nomCampers.sort()  ## ordena en orden alfabetico
print(nomCampers,"\n")

nomCampers.insert(2,"Daniel")
nomCampers.sort()
print(nomCampers)

nomCampers.sort(reverse=True)
print(nomCampers)
