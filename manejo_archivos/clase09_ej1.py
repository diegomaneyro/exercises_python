import sys
if len(sys.argv)==4:
    print('El primer argumento es: ', sys.argv[1])
    print('El segundo argumento es: ', sys.argv[2])
    print('El tercer argumento es: ', sys.argv[3])
else:
    print('Error: Introdujo una cantidad de argumentos distinta de (3)')
    print('Ejemplo: clase09_ej1.py 1 2 3')
