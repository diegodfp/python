fd = open("/home/spukN01-019/Documents/Diego/python/archivos/datos-empleados.dat","r")

listaDatos = []

##### opcion 1 #####
# for linea in fd:
#     linea.strip()
#     listaDatos.append(linea.split(","))

# fd.close()
# for i in range(1,len(listaDatos)):
#     print("iD:", listaDatos[i][0])
#     print("nombre:", listaDatos[i][1])
#     print("edad:", listaDatos[i][2])
#     print("sexo:", listaDatos[i][3])
#     print("telefono:", listaDatos[i][4])
#     print("--"*30)
istEmpleado = []
for empleado in fd:
    if not empleado.startswith("ID"):
        listEmpleado = empleado.split(",")
        print(f"ID = {listEmpleado[0]}")
        print(f"NOMBRE = {listEmpleado[1]}")
        print(f"EDAD = {listEmpleado[2]}")
        print(f"SEXO = {listEmpleado[3]}")
        print(f"TELEFONO = {listEmpleado[4]}")
        print("-------------------------")

fd.close()