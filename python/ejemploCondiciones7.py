class Operacion:

    def __init__(self):
        print("");
    
    def operar(self, opcion):
        match opcion:
            case "A": return "Usted ha seleccionado opcion A";
            case "B": return "Usted ha seleccionado opcion B";
            case "C": return "Usted ha seleccionado opcion C";

#cliente
opcion = input("Digite alguna operacion (A,B o C): ");
operacion = Operacion();
respuesta = operacion.operar(opcion);
print(respuesta)




