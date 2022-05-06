import csv,numpy as np

from IntegranteProyecto import IntegranteProyecto

class ManejadorIntegrantesProyecto:
    __dimension=0
    __cantidad=0
    __incremento=0
    __integrantesProyecto=None
    def __init__(self,dimension=3,incremento=5):
        self.__integrantesProyecto=np.empty(dimension,dtype=IntegranteProyecto)
        self.__incremento=incremento
        self.__dimension=dimension
        self.__cantidad=0
    def agregarIntegrante(self,integrante):
        if type(integrante)==IntegranteProyecto:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__integrantesProyecto.resize(self.__dimension)
            self.__integrantesProyecto[self.__cantidad]=integrante
            self.__cantidad+=1
        else:
            print('Error, no se pudo agregar un integrante al arreglo, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='integrantesProyecto.csv'
        archivo=open(nombreArchivo)
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                self.agregarIntegrante(IntegranteProyecto(fila[0],fila[1],fila[2],fila[3],fila[4]))
        archivo.close()
        print('Fin de la carga desde: ',nombreArchivo)
    def cantidadIntegrantesProyecto(self,idProyecto):
        resultado=0
        i=0
        bandera=True
        while i<self.__cantidad and bandera:
            if self.__integrantesProyecto[i].verificarId(idProyecto):
                resultado+=1
                if resultado==3:
                    bandera=False
            i+=1
        return resultado
    def comprobarTieneDirector(self,idProyecto):
        resultado=False
        i=0
        bandera=True
        while i<self.__cantidad and bandera:
            if self.__integrantesProyecto[i].verificarId(idProyecto):
                if self.__integrantesProyecto[i].getRol()=='director':
                    bandera=False
                    resultado=True
            i+=1
        return resultado
    def comprobarTieneCoDirector(self,idProyecto):
        resultado=False
        i=0
        bandera=True
        while i<self.__cantidad and bandera:
            if self.__integrantesProyecto[i].verificarId(idProyecto):
                if self.__integrantesProyecto[i].getRol()=='codirector':
                    bandera=False
                    resultado=True
            i+=1
        return resultado
    def comprobarDirectorCategoria(self,idProyecto):
        resultado=False
        i=0
        bandera=True
        while i<self.__cantidad and bandera:
            if self.__integrantesProyecto[i].verificarId(idProyecto):
                if self.__integrantesProyecto[i].getRol()=='director':
                    if self.__integrantesProyecto[i].getCategoria()=='I' or self.__integrantesProyecto[i].getCategoria()=='II':
                        bandera=False
                        resultado=True
            i+=1
        return resultado
    def comprobarCodirectorCategoria(self,idProyecto):
        resultado=False
        i=0
        bandera=True
        while i<self.__cantidad and bandera:
            if self.__integrantesProyecto[i].verificarId(idProyecto):
                if self.__integrantesProyecto[i].getRol()=='codirector':
                    if self.__integrantesProyecto[i].getCategoria()=='I' or self.__integrantesProyecto[i].getCategoria()=='II' or self.__integrantesProyecto[i].getCategoria()=='III':
                        bandera=False
                        resultado=True
            i+=1
        return resultado
    def test(self):
        print('Comienza test ManejadorIntegrantesProyecto')
        manejador=ManejadorIntegrantesProyecto()
        manejador.cargarDesdeArchivo()
        manejador.agregarIntegrante(IntegranteProyecto('21E222','Sanchez Juan','33444444','I','director'))
        print(manejador.comprobarTieneDirector('21E222'))
        print(manejador.comprobarTieneCoDirector('21E222'))
        print(manejador.comprobarDirectorCategoria('21E551'))
        print(manejador.comprobarCodirectorCategoria('21E551'))
        print(manejador.cantidadIntegrantesProyecto('21E222'))   
        print(manejador.cantidadIntegrantesProyecto('21E442'))       
        print('Fin test ManejadorIntegrantesProyecto. \n')