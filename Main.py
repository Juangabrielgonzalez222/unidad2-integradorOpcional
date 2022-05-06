from ManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto
from ManejadorProyecto import ManejadorProyecto
from Menu import Menu

if __name__== '__main__':
    manejadorProyecto=ManejadorProyecto()
    manejadorIntegrantes=ManejadorIntegrantesProyecto()
    manejadorProyecto.cargarDesdeArchivo()
    manejadorIntegrantes.cargarDesdeArchivo()
    menu=Menu()
    menu.lanzarMenu(manejadorProyecto,manejadorIntegrantes)
