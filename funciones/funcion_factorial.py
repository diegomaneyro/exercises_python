def factorial(numero):
    if type(numero) != int:
        return "El numero debe ser entero"
    if numero < 0:
        return "El numero  debe ser positivo "
    if numero > 1:
        numero = numero * factorial(numero -1)
    return numero
print(factorial(4))

