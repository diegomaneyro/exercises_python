#importa paquetes
import os
import sys
import datetime
#comprovacion de seguridad, ejecutar si se recibieron tres argumentos

if len(sys.argv) == 4:
    marca_de_tiempo = datetime.datetime.now()#guarda enmarca de tiempo la fecha actual y hora
    marca_de_tiempo = datetime.datetime.timestamp(marca_de_tiempo)#convirte y sobre escribe la fecha en segundos

    temperatura = sys.argv[1]#guarda en las variables los argumentos
    humedad = sys.argv[2]#guarda en las variables los argumentos
    lluvia = sys.argv[3]#guarda en las variables los argumentos
    linea = str(marca_de_tiempo) + " " + temperatura + "," + humedad + "," + lluvia#concatena valores almacenados en las variables como str

    logs_lluvia = open('clase09_ej2.csv', "a")
    logs_lluvia.write(linea+"\n")
    logs_lluvia.close()
else:
    print('Error: introdujo una cantidad de argumentos distinta de tres (3)')
    print('Ejemplo: clase09_ej1.py <temperatura> <humedad> <true o false> ')








