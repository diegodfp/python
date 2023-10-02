while True:
    try:
        cat = int(input("ingrese una catagoria (1,2 o 3)"))
        if cat < 1 or cat >3 :
            print("categoria invalida. ingrese 1 o 2 o 3")
            continue
        break
    except ValueError:
        print("error.categoria invalida")