# validar el nombre del usario
while True:
    try:
        nombre = input(" ingrese el nombre del usuario")
        nombre = nombre.strip()
        if len(nombre) == 0 or  nombre.isalnum() ==False:
            print(" nombre invalido. vuelve a digitarlo")
            continue
        break
    except Exception as e:
        print("Error. Al ingresar el nombre. \n",e)
# validar el estrato
while True:
    try:
        estrato = int(input(" ingrese el estrato(1-5)"))
        if estrato < 1 or estrato>5:
            print(" el estrato no esta en el rango")
            continue
        break
    except ValueError:
        print("Error. Al ingresar el estrato")
if estrato == 1:
    tarifaBasica = 10000
elif estrato ==2:
    tarifaBasica = 15000
elif estrato ==3:
    tarifaBasica = 30000
elif estrato ==4:
    tarifaBasica = 50000
else:
    tarifaBasica = 65000

print ("\n", "=" *30)
print("nombre ", nombre)
print("tarifa basica: ", tarifaBasica)
