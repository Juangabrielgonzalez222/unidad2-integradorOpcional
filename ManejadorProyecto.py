import csv

from Proyecto import Proyecto

class ManejadorProyecto:
    __listaProyectos=[]
    def __init__(self):
        self.__listaProyectos=[]
    def agregarProyecto(self,proyecto):
        if type(proyecto)==Proyecto:
            self.__listaProyectos.append(proyecto)
        else:
            print('Error, no se pudo agregar un proyecto a la lista, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='proyectos.csv'
        archivo=open(nombreArchivo)
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                self.agregarProyecto(Proyecto(fila[0],fila[1],fila[2]))
        archivo.close()
    def calcularPuntosProyectos(self,manejadorIntegrante):
        for proyecto in self.__listaProyectos:
            puntaje=0
            tieneDirector=True
            tieneCoDirector=True
            if manejadorIntegrante.cantidadIntegrantesProyecto(proyecto.getId())==3:
                puntaje+=10
            else:
                puntaje-=20
                print('El Proyecto {} debe tener como mínimo 3 integrantes'.format(proyecto.getId()))
            if not manejadorIntegrante.comprobarTieneDirector(proyecto.getId()):
                print('El Proyecto {} debe tener un Director'.format(proyecto.getId()))
                tieneDirector=False
            if tieneDirector and manejadorIntegrante.comprobarDirectorCategoria(proyecto.getId()):
                puntaje+=10
            else:
                puntaje-=5
                print('El Director del Proyecto {} debe tener categoría I o II'.format(proyecto.getId()))
            if not manejadorIntegrante.comprobarTieneCoDirector(proyecto.getId()):
                print('El Proyecto {} debe tener un Codirector'.format(proyecto.getId()))
                tieneCoDirector=False
            if tieneCoDirector and manejadorIntegrante.comprobarCodirectorCategoria(proyecto.getId()):
                puntaje+=10
            else:
                puntaje-=5
                print('El Codirector del Proyecto  {} debe tener como mínimo categoría III'.format(proyecto.getId()))
            if not tieneCoDirector or not tieneDirector:
                puntaje-=10
            proyecto.setPuntaje(puntaje)
    def mostrarProyectosOrdenadosPuntaje(self,manejadorIntegrantes):
        self.calcularPuntosProyectos(manejadorIntegrantes)
        self.ordenarMayorAMenor()
        for proyecto in self.__listaProyectos:
            print(proyecto)
    def ordenarMayorAMenor(self):
        if len(self.__listaProyectos)>1:
            nuevaLista=[]
            nuevaLista.append(self.__listaProyectos[0])
            for i in range(1,len(self.__listaProyectos)):
                j=0
                if self.__listaProyectos[i]>nuevaLista[j]:
                    nuevaLista.insert(j,self.__listaProyectos[i])
                elif nuevaLista[-1] > self.__listaProyectos[i]:
                    nuevaLista.append(self.__listaProyectos[i])
                else:
                    j+=1
                    longitudNuevaLista=len(nuevaLista)
                    longitudNuevaLista-=1
                    bandera=True
                    while j<longitudNuevaLista and bandera:
                        if nuevaLista[j]>self.__listaProyectos[i]:
                            j+=1
                        else:
                            bandera=False
                    nuevaLista.insert(j,self.__listaProyectos[i])
            self.__listaProyectos=nuevaLista
    def test(self,manejadorIntegrantes):
        print('Comienza test ManejadorProyecto')
        manejadorProyecto=ManejadorProyecto()
        manejadorProyecto.cargarDesdeArchivo()
        print('Metodo agregarProyecto()')
        manejadorProyecto.agregarProyecto(Proyecto('21E222','Proyecto de testeo','Test Proyecto'))
        print('Metodo calcularPuntosProyectos()')
        manejadorProyecto.calcularPuntosProyectos(manejadorIntegrantes)
        print('Metodo mostrarProyectosOrdenadosPuntaje()')
        manejadorProyecto.mostrarProyectosOrdenadosPuntaje(manejadorIntegrantes)
        print('Fin test ManejadorProyecto. \n')