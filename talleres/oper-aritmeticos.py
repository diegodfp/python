tuition = float(input(" ingrese el valor de la matricula \n"))
c = 0
tuition2= tuition*2
while tuition<= tuition2:
   c = c+1
   tuition = tuition + ( tuition*0.07)
   
print(" dentro de ", c ,"  años el valor de la matricula costara el doble")



tuition1 = float(input(" ingrese el valor de la matricula \n"))
tuition3= tuition1*2
for i in range(100):
   if tuition1<= tuition3:
    tuition1 = tuition1 + ( tuition1*0.07)
   else:
     break
print(" dentro de ", i ,"  años el valor de la matricula costara el doble")