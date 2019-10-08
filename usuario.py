from tipousuariosenum import TipoUsuariosEnum

class Usuario:
    ## CONSTRUCTOR
    def __init__(self, nombre, apellido, dni, contrasena, tipo, activo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__contrasena = contrasena
        self.__tipo = tipo
        self.__activo = activo
    
    ## GETTERS Y SETTERS

    def setactivo(self, activo):
        self.__activo = activo

    def getactivo(self):
        return self.__activo

    def setnombre(self, nombre):
        self.__nombre = nombre

    def getnombre(self):
        return self.__nombre

    def setapellido(self, apellido):
        self.__apellido = apellido

    def getapellido(self):
        return self.__apellido

    def setcontrasena(self, contrasena):
        self.__contrasena = contrasena

    def getcontrasena(self):
        return self.__contrasena
    
    # DEVNOTE: tipo y dni no tienen setter ya que no
    # deberian cambiar a lo largo del tiempo

    def gettipo(self):
        if(self.__tipo == TipoUsuariosEnum.ADMINISTRADOR):
            return 'Administrador'
        elif(self.__tipo == TipoUsuariosEnum.CLIENTE):
            return 'Cliente'
        else: 
            return 'Mecanico'
            
    def getdni(self):
        return self.__dni