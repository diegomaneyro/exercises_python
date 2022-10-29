def ClaseVehiculo(tipo, color):
    class ClaseVehiculo(ClaseVehiculo):   
        def __init__(self,tipo, color):
            self.color = color
            self.tipo = tipo
            velocidad_vehiculo = 0
        
        def acelerar(self, velocidad):
            velocidad_vehiculo +=velocidad
            if (velocidad<0):
                velocidad_vehiculo = 0
            elif (velocidad>100):
                velocidad_vehiculo = 100 
            return velocidad_vehiculo
        
a = ClaseVehiculo('auto','gris')
print(a.Acelerar(10)) 
a.Acelerar(15) 
a.Acelerar(-10)