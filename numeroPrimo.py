# break
# calcular si un numero es primo

numero = int(input(" indique el numero que quiere saber si es un numero primo\n"))
if numero <2:
    print("no es primo")
elif numero == 2:
    print("es primo")
else:
    esprimo = True #variables banderas
    for i in range(2,numero):
        if numero%i ==0:
            esprimo = False
            break
    if esprimo == True:
        print(" es primo")
    else:
        print("no es primo")

#continue
# salta una iteracion de un ciclo

for i in range (1,101):
    if i % 7 ==0:
        continue
    print(1, end =",")