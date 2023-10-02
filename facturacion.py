n = int(input("cuantos usuarios"))
valorTotalAgua = 0
for i in range(1,n+1):
    print  ( f"\n datos del unario # {i} ")
    cod = input("codigo?\n")
    nom = input("nombre \n")
    est = input(" estado [v: vigente o s: suspendido]?")
    estra = int(input("estrato [1 al 6]?"))
    con = float(input("consumo agua al mes [cm3]?"))
    if est == "V" or est=="v":
        if estra ==1:
            tarifaBasica=10000
        elif estra ==2:
            tarifaBasica=20000
        elif estra ==3:
            tarifaBasica=30000
        elif estra ==4:
            tarifaBasica=45000
        elif estra ==5:
            tarifaBasica = 60000 
        elif estra ==6:
            tarifaBasica = 70000
        else:
            tarifaBasica=0
        # calcular el valor del consumo
        valorConsumo = con * 200 
        # calcular el valor a pagar
        valPagar = tarifaBasica + valorConsumo
        valorTotalAgua = valorTotalAgua + valPagar
        # imprimir el informe del usuario
        print ("\n","="*40)
        print ("\tnombre: ", nom)
        print (f"\t valor tarifa basica: ${tarifaBasica:,}")
        print (f"\t valor consumo ${valorConsumo:,.0f}")
        print(f"\t valor a pagar ${valPagar:,.0f}")
print("\n","="*40)
print(f"\t el valor total que todos los usarios pagarian es ${valorTotalAgua:,.0f}")
    