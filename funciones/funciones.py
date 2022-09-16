"""
funcion que verifca si un numero entero es primo inicializa elvalor in True
si la condicion entre 1 y N la condicion cambia a False
"""
def verifcar_primo(numero):
    es_primo = True
    for i in range(2,numero):
        if numero % i == 0:
            es_primo = False
            break
    return es_primo

lista_numeros = [i for i in range(0,21)]

def devuelve_primos_lista(lista):
    lista_primos = []
    for i in lista:
        if verifcar_primo(int(i)):
            lista_primos.append(i)
    return lista_primos

devuelve_primos_lista(lista_numeros)
#print(lista_primos)

def deveuelve_mas_repetido(lista):
    pass