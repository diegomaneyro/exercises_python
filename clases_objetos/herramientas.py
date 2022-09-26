class Herramientas:
    """
    Clase herramientas. metodos verificar primo, valor modal, canversion grados, factorial
    """
    def __init__(self, lista_numeros) -> None:
        if (type(lista_numeros) != list):
            self.lista = [0]
            raise ValueError('se creo una lista inicializada en cero. se esperaba un lista de numeros enteros')
        else:
            self.lista = lista_numeros

    def factorial(self, ):
        for i in self.lista:
            print(f'el factorial de: {i} es: {self.__factorial(i)}')

    def conversion_grados(self, entrada, salida):
        lista_parametros_esperados = ["celcius","kelvin","farenheit"]
        lista_grados = []
        if (str(entrada) not in lista_parametros_esperados):
            print('los paramaros esperados son: ',lista_parametros_esperados)
            return lista_grados
        if (str(salida) not in lista_parametros_esperados):
            print('los parametros esperados son: ',lista_parametros_esperados)
            return lista_grados
        for i in self.lista:
            lista_grados.append(self.__conversion_grados(i, entrada, salida))
        return lista_grados

    def verifica_primo(self, lista):
        lista_primo=[]
        if (type(lista) != list):#valida error de input
           raise ValueError('Error de ingreso tipo de dato, se esperaba una lista')
        else:
            for i in self.lista:
                if (self.__verficar_primo(i)):
                    lista_primo.append(True)
                else:
                    lista_primo.append(False)
            return lista_primo


    def valor_modal(self, menor):
        """
        numero modal: mas se repite de una lista y cual es el numero mas repetido
        pide menor o mayor
        retorna una lista con moda y maximo
        """
        lista_unicos = []
        lista_repetidos = []

        if len(self.lista) == 0:
            return None

        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)

        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repetidos[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repetidos.append(1)
        moda = lista_unicos[0]
        maximo = lista_repetidos[0]
        for i,e in enumerate(lista_unicos):
            if lista_repetidos[i]>maximo:
                maximo = lista_repetidos[i]
                moda = lista_unicos[i]
        return moda, maximo
    def __verficar_primo(self,numero):
        es_primo = True
        for i in range(2,numero):
            if numero % i == 0 :
                es_primo = False
                break
        if(es_primo):
            return es_primo
        else:
            es_primo = True

    def __conversion_grados(self,grados, entrada, salida):
        grados_salida = None
        if entrada == "celcius":
            if salida == "celcius":
                grados_salida = grados
            elif salida == "farenheit":
                grados_salida = (grados * 9 / 5) + 32
            elif salida == "kelvin":
                grados_salida = grados + 273.15
        if entrada == "farenheit":
            if salida == "celcius":
                grados_salida = (grados - 32) * 5 / 9
            elif salida == "farenheit":
                grados_salida = grados
            elif salida == "kelvin":
                grados_salida = ((grados - 32) * 5 / 9) + 273.15
        if entrada == "kelvin":
            if salida == "celcius":
                grados_salida = grados - 273.15
            elif salida == "farenheit":
                grados_salida = ((grados - 273.15) * 9 / 5) + 32
            elif salida == "kelvin":
                grados_salida = grados
        if not(entrada == "celcius" or entrada == "farenheit" or entrada == "kelvin"):
            return "Error. entrada es invalida"
        return grados_salida

    def __factorial(self,numero):
        numero_original = numero
        if (type(numero) != int):
            return 'Error. el tipo de dato no es entero'
        elif numero <1:
            return 'Error. el numero debe ser mayor a 1'
        if (numero>1):
            numero = numero * self.__factorial(numero-1)
        return numero

if __name__ == "__main__":
    a = Herramientas()
    #print(a.verficar_primo(5))

if __name__ == "__main__":
    lista = [12,32,5,5,5,1]
    moda,maximo = a.valor_modal(lista, True)
    #print(f'moda: {moda} maximo: {maximo}')

if __name__ == "__main__":
    """
    prueba:
    grados_salida = a.conversion_grados(1,"celcius","farenheit")
    print('1° celcius a farenheit',grados_salida,"f°")
    grados_salida = a.conversion_grados(1, "farenheit", "kelvin")
    print('1° farenheit a kelvin',grados_salida,"k°")
    grados_salida = a.conversion_grados(1, "kelvin", "celcius")
    print('1° kelvin a celcius',grados_salida,"c°")
    """
