class IntegranteProyecto:
    __idProyecto=''
    __apellidoNombre=''
    __dni=''
    __categoriaInvestigacion=''
    __rol='' 
    def __init__(self,idProyecto='',apellidoNombre='',dni='',categoriaInvestigacion='',rol=''):
        self.__idProyecto=idProyecto
        self.__apellidoNombre=apellidoNombre
        self.__dni=dni
        self.__categoriaInvestigacion=categoriaInvestigacion
        self.__rol=rol
    def verificarId(self,id):
        return self.__idProyecto==id
    def getRol(self):
        return self.__rol
    def getCategoria(self):
        return self.__categoriaInvestigacion
    def test(self):
        print('Comienza test IntegranteProyecto')
        integrante=IntegranteProyecto('21E222','Sanchez Juan','33444444','I','director')
        print(integrante.verificarId('21E222'))
        print('Rol:{} Categoria:{}'.format(integrante.getRol(),integrante.getCategoria()))
        print('Fin test IntegranteProyecto. \n')