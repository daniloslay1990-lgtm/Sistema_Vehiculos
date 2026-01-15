# Clase que maneja la lógica del sistema de control de transporte

class ControlTransporte:
    def __init__(self):
        self.vehiculos = []

    def registrar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_consumo(self):
        print("REPORTE DE CONSUMO DE VEHÍCULOS")
        print("-" * 35)

        for v in self.vehiculos:
            print(
                f"Marca: {v.get_marca()} | "
                f"Kilómetros: {v.get_kilometros()} km | "
                f"Consumo: {v.consumo():.2f} litros"
            )

