#1.
# v1 = -2
# if v1 >0:
#     print(f"variable: {v1} es es mayor que cero")
# elif v1 < 0:
#     print(f"variable: {v1} es menor que cero")
# else:
#     print(f"variable: {v1} es igual a cero")

#2.
# v1 = "12"
# v2 = "12"
# if type(v1) == type(v2):
#     print("v1 y v2 son del mismo tipo de dato")
# else:
#     print("v1 y v2 son de diferentes tipos d datos")
#

#3.
# for i in range(1,21):
#     if i % 2 == 0:
#         print(f"{i} es par")
#     else:
#         print(f"{i} es impar")

#4.
# for i in range(1,6):
#     print(f"{i} elevado a la 3 es: {i**3}")
#

# #5.
# numero = 5
# for i in range(1,numero+1):
#     print(i)

#6.

# numero = int(input("ingrese un numero positivo mayor que cero: "))
#
# if (type(numero) == int):
#     if numero <= 0:
#         print("ingrese un numero mayor que cero")
#     else:
#         factorial = numero
#         while (numero>2):
#             numero = numero - 1
#             factorial = factorial * numero
#         print(f"El factorial es {factorial}")
# else:
#     print("ingrese un numero entero")

#7.
# n = 5
# while(n>0):
#     for i in range(0,n):
#         print(n)
#     n = n - 1
# print("fin del ciclo")

#8.
# n = 5
# for i in range(1,n):
#     while(n>0):
#         n = n-1
#         print(n)

#9.
#
# for i in range(1,31):
#     if i % 2 == 0:
#         print(f"{i}, es primo")


# while(n<maximo):
#     for i in range(2,n):
#         if (n % i == 0):
#             primo = False
#             break
#     if (primo):
#         print(n)
#     else:
#         primo = True
#     n += 1


#11.
maximo = 30
n = 0
primo = True
while(n<maximo):
    for i in range(2,n):
        if n % i == 0:
            primo= False
            break
    if(primo):
        print(n)
    else:
        primo = True
    n += 1

