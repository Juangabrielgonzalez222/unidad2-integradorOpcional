class Proyecto:
    __idProyecto=''
    __titulo=''
    __palabrasClave=''
    __puntaje=0
    def __init__(self,idProyecto='',titulo='',palabrasClave='',puntaje=0):
        self.__idProyecto=idProyecto
        self.__titulo=titulo
        self.__palabrasClave=palabrasClave
        self.__puntaje=puntaje
    def setPuntaje(self,puntaje):
        self.__puntaje=puntaje
    def getPuntaje(self):
        return self.__puntaje
    def getId(self):
        return self.__idProyecto
    def __str__(self):
        return 'ID:{}, Titulo:{} PalabrasClave:{} Puntaje:{}'.format(self.__idProyecto,self.__titulo,self.__palabrasClave,self.__puntaje)
    def __gt__(self,otroProyecto):
        return self.__puntaje>otroProyecto.getPuntaje()
    def test(self):
        print('Comienza test Proyecto')
        proyecto=Proyecto('21E222','Proyecto de testeo','Test Proyecto')
        proyecto2=Proyecto('21E333','Proyecto de testeo2','Test Proyecto2')
        print(proyecto.getId())
        proyecto.setPuntaje(25)
        print(proyecto.getPuntaje())
        print(proyecto)
        proyecto2.setPuntaje(10)
        print(proyecto>proyecto2)
        print('Fin test Proyecto. \n')