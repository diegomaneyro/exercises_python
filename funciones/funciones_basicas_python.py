mi_lista = ["Buenos Aires","Mendoza","San Luis","Corrientes","Chaco","Santa Fe"]
print(mi_lista)
mi_lista2 =[1,2,3,4,5]
# print(mi_lista.count("Roma"))
# print(mi_lista)
# elemento = "Mendoza"
# if not(elemento in mi_lista):
#     mi_lista.append(elemento)
#     print("Se agrego elelemento: ", elemento)
# else:
#     print("el elemento:", elemento, "Ya exite")
# mi_lista.remove()
#lenar tupla con for
#tupla = tuple(for i in i range(0,20)
tupla = tuple(mi_lista)
print(tupla)
#print(len(tupla))

v1,v2,v3, _, _, _ = tupla
#print(v1,v2,v3)

dicc = {
    "Ciudades":mi_lista
}
dicc.setdefault("numeros",mi_lista2)
print(dicc.pop("numeros"))
print(dicc.pop("Ciudades"))
print(dicc)
