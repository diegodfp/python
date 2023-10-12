fd = open("C:\\Users\\DIEGO\\Documents\\Python\\python\\archivos\\mbox-short.txt","r")
fdCorreos = open("C:\\Users\\DIEGO\\Documents\\Python\\python\\archivos\\correosEnviados.txt","w")

#guardamos los correos en un conjunto para que no cuente los correos repetidos
setEmail = set()

for linea in fd:
    if linea.startswith("To:"):
        email = (linea.split()[1])
        setEmail.add(email)
for email in setEmail:
    mensaje = f"{email} enviado [ok]"
    print (mensaje)
    fdCorreos.write(mensaje+"\n")
fd.close()
fdCorreos.close()