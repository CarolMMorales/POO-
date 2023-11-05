class Cuadrado():

    def __init__(self, lado1) -> None:
        self.__lado1 = lado1;
        self.__lado2 = lado1;

    def calcularArea(self):
        return self.__lado1 * self.__lado2;

class Rectangulo(Cuadrado):
    pass

lado = 4;
cuadrado = Rectangulo(lado)
respuesta = cuadrado.calcularArea();
print(f"El area de {lado} es igual a {respuesta}")

