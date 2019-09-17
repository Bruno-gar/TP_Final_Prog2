
#! /usr/bin/env python3
from usuario import Usuario
from vehiculo import Vehiculo
from tipousuariosenum import TipoUsuariosEnum
from marcavehiculosenum import MarcaVehiculosEnum
import sys

class Menu:
    '''Mostrar un menu y responder a las opciones'''
    def __init__(self):
        self.usuarios = []
        self.vehiculos = []
        # SUPONEMOS QUE HAY TRES USUARIOS PRE-CARGADOS
        self.usuarios.append(Usuario('Juan', 'Perez', 1, 'meca', TipoUsuariosEnum.MECANICO))
        self.usuarios.append(Usuario('Esteban', 'Quito', 2, 'client', TipoUsuariosEnum.CLIENTE))
        self.usuarios.append(Usuario('Juan', 'Perez', 3, 'dios', TipoUsuariosEnum.ADMINISTRADOR))
        self.opciones_cliente= {
            "1": self.cargar_vehiculo,
            "2": self.consultar_service,
            "3": self.listar_vehiculos_cliente,
            "4": self.salir
        }

    def mostrar_menu_cliente(self):
        print("""
                Menú del Cliente:
                1. Cargar Vehiculo
                2. Consultar Service
                3. Ver mis vehiculos
                4. Salir
                """)

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            # reemplazar linea por 'login'...
            self.usuario_logueado = self.usuarios[1]
            print(f'Bienvenido {self.usuario_logueado.getnombre()}')
            self.mostrar_menu_cliente()
            opcion = input("Ingresar una opcion: ")
            accion = self.opciones_cliente.get(opcion)
            if accion:
                accion()
            else:
                print(f'{opcion} no es una opcion valida')

    def cargar_vehiculo(self):
        marca = input("""
            Seleccione la marca de su coche:
            [1] Peugeot
            [2] Volkswagen
            [3] Ford
            """)
        while not marca.isdigit() and not(marca == MarcaVehiculosEnum.VOLSKWAGEN or marca == MarcaVehiculosEnum.PEUGEOT or marca == MarcaVehiculosEnum.FORD):
            marca = input("""
                Seleccione la marca de su coche:
                [1] Peugeot
                [2] Volkswagen
                [3] Ford
                """)
        marca = MarcaVehiculosEnum(int(marca))
        modelo = input('Ingrese el modelo de su coche (p.e: Focus): ')
        nuevo_auto = Vehiculo(marca, modelo, self.usuario_logueado)
        self.vehiculos.append(nuevo_auto)
        print(f'ID: {nuevo_auto.get_id()}')
    
    def listar_vehiculos_cliente(self):
        for vehiculo in self.vehiculos:
            if(vehiculo.get_dueno() == self.usuario_logueado):
                print(f'ID: {vehiculo.get_id()}\n MARCA/MODELO: {vehiculo.get_marca()} {vehiculo.get_modelo()}')
    
    def consultar_service(self):
        id = input("Ingresar el id de su coche: ")
        while (not id.isdigit()):
            id = input("Ingresar el id de su coche: ")
        id = int(id)
        existe = False
        for vehiculo in self.vehiculos:
            if (vehiculo.get_id() == id and vehiculo.get_dueno() == self.usuario_logueado): 
                existe = True
                vehiculo.consultar_proximo_servicio()
            if (not existe):
                print('No se encontro un coche a su nombre con ese id')
        


    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

#Esta parte del cÃƒÂ³digo estÃƒÂ¡ fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro mÃƒÂ³dulo, sino ejecutado directamente), entonces llamamos al mÃƒÂ©todo
# ejecutar().
if __name__ == "__main__":
    Menu().ejecutar()
