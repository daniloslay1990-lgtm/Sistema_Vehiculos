from modelos.auto import Auto
from modelos.motocicleta import Motocicleta
from servicios.inventario import InventarioVehiculos

# FUNCIÓN PRINCIPAL
# Punto de entrada del programa
def main():
    # Creación del inventario
    inventario = InventarioVehiculos()

    # Creacion de objetos
    auto1 = Auto("Chevrolet", "Sail", 4)
    moto1 = Motocicleta("Honda", "HY457X", 190)

    # Agregamos los objetos al inventario
    inventario.agregar(auto1)
    inventario.agregar(moto1)

    print("=== Encendiendo vehículos ===")
    inventario.encender_todos()

    print("\n=== Buscar por marca ===")
    encontrados = inventario.buscar(marca="Honda")

    for v in encontrados:
        print(f"- {v.marca} {v.modelo} (encendido={v.esta_encendido()})")

# Condición para ejecutar el programa
if __name__ == "__main__":
    main()
