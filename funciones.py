def longString(str):
    try:
        long = 0
        while str[long] != None:
            long +=1
    except:
        pass
    return long
def prepararCafe (insumo1, insumo2):
    salida=""
    if insumo1.lower() =="cafe" and insumo2.lower() =="agua":
        salida = "tinto"
    else:
        salida ="daño la cafetera"
    return salida


taza = prepararCafe("leche","agua")
print(taza)
print(len(taza))
print(longString(taza))
