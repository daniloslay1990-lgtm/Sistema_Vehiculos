from Sistema_Vehiculos.Modelos.vehiculo import Vehiculo
from Sistema_Vehiculos.Modelos.vehiculo_moto import VehiculoMoto
from Sistema_Vehiculos.Modelos.vehiculo_auto import VehiculoAuto
from Sistema_Vehiculos.Servicios.control_transporte import ControlTransporte

control = ControlTransporte()

vehiculo1 = VehiculoAuto("Toyota", 300, 10)  
vehiculo2 = VehiculoMoto("Yamaha", 300, 40)

control.registrar_vehiculo(vehiculo1)
control.registrar_vehiculo(vehiculo2)

control.mostrar_consumo()
