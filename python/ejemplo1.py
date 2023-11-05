class Carro():
    '''comentario 
    multilinea'''
    def __init__(self, color, modelo, m):
        print("Inicializar objeto")
        self.__color = color
        self.__modelo = modelo
        self.__marca = m;

    def arrancar(self):
        listado = self.validarParametrosEsc2();
        for mensajeError in listado:
            print(mensajeError)
        return "El carro de marca -> ", self.__marca;

    def validarParametros(self):
        listadoMensajesError = [];
        
        if self.__color == "":
            listadoMensajesError.append("Debe digitar color!");
        if self.__modelo == "":
            listadoMensajesError.append("Debe digitar modelo!")
        if(self.__marca == ""):
            listadoMensajesError.append("Debe digitar marca!");

        print(self.__marca == "")

        return listadoMensajesError;

    def validarParametrosEsc2(self):
        listadoMensajesError = [];
        
        if (self.__color == "" or self.__modelo == ""):
            listadoMensajesError.append("Validaciones incorrecta")
        
        return listadoMensajesError;

#Cliente
color = input("Digite color: ");
modelo = input("Digite modelo: ")
marca = input("Digite marca: ")
carroJDST = Carro(color,modelo,marca);
mensaje = carroJDST.arrancar();
print(mensaje)



        