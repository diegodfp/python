cadena = input(" ingrese una cadena solo que comprenda los caracteres de la [a,..z]")
contadorCaracteres  = 0
if cadena.isalpha  and cadena.islower : 
   for i in range(len(cadena)):
       if cadena.count(cadena[i])>=2:
           if cadena.find(cadena[i]) == (cadena.rfind(cadena[i])-1):
               print("si")
else:
   "error. Solo se admiten caracteres alfabeticos en minuscula"