def verifica_primo(numero):
    primo = True
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
            break
    return primo

lista1 = [2,5,4]
#print(verifica_primo(lista1[2]))

def repite_lista(lista,menor):
    if len(lista)== 0 :
        return None
    if (menor):
        lista.sort()
    else:
        lista.sort(reverse=True)

    lista_unicos = []
    lista_repite = []

    for e in lista:
        if e in lista_unicos:
            i = lista_unicos.index(e)
            lista_repite[i]+=1
        else:
            lista_unicos.append(e)
            lista_repite.append(1)

    maximo = lista_repite[0]
    modal = lista_unicos[0]

    for i,e in enumerate(lista_unicos):
        if lista_repite[i]>maximo:
              maximo = lista_repite[i]
              modal = lista_unicos[e]
    return maximo, modal



lista = [5,45,6,32,12,5,5,1,5,4,8,5,6,9,2,1,45]
maximo, moda = repite_lista(lista,True)
#print(maximo, moda)

def convierte_grados(grados, origen, salida):
    if origen == "celcius":
        if salida == "celcius":
            grados = grados
            return grados
        if salida == "farenheit":
            grados = (grados*9/5)+32
            return grados
        if salida == "kelvin":
            grados = grados+275.15
            return grados
    if origen == "farenheit":
        if salida == "celcius":
            grados = (grados -32) *5/9
            return grados
        if salida == "farenheit":
            grados = grados
            return grados
        if salida == "kelvin":
            grados = (grados-32)*5/9 +273.15
            return grados
    if origen == "kelvin":
        if salida == "celcius":
            grados = grados -273.15
            return grados
        if salida == "farenheit":
            grados = (grados-273.15)*9/5+32
            return grados
        if salida == "kelvin":
            grados = grados
            return grados
a_celcius = convierte_grados(30, "farenheit","celcius")
a_farenheit = convierte_grados(30, "kelvin","farenheit")
a_kelvin = convierte_grados(30, "celcius","kelvin")
"""print(a_celcius)
print(a_kelvin)
print(a_farenheit)"""

metricas = ["celcius","kelvin","farenheit"]
for i in range(0,3):
    for j in range(0,3):
        print(f'1 grado: {metricas[i]} a {metricas[j]}: {convierte_grados(1,metricas[i],metricas[j])}')