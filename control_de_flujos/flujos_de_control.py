#1.
"""
num = int(input("ingrese un numero entero: "))
if num<0:
    print(f"El numero: {num} es menor que cero")
elif num==0:
    print(f"El numero: {num} es cero")
else:
    print("Numero: ", num, " es mayor que cero")
"""

"""
#2.
v1 = 3.1415
v2 = 31415
if (type(v1)==type(v2)):
    print("v1 y v2: si ,son del mismo tipo de dato")
else:
    print("v1 y v2: no , son del mismo tipo de dato")
"""

#3.
"""
for i in range(1,21):
    if i % 2 == 0:
        print(i, "Es par")
"""

#4.
""""
for i in range(0,6):
     print(f"{i} al cubo= ", i**3)
"""

"""
5.
mi_variable = 7

for i in range(0,mi_variable):
    print(i)
"""

#6.
"""
num = int(input("ingrese un numero entero mayor que cero:"))
if(type(num)==int):
    if(num>0):
        factorial = 1
        while(num>1):
            factorial = num * factorial
            num -= 1
        print("El factorial es: ", factorial)
    else:
        print("ingrese numero mayor que cero")
else:
    print("tipo de dato invalido")
"""

#7.
"""
num = 5
while(num>1):
    for i in range(0,num):
        print(f"i vale: {i}")
        num -=1
"""

#8.
"""num = 5
for i in range(0,num):
    while(num>1):
        print(num)
        num -=1
"""

#9.
"""n = 0
tope_maximo = 30
es_primo = True
ciclos_for = 0
while(n<tope_maximo):
    for i in range(2, n):
        ciclos_for += 1
        if n % i == 0:
            es_primo = False
            break
    if(es_primo):
        print(n, " Es primo")
    else:
        es_primo = True
    n += 1
print("ciclos for: ", ciclos_for)
"""

#10.
"""n = 99
tope = 300
while(n<=tope):
    n +=1
    if (n % 12 !=0):
        continue
    print(n, "es divisible por 12")

"""
#14.
# numero = 1
# primo = True
# sigue = 1
# while(sigue == 1):
#     for i in range(2,numero):
#         if (numero % i == 0):
#             primo = False
#             break
#     if(primo):
#         print(numero, "es primo")
#         print("desea buscar otro numero primo? presione 1 para continuar")
#         if (input() != "1"):
#             print("fin del proceso")
#             break
#
#     else:
#         primo = True
#     numero += 1

#15.
# n = 99
# tope_rango = 300
# while(n<= 300):
#     n += 1
#     if n % 3 == 0:
#         if n % 6 == 0:
#             print("numero encontrado: ", n)
#             break
#
