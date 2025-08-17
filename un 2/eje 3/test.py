from manejadorDepto import manejadorDepto
from accidente import accidente

def test():
    manejador=manejadorDepto()
    manejador.cargar()
    accite=accidente()
    accite.inicializar()
    
    i=int(input('ingrese cantidad de accidentes a registrar: '))
    while i>0:
        nroDepto=int(input('ingrese numero de departamento: '))
        nroMes=int((input('ingrese numero de mes: ')))
        accidentes=int(input('ingrese numero de accidentes: '))
        accite.cargar(nroDepto,nroMes,accidentes)
        i-=1
    accite.mostra()
    return manejador,accite

    