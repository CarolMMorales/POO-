from comparacion import ComparacionVehiculo;
from vehiculo import Vehiculo, comparar,uniempresarial;

renault_oroch_zen = Vehiculo("Oroch Zen 4x4", "Renault","2023", 108000000, "vans");
toyota_hilux_chasis = Vehiculo("Hilux 2.7 4x2 Chasís", "Toyota","2023", 123000000, "vans");
chevrolet_joy_nb = Vehiculo("Joy NB", "Chevrolet","2023", 65000000, "automovil");
listadoVeh = [toyota_hilux_chasis,chevrolet_joy_nb,renault_oroch_zen];
ComparacionVehiculo.definirListadoVehiculos(listadoVeh);
print(ComparacionVehiculo.obtenerVehiculoMasCostoso());
print(ComparacionVehiculo.obtenerVehiculoMenorCostoso());
resultado = ComparacionVehiculo.obtenerCantidadVehiculosPorTipo("camioneta");
print("Cantidad vehiculos por tipo: ", resultado);
print(uniempresarial);