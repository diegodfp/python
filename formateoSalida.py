#formateo de enteros, para que los imprima separados por ","
#con format

sueldo = 5600000

print("sueldo:  ${:,}".format(sueldo))

intereses = 256666.5555

print("intereses:  ${:,.3f}".format(intereses))

# f-string
print(f"sueldo: ${sueldo:,}")
print(f"intereses: ${intereses:,.3f}")