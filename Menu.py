from IntegranteProyecto import IntegranteProyecto
from ManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto
from ManejadorProyecto import ManejadorProyecto
from Proyecto import Proyecto

class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.test,
            '3':self.salir
        }
    def lanzarMenu(self,manejadorProyecto,manejadorIntegrantes):
        #Menu opciones
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para listar los datos de los Proyectos ordenados por puntaje.')
            print('-Ingrese 2 para ejecutar test.')
            print('-Ingrese 3 para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion=='1':
                ejecutar(manejadorProyecto,manejadorIntegrantes)
            else:
                ejecutar()
    def opcion1(self,manejadorProyecto,manejadorIntegrantes):
        manejadorProyecto.mostrarProyectosOrdenadosPuntaje(manejadorIntegrantes)
    def test(self):
        proyecto=Proyecto('21E222','Proyecto de testeo','Test Proyecto')
        integrante=IntegranteProyecto('21E222','Sanchez Juan','33444444','I','director')
        proyecto.test()
        integrante.test()
        manejadorIntegrantes=ManejadorIntegrantesProyecto()
        manejadorProyecto=ManejadorProyecto()
        manejadorIntegrantes.test()
        manejadorIntegrantes.cargarDesdeArchivo()
        manejadorIntegrantes.agregarIntegrante(integrante)
        manejadorProyecto.test(manejadorIntegrantes)
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')