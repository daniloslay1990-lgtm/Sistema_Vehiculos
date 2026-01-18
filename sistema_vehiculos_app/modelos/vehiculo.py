from abc import ABC, abstractmethod

# ABSTRACCIÓN
# Clase base abstracta que define lo que todo vehículo debe tener
class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.__en_marcha = False  # Encapsulación

    def esta_encendido(self) -> bool:
        return self.__en_marcha

    def _cambiar_estado(self, estado: bool) -> None:
        self.__en_marcha = estado

    @abstractmethod
    def encender(self) -> str:
        pass

    def apagar(self) -> str:
        self._cambiar_estado(False)
        return f"{self.marca} {self.modelo} apagado."