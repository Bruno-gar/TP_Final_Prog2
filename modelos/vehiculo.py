import math
from marcavehiculosenum import MarcaVehiculosEnum
cantidadVehiculos = 0


class Vehiculo:
    # CONSTRUCTOR
    def __init__(self, marca, modelo, dueno):
        self.__marca = marca
        self.__modelo = modelo
        self.__dueno = dueno
        global cantidadVehiculos
        cantidadVehiculos += 1
        self.__id = cantidadVehiculos

    #GETTERS Y SETTERS
    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        if(self.__marca == MarcaVehiculosEnum.FORD):
            return 'Ford'
        elif(self.__marca == MarcaVehiculosEnum.PEUGEOT):
            return 'Peugeot'
        else: 
            return 'Volkswagen'
        
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo
        
    def set_dueno(self, dueno):
        self.__dueno = dueno

    def get_dueno(self):
        return self.__dueno
    
    ##DEVNOTE: id del vehiculo es invariante (solo get)
    def get_id(self):
        return self.__id

    ## METODOS DE LA CLASE
    def consultar_proximo_servicio(self):
        kilometros = input('Ingrese cantidad de Km del vehiculo: ')
        while (not kilometros.isdigit()):
            kilometros = input('Ingrese cantidad de Km del vehiculo: ')
        kilometros = int(kilometros)
        proximo_service = math.ceil(kilometros / 10000) * 10000
        print(f'En {proximo_service - kilometros} debera: \n')
        if(proximo_service % 10000 == 0 ):
            print('\t-CAMBIAR ACEITE\n')
            print('\t-CAMBIAR FILTRO DE ACEITE\n')
            print('\t-CAMBIAR FILTRO DE AIRE\n')
            print('\t-CAMBIAR FILTRO DE HABITACULO\n')
            print('\t-VERIFICAR NIVELES DE FLUIDOS\n')
            print('\t-VERIFICACION DE SISTEMAS LUMINICOS\n')
        if(proximo_service % 40000 == 0 ):
            print('\t-CAMBIAR LIQUIDO DE FRENOS\n')
            print('\t-CAMBIAR BUJIAS\n')
        if(proximo_service % 60000 == 0 and (self.__modelo == MarcaVehiculosEnum.PEUGEOT or self.__modelo == MarcaVehiculosEnum.FORD)):
            print('\t-CAMBIAR CORREA DE DISTRIBUCION\n')
            print('\t-CAMBIAR TENSORES\n')
            print('\t-CAMBIAR BOMBA DE AGUA\n')            
        if(proximo_service % 80000 == 0 and self.__modelo == MarcaVehiculosEnum.VOLSKWAGEN):
            print('\t-CAMBIAR BOMBA DE AGUA\n')
            print('\t-VERIFICAR TENSION CADENA DE DISTRIBUCION\n')

