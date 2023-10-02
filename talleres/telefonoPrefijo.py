num = input(" ingrese el numero")

if num.startswith("+")and num.count("-") == 2:
    partes = num.split("-")
    print ("el telefono es:", partes[1])
else:
    print(" Error. el numero no cumple con el formato")

cadena = input("ingrese la palabra para saber si es palindroma\n")


# if cadena == cadena[::-1]:
#     print(" si es")
# else: 
#     print("no es ")
print(len(cadena))
bandera = 1
for i in range (len(cadena)):
    if cadena[i] == cadena [i-len(cadena)]:
        bandera = 1
    else:
        bandera = 0
if bandera == 1:
    print("si es palindroma")       
else:
    print("no es")