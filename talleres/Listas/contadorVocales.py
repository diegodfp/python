letras = []
while True:
    letra = input("ingrese una letra:  ")
    if not letra.isalpha():
        print("error esa no es una letra")
        input()
        continue
    letras.append(letra)

    op = input("\n desea continuar s o n")
    if op.lower() != "s":
        break

print("\n ", " == "*30)
vocales = ["a","e","i","o","u"]
canVocales = [0]*5
# recorrer la lista de los elementos

for l in letras:
    if l.lower() in vocales: ##  el in se utiliza para saber si se encuentra en la lista 
        p= vocales.index(l.lower())
        canVocales[p] += 1

# recorrer la lista por posicion

for i in range(len(vocales)):
    print(vocales[i], "   = ", canVocales[i])