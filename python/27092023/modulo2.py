import operator

class MedioTransporte():

    def __init__(self):
        self.__nombre = ""
        self.__descripcion = "";

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getDescripcion(self):
        return self.__descripcion
    

class Vehiculo(MedioTransporte):
    def __init__(self):
        self.__marca = "";
        self.__descripcion = "";
        self.__valor = 0.0

    def setMarca(self, marca):
        self.__marca = marca
    def getMarca(self):
        return self.__marca;

    def setDescripcion(self, desc):
        self.__descripcion = desc
    def getDescripcion(self):
        return self.__descripcion
    
    def setValor(self, val):
        self.__valor = val
    def getValor(self):
        return self.__valor;

    def obtenerInfo(self):
        return "Vehiculo " + self.getMarca() + "Modelo " + self.getDescripcion() + ", con valor de " + str(self.__valor)


class Moto(MedioTransporte):
    def __init__(self):
        self.__marca = "";
        self.__descripcion = "";
        self.__valor = 0.0

    def setMarca(self, marca):
        self.__marca = marca
    def getMarca(self):
        return self.__marca;

    def setDescripcion(self, desc):
        self.__descripcion = desc
    def getDescripcion(self):
        return self.__descripcion
    
    def setValor(self, val):
        self.__valor = val
    def getValor(self):
        return self.__valor;

class FabricaVehiculos():

    def __init__(self):
        self.__listadoVehiculos = []

    def inicializarListadoVehiculos(self):
        joyNbJDST = Vehiculo()
        joyNbJDST.setDescripcion("JOY NB")
        joyNbJDST.setMarca("Chevrolet")
        joyNbJDST.setValor(65000000.45)
        self.__listadoVehiculos.append(joyNbJDST)

        mazdaGTSigMU = Vehiculo()
        mazdaGTSigMU.setDescripcion("CX-60 3.3 Grand Touring Signature AT")
        mazdaGTSigMU.setMarca("Mazda")
        mazdaGTSigMU.setValor(241000000.00) 
        self.__listadoVehiculos.append(mazdaGTSigMU)
        
        ExplorerLimitedDEVG = Vehiculo()
        ExplorerLimitedDEVG.setDescripcion("Explorer Limited 4X4")
        ExplorerLimitedDEVG.setMarca("Ford")
        ExplorerLimitedDEVG.setValor(268000000.00) 
        self.__listadoVehiculos.append(ExplorerLimitedDEVG)      

        mazdaSedanSMC = Vehiculo()
        mazdaSedanSMC.setDescripcion("3 SEDAN 2.5 GRAND TOURING AUT LX")
        mazdaSedanSMC.setMarca("Mazda")
        mazdaSedanSMC.setValor(129000000.00)
        self.__listadoVehiculos.append(mazdaSedanSMC)

        NPRJMOJ = Vehiculo()
        NPRJMOJ.setDescripcion("NPR BUSETON")
        NPRJMOJ.setMarca("Chevrolet")
        NPRJMOJ.setValor(171500000)
        self.__listadoVehiculos.append(NPRJMOJ)

        EquinoxAFCT = Vehiculo()
        EquinoxAFCT.setDescripcion("EQUINOX RS")
        EquinoxAFCT.setMarca("Chevrolet")
        EquinoxAFCT.setValor(160000000)
        self.__listadoVehiculos.append(EquinoxAFCT)

        SONETMDLG = Vehiculo()
        SONETMDLG.setDescripcion("SONET VIBRANTS 1.5")
        SONETMDLG.setMarca("KIA")
        SONETMDLG.setValor(101000000)
        self.__listadoVehiculos.append(SONETMDLG)

        AMGMARB = Vehiculo()
        AMGMARB.setDescripcion("AMG GLC 43 4MATIC COUPE")
        AMGMARB.setMarca("MERCEDES BENZ")
        AMGMARB.setValor(1400000000)
        self.__listadoVehiculos.append(AMGMARB)

        RAV425XROAD = Vehiculo()
        RAV425XROAD.setDescripcion("RAV42.5X-ROAD")
        RAV425XROAD.setMarca("Toyota")
        RAV425XROAD.setValor(209000000)
        self.__listadoVehiculos.append(RAV425XROAD)

        RSQ3BP = Vehiculo()
        RSQ3BP.setDescripcion("RSQ3ST QUATTRO BP")
        RSQ3BP.setMarca("AUDI")
        RSQ3BP.setValor(387000000)
        self.__listadoVehiculos.append(RSQ3BP)

        HondaAccordav6=Vehiculo()
        HondaAccordav6.setDescripcion("Accord V6")
        HondaAccordav6.setMarca("Honda")
        HondaAccordav6.setValor(108000000)
        self.__listadoVehiculos.append(HondaAccordav6)

        M4CompetitionJDTM = Vehiculo()
        M4CompetitionJDTM.setDescripcion("M4 COMPETITION PRO COUPE")
        M4CompetitionJDTM.setMarca("BMW")
        M4CompetitionJDTM.setValor(750000000)
        self.__listadoVehiculos.append(M4CompetitionJDTM)

        renaultSanderoZEN = Vehiculo()
        renaultSanderoZEN.setDescripcion("Renault Sandero Zen")
        renaultSanderoZEN.setMarca("Renault")
        renaultSanderoZEN.setValor(75000000.00)
        self.__listadoVehiculos.append(renaultSanderoZEN)

        SuzukiSwift = Vehiculo()
        SuzukiSwift.setDescripcion("SuzukiSwiftSedanTam")
        SuzukiSwift.setMarca("Suzuki")
        SuzukiSwift.setValor(81680000.00)
        self.__listadoVehiculos.append(SuzukiSwift)

        renaultFluenceFARU = Vehiculo()
        renaultFluenceFARU.setDescripcion("Renault Fluence")
        renaultFluenceFARU.setMarca("Renault")
        renaultFluenceFARU.setValor(34500000)
        self.__listadoVehiculos.append(renaultFluenceFARU)

    def obtenerVehiculoMasCostoso(self):
        vehiculoMasCostoso = Vehiculo()
        vehiculoMasCostoso.setDescripcion("Marca gato")
        vehiculoMasCostoso.setMarca("Cat")
        vehiculoMasCostoso.setValor(0)
        for vehiculo in self.__listadoVehiculos:
            esMasCostoso = vehiculo.getValor() > vehiculoMasCostoso.getValor();
            if esMasCostoso:
                vehiculoMasCostoso = vehiculo
        return vehiculoMasCostoso
    
    def obtenerVehiculoMenosCostoso(self):
        vehiculoMenosCostoso = Vehiculo()
        vehiculoMenosCostoso.setDescripcion("bugatti JDST")
        vehiculoMenosCostoso.setMarca("BUGATTI")
        vehiculoMenosCostoso.setValor(4000000000)
        for vehiculo in self.__listadoVehiculos:
            esMenosCostoso = vehiculo.getValor() <= vehiculoMenosCostoso.getValor();
            if esMenosCostoso:
                vehiculoMenosCostoso = vehiculo
        return vehiculoMenosCostoso
    

    def obtenerMarcaMasVendida(self):

        listadoMarcasVendidas = self.generarListadoMarcasVendidas()
        listadoMarcasOrdenadas = sorted(listadoMarcasVendidas.items(),
                                        key=operator.itemgetter(1),
                                        reverse=True)
        return listadoMarcasOrdenadas
    
    
    def generarListadoMarcasVendidas(self):
        
        listadoMarcasVendidas = dict()
        for vehiculo in self.__listadoVehiculos:
            marca = vehiculo.getMarca()
            if marca not in listadoMarcasVendidas:
                listadoMarcasVendidas[marca] = 1
            else: 
                listadoMarcasVendidas[marca] = listadoMarcasVendidas[marca] + 1
        return listadoMarcasVendidas
        



        



#CLIENTE - Crear vehiculos
sucursalPA = FabricaVehiculos()
sucursalPA.inicializarListadoVehiculos();
vehiculoMasCostoso = sucursalPA.obtenerVehiculoMasCostoso();
print(vehiculoMasCostoso.obtenerInfo())
vehiculoMenosCostoso = sucursalPA.obtenerVehiculoMenosCostoso();
print(vehiculoMenosCostoso.obtenerInfo())
print(sucursalPA.obtenerMarcaMasVendida())






    