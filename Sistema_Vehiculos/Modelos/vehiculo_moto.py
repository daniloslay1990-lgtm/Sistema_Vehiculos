# Clase derivada que sobrescribe un método (polimorfismo)

from Sistema_Vehiculos.Modelos.vehiculo import Vehiculo


class VehiculoMoto(Vehiculo):
   
    def __init__(self, marca, kilometros, eficiencia):
        super().__init__(marca, kilometros)
        self.eficiencia = eficiencia

    def consumo(self):
        return self.get_kilometros() / self.eficiencia
