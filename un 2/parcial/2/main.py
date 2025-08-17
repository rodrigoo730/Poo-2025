from movilidad import Movilidad
from manejaM import manejaMo
from manejaG import ManejaGastos



if __name__=='__main__':

    def menu():
        bandera=True
        while bandera:
            op=input('ingrese opcion a, b, c ,d=salir: ')
            if op == 'a':
                patente= input('ingrese patente: ')
                manejaM.buscarPatente(patente,manejaG)
            elif op == 'b':
                fecha=input('ingrese fecha: ')
                manejaG.buscarFecha(fecha,manejaM)
            elif op == 'c':
                manejaG.ordenar()
                manejaG.mostrar()
                fecha=input('ingrese fecha: ')
                manejaG.buscarFecha(fecha,manejaM)
            elif op == 'd':
                bandera=False


    manejaM=manejaMo(5)
    manejaM.cargar()
    manejaM.mostrar()
    manejaG=ManejaGastos()
    manejaG.cargar()
    manejaG.mostrar()
    menu()
    
    


    