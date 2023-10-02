while True:
    try:
        num=int(input("ingrese un numero"))
        break
    except ValueError:
        print(" numero entero no valido")
while True:
    try:
        num2=int(input("ingrese otro numero"))
        break
    except ValueError:
        print(" numero entero no valido")
try:
    suma = num + num2
    print(" la suma es : ", suma)
except Exception as e:
    print("error al intentar sumar.\n"+e)