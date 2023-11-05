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

class Docente(IntegranteComunidadUE):
   def obtenerEstudios():
     pass;

class Administrativo(IntegranteComunidadUE):
   def obtenerCargoActual():
     pass;

laura = Estudiante();
laura.setNombre("Laura");
print(laura.imprimirInformacion());
cesar = Docente();
cesar.setNombre("Cesar")
print(cesar.imprimirInformacion())
jesus = Administrativo();
jesus.setNombre("Jesus");
print(jesus.imprimirInformacion());


