"""
mi_lista = ["merlo","padua","ituzaingo","moron","pontevedra"]
mi_lista_provincias = ["buenos aires","entre rios","la pampa"]
nueva_lista = ["chubut","neuquen","usuahia"]
mi_lista.extend(["jujuy","salta"])
mi_lista.extend([nueva_lista])

print(mi_lista[:])
print(mi_lista[1])
print(mi_lista[1:4])
print(type(mi_lista))
print(mi_lista[3:])
print(mi_lista[:4])

# mi_lista.append("merlo")
# mi_lista.append("castelar")
# # print(mi_lista)
# mi_lista.insert(3,"paso del rey")
# mi_lista.extend(mi_lista_provincias)

# #print(f'elemento duplicado (merlo) indice : {mi_lista.index("merlo")}')
# #print(mi_lista.index("chubut"))
# ultimo_elemento = mi_lista.pop()
# #print(ultimo_elemento)
# #print(mi_lista*4)

# mi_lista_numeros = []

# for i in range(1,21):
#     mi_lista_numeros.append(i)
#     mi_tupla_numeros = tuple(mi_lista_numeros)

# # print(mi_tupla_numeros[9:15])
# # if mi_tupla_numeros.count(20):
# #     print(f"Elemento: 20. Encontrado")
# #     if mi_tupla_numeros.count(30):
# #         print(f"Elemento: 30. Encontrado")
# #     else:
# #         print("Elemento: 30. No se encuetra ")
# # else:
# #     print("Elemento: 20. No se encuetra ")
#
#

# # for i in range(0, len(mi_lista)):
# #     if mi_lista[i]=="paris":
# #         print(f'Elemento: "paris" encotrado')
# #     else:
# #         mi_lista.append("paris")
# #         encontrado = mi_lista.pop()
# #         print(f"se agrego: {encontrado}")
# #         print(mi_lista)
# #         break
# #
# # print(mi_lista)
# # print(mi_tupla_numeros)
# # busca = 2
# # contador = 0
# # for i in range(0,len(mi_tupla_numeros)):
# #     if mi_tupla_numeros[i] == busca:
# #         contador += 1
# # print(f'{busca} encontrado {contador} veces')
# #
# mi_lista_numeros = list(mi_tupla_numeros)
# print(mi_lista_numeros)
# v1 = mi_lista_numeros[0]
# v2 = mi_lista_numeros[1]
# v3 = mi_lista_numeros[2]
# print(v1,v2,v3)

dicc = {
    "ciudad": (mi_lista),
    "pais": ("argentina"),
    "continente": ("america")
     }
# print(dicc.keys())
# print(dicc.get("ciudad"))
# print(dicc.get("pais"))
# print(dicc.get("continente"))"""