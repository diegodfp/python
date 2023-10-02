import math
#nota = float(input(" ingrese la nota del estudiante  \n"))

#notaFinal= (nota*0.8)+1

#print(" su nota final es: {:.3f}".format(notaFinal))

# valorHora=20000
# horasTrabajadas = int(input(" por favor ingrese la cantidad de horas que trabajas por el empleado\n"))

# sueldoBruto = valorHora * horasTrabajadas
# valorEps= (sueldoBruto*4)/100
# valorPension= (sueldoBruto*4)/100
# sueldoNeto=(sueldoBruto - (valorEps+valorPension))


# print ("tu sueldo bruto es  $ {:,}".format(sueldoBruto))
# print(" tu sueldo neto es $ {:,}".format(sueldoNeto))
# print("tu descuento por pension fue: $ {:,.2f}".format(valorPension))
# print("tu descuento por eps fue: $ {:,.2f}".format(valorEps))
    

# segundos = int(input(" escribe la cantidad de segundos que quieres convertir\n"))

# hora = segundos//3600
# minutos= (segundos-hora*3600)//60
# segundos2 = (segundos-hora*3600-minutos*60)
# print("la cantidad de horas que tienen ", segundos, " es:", hora," horas , la cantidad de minutos es : ", minutos, " y los segundos es", segundos2)


numero = int((input(" ingrese el numero que necesita contar los digitos \n")))
nDigitos = math.floor(math.log10(numero))+1
print(" input ", numero,"\n")
print(" output  ", nDigitos,"\n")
