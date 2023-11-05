class Vehiculo():

    def __init__(self):
        self.__marca = str();
        self.__modelo = str();
        self.__anio = bool();

    def getMarca(self):
        return self.__marca;
    
    def setMarca(self, mar):
        self.__marca = mar;

    def getModelo(self):
        return self.__modelo;
    
    def setModelo(self, modelo):
        self.__modelo = modelo; 

    def getAnio(self):
        return self.__anio;
    
    def setAnio(self, anio):
        self.__anio = anio;

    def imprimirInformacion(self):
        return self.__marca + " " + self.getModelo(); 

class Carro(Vehiculo):
    def imprimirInformacion(self):
        return "Carro: " + self.getMarca() + " " + self.getModelo();

class Bicicleta(Vehiculo):
    def imprimirInformacion(self):
        return "Bicicleta: " + self.getMarca() + " " + self.getModelo();
#cliente
vehiculo = Carro();
vehiculo.setMarca("Porshe")
bicicleta = Bicicleta();
bicicleta.setMarca("Shimano");

lista = [vehiculo, bicicleta];

for veh in lista:
    print(veh.imprimirInformacion())


#class Carro():

#class Bicicleta():