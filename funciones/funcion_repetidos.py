import random


def valor_modal(lista):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] +=1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]

def valor_maximo(lista):
    print(lista_num)
    lista_max = []
    print(max(set(lista_num), key = lista_num.count))

lista_num = [random.randint(0, 50) for _ in range(18)]
mi_lista2 =[1,2,3,4,5,5,5]
valor_maximo(mi_lista2)

