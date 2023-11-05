from abc import ABC

class FiguraGeometrica(ABC):
    def calcularArea():
        pass

class Rectangulo(FiguraGeometrica):

    def __init__(self, alto, ancho) -> None:
        #super().__init__()
        self.__alto = alto;
        self.__ancho = ancho;
    
    def calcularArea(self):
        return self.__ancho * self.__alto;

class Cuadrado(FiguraGeometrica):

    def __init__(self, lado) -> None:
        #super().__init__()
        self.__lado = lado;
    
    def calcularArea(self):
        return self.__lado * self.__lado;

#cliente
cuadrado = Cuadrado(2)
rectangulo = Rectangulo(2,4)

listaFiguras = []
listaFiguras.append(cuadrado)
listaFiguras.append(rectangulo)

for figura in listaFiguras:
    print(f"Area figura {type(figura)} es  {figura.calcularArea()}")