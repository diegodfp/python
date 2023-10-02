s = "yo soy tu padre"
# print(s[7])
# print(s[-8])
#recorrer las cadenas

for i in range(len(s)):
    print(s[i],end=",")
# # recorrido por elemento
# for e in s:
#     print(e, end=", ")

# slice

print("")
print(s[2:])
print(s[4:7])
print(s[::-1])

#find
print(s.find("pa"))
print(s.find("o"))
#rfind
print(s.rfind("o"))
#split() por ejemplo para separar nombres
nombre = "Juan Daniel Ramirez Salazar"
email= "juandaniel@gmail.com"
print(nombre.split("Juan"))
print(email.split("@"))