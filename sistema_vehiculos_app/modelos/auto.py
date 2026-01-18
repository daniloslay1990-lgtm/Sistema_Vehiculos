from modelos.vehiculo import Vehiculo

# HERENCIA
class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, numero_puertas: int):
        
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas

    # POLIMORFISMO:
    # Implementación propia del método encender
    def encender(self) -> str:
        self._cambiar_estado(True)
        return (
            f"Auto {self.marca} {self.modelo} encendido "
            f"con {self.numero_puertas} puertas"
        )
