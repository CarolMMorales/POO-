class Vehiculo():

    def __init__(self, modelo, marca, anio, precio, tipo_vehiculo):
        self.__modelo = modelo;
        self.__marca = marca;
        self.__anio = anio;
        self.__precio = precio;
        self.__tipo_vehiculo = tipo_vehiculo;

    def obtenerInformacion(self):
        return "Informacion vehiculo:\nMarca:\t" + self.__marca + "\nModelo:\t" + self.__modelo + "\nPrecio:\t"  + str(self.__precio);

    def obtenerPrecio(self):
        return self.__precio;

    def obtenerTipoVehiculo(self):
        return self.__tipo_vehiculo;

def comparar(valor,valo2):
    return valor == valo2;

uniempresarial = ("2023");