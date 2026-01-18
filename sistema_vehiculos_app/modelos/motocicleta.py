from modelos.vehiculo import Vehiculo

# HERENCIA
class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, cilindrada: int):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    # POLIMORFISMO
    # Misma acción de encendido pero comportamiento diferente
    def encender(self) -> str:
        self._cambiar_estado(True)
        return (
            f"Motocicleta {self.marca} {self.modelo} encendida "
            f"({self.cilindrada} cc)"
        )
