
#1
"""
mi_lista = []
n = -15
while(n < 0):
    mi_lista.append(n)
    n +=1
print(mi_lista[:])
"""

#2.
from collections.abc import Iterable

"""
n=0
while(n<len(mi_lista)):
    if mi_lista[n] % 2 == 0:
        print(f'{mi_lista[n]}: es par')
    n+=1
"""

#3.
"""
for i in range(0,len(mi_lista)):
    if mi_lista[i] % 2 == 0:
        print(f"{mi_lista[i]}: es par")
"""

#4.
"""
for i in range(0,3):
     print(mi_lista[i])
    
"""

#5.
"""
for i,e in enumerate(mi_lista):
    print(i,e)
"""

#6.
"""
lista = [1,2,5,7,8,10,13,14,15,17,20]

for i in range(1,20):
    if(not(i in lista)):
        lista.insert((i-1),i)
print(lista)
"""

#7.fibonacci
"""lista_fibonacci = [0,1]
n = 2
aux = 0
while(n<30):
    lista_fibonacci.append(lista_fibonacci[n-2]+lista_fibonacci[n-1])
    n += 1
print(lista_fibonacci, sum(lista_fibonacci))
"""
"""
lista = [i for i in range(0,39)]
cadena  = "cadena"
for e,c in enumerate(cadena):
    if c == "a": 
        print(e,c)
"""
"""lista = [1,2,5,4,5,8,6,6]
print(lista)
print(sum(lista))
lista_nombre = ["diego"]

print("-".join("diego mauro daniel"))
"""
mi_dicc = {
    "nombre":["diego","mauro","daniel"],
    "apellido":["maneyro"]
    }
mi_dicc.setdefault("edad",[39])
mi_dicc["direccion"] = ["sucre1279"]
for i in mi_dicc:
    print(i)

"""""
libro = ["pagina1","pagina2","pagina3","pagina4"]
marca_paginas = iter(libro)

print(next(marca_paginas))
print(next(marca_paginas))
print(next(marca_paginas))
print(next(marca_paginas))
print(next(marca_paginas))
print(next(marca_paginas))
"""
"""
a = [1,2,3]
b = ["Diego","Mauro","Daniel"]
c = zip(a,b)

print(list(c))
"""
"""
frace = "Y pensar que me la lleve al rio creyedo que era mozuela"
e = [i for i in frace if i == "e"]
print(len(list(e)))

"""




"""letra = "n"
cadena = "Hola Mundo. Esto es una practica del lenguaje de programación Python"
for e,i in enumerate(cadena):
    if i == "n":
        print(f'posicion: {e} letra: {i}')
"""
"""cadena = "Hola Mundo. Esto es una practica del lenguaje de programación Python"
lista_cadena = list(cadena)
print(type(lista_cadena))
print(lista_cadena)

recorre = iter(lista_cadena)
largo = len(lista_cadena)
for i in range(0,largo):
    print(next(recorre))

lista1 = [1,2,3,4,5]
lista2 = ["a","b","c","d","e"]
tupla1 = zip(lista1,lista2)
print(tuple(tupla1))
"""
"""
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lista_div =[i for i in lis if i % 7 == 0]
print(lista_div)
"""
"""
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cantidad = 0
for i in lis:
    if type(i)== list:
        cantidad += len(i)
    else:
        cantidad+=1
print(f'cantidad de elementos en la lista: {cantidad}')

for i,e in enumerate(lis):
    if type(e) != list:
        lis[i] = [e]
print(lis)
"""
"""#fibo
fibonacci = [0,1]
n = 2
while(n<30):
    fibonacci.append(fibonacci[n-1]+fibonacci[n-2])
    n+=1
print(fibonacci)
print(f'suma de elementos en lista fibonaci: {sum(fibonacci)}')

n = 2
while(n<len(fibonacci)):
    print(fibonacci[n]/fibonacci[n-1])
    n+=1

"""












