fd = open("/home/spukN01-019/Documents/Diego/python/archivos/mbox-short.txt","r")

def miFun(email):
    return len(email)
#guardamos los correos en un conjunto para que no cuente los correos repetidos
setEmail = set()
# for linea in fd:
#     if linea.startswith("From:"): ###  buscamos lineas que comiencen con from
#         #
#         # email= linea.split()[1]
#         # print(email)
#         setEmail.add(linea.split()[1]) ## añadimos al conjunto las palabras que vayan despues del From


# cl = (len(setEmail))
# print("cantidad de correo de origenes distintos: ",cl)

# for linea in fd:
#     if linea.startswith("To:"):
#         setEmail.add(linea.split()[1])
# for email in sorted(setEmail, reverse=False, key= miFun):
#     print(email, " enviado  [ok]")


for linea in fd:
    if linea.startswith("To:"):
        setEmail.add(linea.split()[1])
for email in setEmail:
    print(email, " enviado  [ok]")
fd.close()