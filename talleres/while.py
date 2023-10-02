num = int(input(" ingrese el numero que quiere saber si es para o impar"))
cPares = 0
cImpares = 0
while num != -1:
    if num % 2 == 0:
        print (" el numero es par")
        cPares += 1
    else:
        print("el numero es impar")
        cImpares += 1
    num = int(input(" ingrese el numero que quiere saber si es para o impar"))

print("\n", "=" *30)
print("cantidad d enumeros pares es ", cPares," y cantidad de numeros impares es ", cImpares)
