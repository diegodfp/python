# funcion range ([ini],fin,[inc])

print(list(range(5)))#-> 0,1,2,3,4
print(list(range(18)))#-> 0,1,2,3,4...18

print(list(range(15, -3,-1))) #15 ,14----.-2

for i in range(6):
    print("*", end="")
print("")
for i in range(3):
    print("*    *")
for i in range(6):
    print("*", end="")

# el usuario dice el tamaño de la piramide

tamaño = int(input(" tamaño de la piramide"))

for i in range(1,tamaño+1):
    
    print("*"*i)

#calcular las notas de un curso y dar un promedio

cant = int(input(" cantidad de notas:"))
notaAcumulada = 0
for i in range(1,cant+1):
    nota =  float(input("ingrese la nota"))
    notaAcumulada = notaAcumulada + nota
prom = notaAcumulada/cant
print(" su nota promedio es:", prom)

# factorial de un numero
# factorial de 5 = 1*2*3*4*5 = 120

num = int(input("ingrese el numero del cual quiere saber el factorial"))
factorial=1
for i in range(1,num+1):
    factorial *= i 
print("el factorial es  {:,}".format(factorial))

