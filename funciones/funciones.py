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
            grados_salida = grados
        elif salida == "farenheit":
            grados_salida = (grados*9/5)+32
        elif salida == "kelvin":
            grados_salida = grados+275.15
    if origen == "farenheit":
        if salida == "celcius":
            grados_salida = (grados -32) *5/9
        elif salida == "farenheit":
            grados_salida = grados
        elif salida == "kelvin":
            grados_salida = (grados-32)*5/9 +273.15
    if origen == "kelvin":
        if salida == "celcius":
            grados_salida = grados -273.15
        elif salida == "farenheit":
            grados_salida = (grados-273.15)*9/5+32
        elif salida == "kelvin":
            grados_salida = grados
    return grados_salida

a_celcius = convierte_grados(30, "farenheit","celcius")
a_farenheit = convierte_grados(30, "kelvin","farenheit")
a_kelvin = convierte_grados(30, "celcius","kelvin")
"""
print(a_celcius)
print(a_kelvin)
print(a_farenheit)
"""

metricas = ["celcius","kelvin","farenheit"]
for i in range(0,3):
    for j in range(0,3):
        """print(f'1 grado: {metricas[i]} a {metricas[j]}: {convierte_grados(1,metricas[i],metricas[j])}')
"""

def factorial(numero):
   if type(numero) != int:
       return 'Error: Ingrese un numero entero'
   elif numero<0:
       return 'Error: Ingrese un numero positivo'
   elif(numero>1):
       numero = numero * factorial(numero-1)
   return numero


numero = 4
resultado = factorial(numero)
print(f'el factorial de: {numero} es: {resultado}')


