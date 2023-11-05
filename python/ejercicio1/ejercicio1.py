from operaciones import Suma, Resta, Multiplicacion, Division


class ProgramacionOperaciones():
    def calcularOperaciones(self):
        suma = Suma()#paso 2
        resta = Resta();#paso 4
        multiplicacion = Multiplicacion();#paso 6
        division = Division()#paso 8
        listaOperaciones = [suma, resta, multiplicacion, division];

        for operacion in listaOperaciones:
            operacion.calcular(6,4);#pasos 10, 12,14 y 16

#usuario/Programador
po = ProgramacionOperaciones()
po.calcularOperaciones();#paso 1