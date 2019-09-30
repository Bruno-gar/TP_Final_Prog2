
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
        self.opciones_cliente = {
            "1": self.cargar_vehiculo_cliente,
            "2": self.consultar_service_cliente,
            "3": self.listar_vehiculos_cliente,
            "4": self.salir
        }
        self.opciones_admin = {
            "0": self.consultar_service,
            "1": self.listar_vehiculos,
            # "2": self.cargar_vehiculo_cliente,
            "3": self.cargar_vehiculo,
            "4": self.borrar_vehiculo,
            "5": self.listar_usuarios,
            "6": self.modificar_cliente,
            "7": self.agregar_usuario,
            # "8": self.listar_vehiculos_cliente,
            "9": self.salir
        }

    def mostrar_menu_cliente(self):
        print("""
                Menú del Cliente:
                1. Cargar Vehiculo
                2. Consultar Service
                3. Ver mis vehiculos
                4. Salir
                """)

    def mostrar_menu_admin(self):
        print("""
            Menú del Administrador:
            0. Consultar Service
            1. Listar Vehiculos
            2. Modificar Vehiculo
            3. Agregar Vehiculo
            4. Borrar Vehiculo
            5. Listar Usuarios
            6. Modificar Usuarios
            7. Agregar Usuarios
            8. Borrar Usuarios
            9. Salir
            """)

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            # reemplazar linea por 'login'...
            print("""Seleccione su tipo de usuario: 
                    [1]: Mecanico
                    [2]: Cliente
                    [3]: Admin
                    [4]: Salir""")
            modo = input('Seleccione una opcion: ')
            while not modo.isdigit():
                print("""Seleccione su tipo de usuario: 
                    [1]: Mecanico
                    [2]: Cliente
                    [3]: Admin
                    [4]: Salir""")
                modo = input('Seleccione una opcion: ')
            modo = int(modo)
            if (modo == 1):
                # self.usuario_logueado = self.usuarios[0]
                # print(f'Bienvenido {self.usuario_logueado.getnombre()}')
                # self.mostrar_menu_mecanico()
                # opcion = input("Ingresar una opcion: ")
                # accion = self.opciones_mecanico.get(opcion)
                print('No implementado, cdtm!')
            elif (modo == 2):
                self.usuario_logueado = self.usuarios[1]
                print(f'Bienvenido {self.usuario_logueado.getnombre()}')
                self.mostrar_menu_cliente()
                opcion = input("Ingresar una opcion: ")
                accion = self.opciones_cliente.get(opcion)
            elif (modo == 3):
                self.usuario_logueado = self.usuarios[2]
                print(f'Bienvenido {self.usuario_logueado.getnombre()}')
                self.mostrar_menu_admin()
                opcion = input("Ingresar una opcion: ")
                accion = self.opciones_admin.get(opcion)
            else:
                self.salir()
            if accion:
                accion()
            else:
                print(f'{opcion} no es una opcion valida')

    def cargar_vehiculo_cliente(self):
        marca = input("""
            Seleccione la marca de su coche:
            [1] Peugeot
            [2] Volkswagen
            [3] Ford
            """)
        while not marca.isdigit() or not(int(marca) == MarcaVehiculosEnum.VOLSKWAGEN.value or int(marca) == MarcaVehiculosEnum.PEUGEOT.value or int(marca) == MarcaVehiculosEnum.FORD.value):
            marca = input("""
                Seleccione la marca de su coche:
                [1] Peugeot
                [2] Volkswagen
                [3] Ford
                """)
        marca = MarcaVehiculosEnum(int(marca))
        modelo = input('Ingrese el modelo de su coche (p.e: Focus): ')
        nuevo_auto = Vehiculo(marca, modelo, self.usuario_logueado, True)
        self.vehiculos.append(nuevo_auto)
        print('El coche se ha agregado')
        print(f'ID: {nuevo_auto.get_id()}')

    def cargar_vehiculo(self):
        marca = input("""
            Seleccione la marca de su coche:
            [1] Peugeot
            [2] Volkswagen
            [3] Ford
            """)
        while not marca.isdigit() or not(int(marca) == MarcaVehiculosEnum.VOLSKWAGEN.value or int(marca) == MarcaVehiculosEnum.PEUGEOT.value or int(marca) == MarcaVehiculosEnum.FORD.value):
            marca = input("""
                Seleccione la marca de su coche:
                [1] Peugeot
                [2] Volkswagen
                [3] Ford
                """)
        marca = MarcaVehiculosEnum(int(marca))
        modelo = input('Ingrese el modelo de su coche (p.e: Focus): ')
        cliente = input("Ingrese el ID de cliente: ")
        while not cliente.isdigit():
            cliente = input("Ingrese el DNI de cliente: ")
        cliente = int(cliente)
        encontrado = False
        while not encontrado:
            for usuario in self.usuarios:
                if (cliente == usuario.getdni()):
                    nuevo_auto = Vehiculo(marca, modelo, usuario, True)
                    self.vehiculos.append(nuevo_auto)
                    print('El coche se ha agregado')
                    print(f'ID: {nuevo_auto.get_id()}')
                    encontrado = True
            if not encontrado:
                print('No se encontro el DNI. Intente nuevamente')
                cliente = input("Ingrese el ID de cliente")
                while not cliente.isdigit():
                    cliente = input("Ingrese el DNI de cliente")
                cliente = int(cliente)

    
    def listar_vehiculos_cliente(self):
        for vehiculo in self.vehiculos:
            if(vehiculo.get_dueno() == self.usuario_logueado and vehiculo.get_activo()):
                print(f'ID: {vehiculo.get_id()}\n MARCA/MODELO: {vehiculo.get_marca()} {vehiculo.get_modelo()}')
    
    def consultar_service_cliente(self):
        id = input("Ingresar el id de su coche: ")
        while (not id.isdigit()):
            id = input("Ingresar el id de su coche: ")
        id = int(id)
        existe = False
        for vehiculo in self.vehiculos:
            if (vehiculo.get_id() == id and vehiculo.get_activo() and vehiculo.get_dueno() == self.usuario_logueado): 
                existe = True
                vehiculo.consultar_proximo_servicio()
            if (not existe):
                print('No se encontro un coche activo a su nombre con ese id')

    def consultar_service(self):
            id = input("Ingresar el id del coche: ")
            while (not id.isdigit()):
                id = input("Ingresar el id del coche: ")
            id = int(id)
            existe = False
            for vehiculo in self.vehiculos:
                if (vehiculo.get_id() == id and vehiculo.get_activo()): 
                    existe = True
                    dueno = vehiculo.get_dueno()
                    print(f'Dueño: {dueno.getnombre} {dueno.getapellido}')
                    vehiculo.consultar_proximo_servicio()
                if (not existe):
                    print('No se encontro un coche activo de ese usuario con ese id')
    
    def listar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(f'Dueno: {vehiculo.get_dueno().getnombre()} {vehiculo.get_dueno().getapellido()} / Coche: {vehiculo.get_marca()} {vehiculo.get_modelo()}')
            print(f'Estado: {vehiculo.get_activo()}')

    def borrar_vehiculo(self):
        id = input("Ingresar el id del coche: ")
        while (not id.isdigit()):
            id = input("Ingresar el id del coche: ")
        id = int(id)
        existe = False
        for vehiculo in self.vehiculos:
            if (vehiculo.get_id() == id and vehiculo.get_activo()): 
                existe = True
                vehiculo.set_activo(False)
                print(f'Vehiculo {id} eliminado exitosamente')
            if (not existe):
                print('No se encontro un coche activo con ese id')

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f'Nombre: {usuario.getnombre()} {usuario.getapellido()} DNI: {usuario.getdni()} TIPO: {usuario.gettipo()}')

    def modificar_cliente (self):
        cliente = input("Ingresar el id del cliente a modificar: ")
        encontrado = False       
        while (not cliente.isdigit()):
            cliente = input("Ingresar el id del cliente a modificar: ")
        cliente = int(cliente)
        while not encontrado:
            for usuario in self.usuarios:
                if (cliente == usuario.getdni()):
                    usuario.setnombre(input ('Ingrese el nuevo nombre: '))
                    usuario.setapellido(input ('Ingrese el nuevo apellido: '))
                    print(f'Usuario {cliente} modificado exitosamente.')
                    encontrado = True
            if not encontrado:
                print('No se encontro el DNI. Intente nuevamente')
                cliente = input("Ingrese el ID de cliente a modificar: ")
                while not cliente.isdigit():
                    cliente = input("Ingrese el DNI de cliente a modificar: ")
                cliente = int(cliente)

    def agregar_usuario(self):
        tipo = input("""
            Seleccione tipo de usuario:
            [1] Mecanico
            [2] Cliente
            [3] Admin
            """)

        while not tipo.isdigit() or not (int(tipo) == TipoUsuariosEnum.ADMINISTRADOR.value or int(tipo) == TipoUsuariosEnum.CLIENTE.value or int(tipo) == TipoUsuariosEnum.MECANICO.value):
            tipo = input("""
            Seleccione tipo de usuario:
            [1] Mecanico
            [2] Cliente
            [3] Admin
            """)
        tipo = TipoUsuariosEnum(int(tipo))
        nombre = input('Ingrese nombre del usurio: ')
        apellido = input('Ingrese apellido del usurio: ')
        contrasena = input('Ingrese contraseña del usurio: ')
        dni = input('Ingrese dni del usurio: ')
        while not dni.isdigit():
            dni = input('Ingrese dni del usurio: ')
        dni = int(dni)
        self.usuarios.remove(Usuario(nombre, apellido, dni, contrasena, tipo))
        print('Usuario agregado exitosamente!')
        self.listar_usuarios()



    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

#Esta parte del cÃƒÂ³digo estÃƒÂ¡ fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro mÃƒÂ³dulo, sino ejecutado directamente), entonces llamamos al mÃƒÂ©todo
# ejecutar().
if __name__ == "__main__":
    Menu().ejecutar()
