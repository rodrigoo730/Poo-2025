#Rodrgo Pastran 39791772 19456
from colectivo import Colectivo
from manejaColectivos import ManejaColectivo
from manejaTramos import ManejaTramos
if __name__=='__main__':

    def menu():
        bandera=True
        while bandera:
            op=input('ingrese la opcion a, b , c, d=salir : ')
            if op =='a':
                dni=int(input('ingrese dni de chofer: '))
                patente=manejaC.buscarDni(dni)
                manejaT.mostrarPorPatente(patente)
            elif op=='b':
                manejaC.mostrarPorPatente(manejaT)
            elif op=='c':
                km=int(input('ingrese distancia a comparar: '))
                manejaT.listarKm(km)
                pass
            elif op=='d':
                bandera=False

    manejaT=ManejaTramos()
    manejaT.cargar()
    #manejaT.mostrar()
    dim=int(input('ingrese dimension de arreglo: '))
    
    manejaC=ManejaColectivo(dim)
    manejaC.cargar()
    #manejaC.mostrar()
    menu()