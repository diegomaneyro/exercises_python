class vehiculo:
    
    def __init__(self,color,tipo, cilindrada):
        self.color = color
        self.cilindrada = cilindrada
        self.tipo = tipo
        self.velocidad = 0
        self.direccion = 0


    def __str__(self):
        return f'Soy: {self.tipo} de color: {self.color} y mi cilindrada es: {self.cilindrada} cc'

    def estado(self):
        return f'velocidad: {self.velocidad} direccion: {self.direccion}'

    def Acelerar(self, vel):
        self.velocidad +=vel

    def Frenar(self, vel):
        self.velocidad-= vel

    def Doblar(self,grados):
        self.direccion += grados



vehiculo_2 = vehiculo("azul", "motocicleta", 250)
vehiculo_2.Acelerar(160)
vehiculo_2.Frenar(120)
vehiculo_2.Doblar(90)

print(vehiculo_2.__str__())
print(vehiculo_2.estado())

vehiculo_2 = vehiculo("rojo", "automovil", 1100)
vehiculo_2.Acelerar(260)
vehiculo_2.Frenar(60)
vehiculo_2.Doblar(45)

print(vehiculo_2.__str__())
print(vehiculo_2.estado())