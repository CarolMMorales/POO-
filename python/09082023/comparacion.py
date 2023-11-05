from vehiculo import Vehiculo

class ComparacionVehiculo:

    listadoVehiculos = [];#lista de tipo estático (Global a la clase)

    @staticmethod
    def definirListadoVehiculos(listadoVehiculos):
        ComparacionVehiculo.listadoVehiculos = listadoVehiculos;

    @staticmethod
    def obtenerVehiculoMasCostoso():
        
        valorVehiculoMasCosto = 0;
        vehiculoMasCostoso = Vehiculo("","","",0.0,"");

        for vehiculo in ComparacionVehiculo.listadoVehiculos:
            if vehiculo.obtenerPrecio() > valorVehiculoMasCosto:
                valorVehiculoMasCosto = vehiculo.obtenerPrecio(); 
                vehiculoMasCostoso = vehiculo;

        return vehiculoMasCostoso.obtenerInformacion();    

    @staticmethod    
    def obtenerVehiculoMenorCostoso():
        valorVehiculoMenosCosto = 99999999999;
        vehiculoMenosCostoso = Vehiculo("","","",0.0,"");

        for vehiculo in ComparacionVehiculo.listadoVehiculos:
            if vehiculo.obtenerPrecio() < valorVehiculoMenosCosto:
                valorVehiculoMenosCosto = vehiculo.obtenerPrecio(); 
                vehiculoMenosCostoso = vehiculo;

        return vehiculoMenosCostoso.obtenerInformacion();

    def obtenerCantidadVehiculosPorTipo(tipoVehiculo):
        cantidadVehiculosPorTipo = 0;
        for vehiculo in ComparacionVehiculo.listadoVehiculos:
            if vehiculo.obtenerTipoVehiculo() == tipoVehiculo:
                cantidadVehiculosPorTipo = cantidadVehiculosPorTipo + 1;

        return cantidadVehiculosPorTipo;