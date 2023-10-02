
# sueldo = 1_000_000
# sueldoMin = 1_160_000

# if sueldo < sueldoMin:
#     auxTrans = 140_000
#     print("el auxilio de transporte es igual a {:,}".format(auxTrans))
# else:
#     auxTrans= 0
#     print("el auxilio de transporte es igual a {:,}".format(auxTrans),"ud tiene mucha plata")


# nombre = input("ingrese nombre")
# nota=int(input(" ingrese la nota de 0 a 100"))

# if nota >= 0 and nota <=59 :
#     notaCualitativa = "D"
#     print(nombre," has sacado una nota cuantativa de: ", nota, " y su nota cualitativa es ",notaCualitativa)
# elif nota >= 60 and nota <=79:
#     notaCualitativa = "C"
#     print(nombre," has sacado una nota cuantativa de: ", nota, " y su nota cualitativa es ",notaCualitativa)
# elif nota >= 80 and nota <=89:
#     notaCualitativa = "B"
#     print(nombre," has sacado una nota cuantativa de: ", nota, " y su nota cualitativa es ",notaCualitativa)
# elif nota >= 90 and nota <=100:
#     notaCualitativa = "A"
#     print(nombre," has sacado una nota cuantativa de: ", nota, " y su nota cualitativa es ",notaCualitativa)
# else:
#     notaCualitativa=""
#     print(" has ingresado un dato incorrecto, corrigelo por favor")


numero1 = int(input(" ingrese el primer numero "))
numero2 = int(input(" ingrese el segundo numero "))
numero3 = int(input(" ingrese el tercer numero "))


if numero1>numero2 and numero1>numero3:
    mayor= numero1
    if numero2>numero1 and numero2>numero3:
        mayor = numero
    if numero1<numero2 and numero1<numero2:
        menor=numero1
elif numero1<numero2 and numero2<numero3:
    medio = numero2
elif numero2>numero1 and numero3<numero2:
    mayor=numero2
elif numero2<numero1 and numero2<numero3:
    menor=numero2
elif numero3>numero1 and numero3<numero2:
    medio=numero3
elif numero3>numero1 and numero3>numero2:
    mayor=numero3
elif numero3<numero1 and numero3<numero2:
    menor = numero3
print( " el numero mayor es ", mayor," el numero medio es ", medio, " el numero menor es", menor )                                    

                                
