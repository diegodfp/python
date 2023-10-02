bandera = 1
valorVentasMes =0
valorComisionMes =0
while bandera == 1:
   while True:
        try:
            cc = (input(" ingrese su documento"))
            if cc.isalpha == False or len(cc) == 0:
                print("el documento solo admite caracteres alfanumericos y no puede estar vacio")
                continue
            break
        except ValueError:
            print(" Error.")
   if cc != -1:
       while True:
           try:
               nombre = input(" ingrese su nombre")
               if nombre.isalnum() == False or len(nombre) == 0:
                   print(" el nombre no puede ir vacio o tener simbolos especiales")
                   continue
               break
           except ValueError:
               print("Error. Valor invalido")
       while True:
           try:
               tipoVendedor = int(input(" ingrese que tipo de vendedor es [1. para puerta puerta 2.Telemercadeo 3. Ejecutivo Ventas]"))
               if tipoVendedor < 1 or tipoVendedor>3:
                   print(" Recuerde que el numero debe estar entre 1 y 3")
                   continue
               break
           except ValueError:
               print("Error. Valor invalido")
       while True:
           try:
               valorVentas = float(input(" ingrese el valor de las ventas que realizo este mes"))
               if valorVentas < 0:
                   print(" el valor debe ser positivo")
                   continue
              
               
               valorVentasMes = valorVentasMes + valorVentas
               break
           except ValueError:
               print (" Error. el valor debe ser un numero")

       if tipoVendedor== 1:
           comision = valorVentas * 0.2
       if tipoVendedor== 2:
           comision = valorVentas * 0.15
       if tipoVendedor== 3:
           comision = valorVentas * 0.25
       valorComisionMes = valorComisionMes + comision
       print (" el valor que ha comisionado, ", nombre, f" es de $ {comision:,} ")
   else:
       bandera = 0  
print("\n","="*30)
print ( f" el valor total de comisiones que se entrego a los vendedores  en este mes fue de $ {valorComisionMes}\n")
print (f"y el valor total de ventas de este mes fue de{valorVentasMes:,}")