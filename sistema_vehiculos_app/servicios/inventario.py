from typing import List
from modelos.vehiculo import Vehiculo

# CLASE DE SERVICIO
class InventarioVehiculos:
    def __init__(self):
       
        self.__vehiculos: List[Vehiculo] = []

    
    def agregar(self, vehiculo: Vehiculo) -> None:
        self.__vehiculos.append(vehiculo)

    def listar(self) -> List[Vehiculo]:
        return list(self.__vehiculos)

    
    def encender_todos(self) -> None:
        for v in self.__vehiculos:
            print(v.encender())

    
    def buscar(self, marca: str = None, modelo: str = None):
        resultado = self.__vehiculos

        if marca is not None:
            resultado = [
                v for v in resultado
                if v.marca.lower() == marca.lower()
            ]

        if modelo is not None:
            resultado = [
                v for v in resultado
                if v.modelo.lower() == modelo.lower()
            ]

        return resultado
