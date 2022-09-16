#funcion que encuentra repetidos en una lista. devuelve el numero mas repetido y la catidad
def numero_modal(lista,menor):
    lista_repetidos =[]
    lista_unicos = []

    if len(lista) == 0:
        return None

    if menor:
        lista.sort()
    else:
        lista.sort(reverse=True)

    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repetidos[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repetidos.append(1)

    modal = lista_unicos[0]
    maximo = lista_repetidos[0]

    for i,e in enumerate(lista_unicos):

        if lista_repetidos[i] > maximo:
            modal = lista_unicos[i]
            maximo = lista_repetidos[i]

    return modal, maximo



lista_numero = [1,1,4,5,6,8,7,9,6,5,4,8,2,1,5,6,9,2,2,8,4,2,5]
moda, repite = numero_modal(lista_numero, True)
print(moda, repite)


