from manejadorCarrera import ManejadorCarre
from manejadorFacultad import ManejadorFacu

def test():
    manejadorCarrera=ManejadorCarre(40,5)
    manejadorCarrera.cargar()
    #manejadorCarrera.mostrar()
    manejadorFacultad=ManejadorFacu(7,3)
    manejadorFacultad.cargar()
    #manejadorFacultad.mostrar()
    

    return manejadorCarrera, manejadorFacultad