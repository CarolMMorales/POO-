class Objeto():
    def imprimirInformacion(self):
        print("Imprimir informacion Objeto")

class Lapiz(Objeto):
    def imprimirInformacion(self):
        print("Imprimir informacion de Lapiz")
'''
Aplicacion principio O (Open/Closed) porque la clase objeto no se
modificó
'''
objeto1 = Lapiz()
objeto2 = Lapiz()

listadoObjetos = [objeto1, objeto2]
for objeto in listadoObjetos:
    objeto.imprimirInformacion()
