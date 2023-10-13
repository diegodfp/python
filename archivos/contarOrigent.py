fd = open("/home/spukN01-019/Documents/Diego/python/archivos/mbox-short.txt","r")
fdCorreos = open("/home/spukN01-019/Documents/Diego/python/archivos/correosEnviados.txt","w")

#guardamos los correos en un conjunto para que no cuente los correos repetidos
lstEmails = []

for linea in fd:
    if linea.startswith("From:"):
        email = (linea.split()[1])
        if email not in lstEmails:
            lstEmails.append(email)
for i in range(len(lstEmails)-1,-1,-1): 
        msj = (f"{lstEmails[i]} enviado [ok]")
        print(msj)
        fdCorreos.write(msj+"\n")

fd.close()
fdCorreos.close()