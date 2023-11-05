class IntegranteComunidadUE():

    def __init__(self):
        self.__nombre = str();
    
    def getNombre(self):
        return self.__nombre;

    def setNombre(self, nom):
        self.__nombre = nom;

    def imprimirInformacion(self):
        return self.__nombre;

class Estudiante(IntegranteComunidadUE):
    def obtenerCarrera():
        pass;
    def imprimirInformacion(self):
        return self.getNombre() + " es una estudiante de UE";

class Docente(IntegranteComunidadUE):
    def obtenerEstudios():
        pass;
    def imprimirInformacion(self):
            return self.getNombre() + " es un docente de UE";

class Administrativo(IntegranteComunidadUE):
    def obtenerCargoActual():
        pass;
    def imprimirInformacion(self):
        return self.getNombre() + " es un administrativo de UE";
#------CLIENTE----
laura = Estudiante();
laura.setNombre("Laura");
cesar = Docente();
cesar.setNombre("Cesar")
jesus = Administrativo();
jesus.setNombre("Jesus");

listadoComunidadUE = [laura, cesar, jesus];

#Polimorfismo
for estudiante in listadoComunidadUE:
    print(estudiante.imprimirInformacion());


