import json

fd = open("/home/spukN01-019/Documents/Diego/python/archivos/json/lista.json","r")

lst = []

lst = json.load(fd)

for e in lst:
    print(f"nombre:  {e['nombre']}")
    print(f"nombre:  {e['edad']}")
    print("-" * 30)
fd.close()