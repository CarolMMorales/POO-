from abc import ABC

class IOperacion(ABC):
    def calcular(x ,y):
        pass

class Suma(IOperacion):

    def __init__(self):
        print("constructor Suma()")#paso 3 (OK)

    def calcular(self,x ,y):
        resultado = x + y;
        print(f"El valor de la operacion suma {x} y {y} es {resultado}");

class Resta(IOperacion):

    def __init__(self):
        print("constructor Resta()")#paso 5 (OK)

    def calcular(self,x ,y):
        resultado = x - y;
        print(f"El valor de la operacion resta {x} y {y} es {resultado}");

class Multiplicacion(IOperacion):

    def __init__(self):
        print("constructor Multiplicacion()")#paso 7 (OK)

    def calcular(self,x ,y):
        resultado = x * y;
        print(f"El valor de la operacion multiplicacion {x} y {y} es {resultado}");

class Division(IOperacion):

    def __init__(self):
        print("constructor Division()")#paso 9 (OK)

    def calcular(self,x ,y):
        resultado = x / y;
        print(f"El valor de la operacion division {x} y {y} es {resultado}");
