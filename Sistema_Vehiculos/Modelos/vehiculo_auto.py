# Clase derivada para automóviles

from Sistema_Vehiculos.Modelos.vehiculo import Vehiculo

class VehiculoAuto(Vehiculo):
    
    def __init__(self, marca, kilometros, rendimiento):
        super().__init__(marca, kilometros)
        self.rendimiento = rendimiento  # km por litro

    def consumo(self):
        return self.get_kilometros() / self.rendimiento
