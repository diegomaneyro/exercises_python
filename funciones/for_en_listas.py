import random

#llenando lista con numeros enteros consecutivos con for desde el 1 hasta el 20
#lista_numeros_enteros = [i for i in range(1, 20)]
#print(lista_numeros_enteros)
#llenando lista con numeros enteros de forma aleatorio entre 0 y 800 cantidad de 20 numeros
#lista_numeros_aleatorios = [random.randint(0, 800)for _ in range(20)]
#print(lista_numeros_aleatorios)
"""
llenando lista de numeros enteros de forma aleatrorio la cantidad que el usuarios desee
en un rango desde 1 hasta 50
"""

#cantidad_numeros = int(input("Cuantos numeros aleaorios desea en su lista: "))
#lista_pedida_aleatorio = [random.randint(1,500)for _ in range(cantidad_numeros)]
#print(lista_pedida_aleatorio)
"""funcion que calcula el numero que se repite mas veces en una lista
"""

def numero_repetido(lista):
    print(max(set(lista), key=lista.count))

lista_numeros_aleatorios = [12,45,46,635,45,21,56,5,4,6,9,8,14,2,2,5,4,2,6,5,8,4]
lista_frutas = ["pera","pera","manzana","pera"]
print(lista_frutas)
numero_repetido(lista_frutas)