import json

fd = open("/home/spukN01-019/Documents/Diego/python/archivos/json/lista.json","w")

lst = [{"nombre":"Paola","edad":25},
       {"nombre": "Carlos","edad":28},
       {"nombre": "Mateo","edad":28},
       {"nombre": "Patricia","edad":21},
       {"nombre": "juan","edad":19}]

json.dump(lst, fd)

fd.close()