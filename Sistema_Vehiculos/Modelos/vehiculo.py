#Demuestra encapsulación y herencia

class Vehiculo:
    
    def __init__(self, marca, kilometros):
        self.__marca = marca          
        self.__kilometros = kilometros

    def get_marca(self):
        return self.__marca

    def get_kilometros(self):
        return self.__kilometros

    def consumo(self):
        return 0

