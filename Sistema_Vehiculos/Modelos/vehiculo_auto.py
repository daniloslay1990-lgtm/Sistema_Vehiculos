from Sistema_Vehiculos.Modelos.vehiculo import Vehiculo

class VehiculoAuto(Vehiculo):
    """
    Clase derivada para automóviles.
    Aplica polimorfismo al calcular el consumo.
    """

    def __init__(self, marca, kilometros, rendimiento):
        super().__init__(marca, kilometros)
        self.rendimiento = rendimiento  # km por litro

    def consumo(self):
        return self.get_kilometros() / self.rendimiento
