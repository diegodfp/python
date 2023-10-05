empleado = {"Nombre:":"Sergio Medina","cargo:":"programador","salario":4000000}
print(empleado["cargo:"])
print(empleado.get("cargo:"))
print(empleado.get("apellido","llave no existe"))

#### agregar una llave
empleado["sexo"] = "masculino"

print(empleado)

### modificar una llave
empleado["salario"] = 4500000

### Borrar una llave y su valor
# empleado = {}
# empleado.clear()
# del empleado

oficina = empleado.copy()
print(oficina)
oficina["salario"] = 5000000
print(oficina)
print(empleado)

##### items

print(empleado.items())

#### keys
print(empleado.keys())

### elimina la dupla pero imprime por ultima vez el valor de la key
print(empleado.pop("salario"))
print(empleado)
### setdefault ---> confirma si el valor a insertar existe o no
print(empleado.setdefault("Nombre","Carlos"))
print(empleado.setdefault("Ciudad","Bucaramanga"))
print(empleado)