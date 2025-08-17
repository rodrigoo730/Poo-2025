from manejaBeca import ManejaBeca
from manejaBeneficiario import ManejaBeneficiario
from test import test

if __name__=='__main__':
    manejaBeca,manejaBeneficiario=test()
    
    bandera=True
    while bandera:
        print('---Menu----')
        print('a. \nb. \nc. \nd. \ne.salir')
        op=input('Ingrese opcion: ')
        if op == 'a':
            beca=input('ingrese tipo de beca: ')
            manejaBeca.buscar(beca,manejaBeneficiario)
        elif op=='b':
            dni=int(input('ingrese dni: '))
            manejaBeneficiario.mostrarDni(dni)

        elif op=='c':
            manejaBeneficiario.ordenar()
            manejaBeneficiario.mostrar()

        elif op=='d':
            manejaBeneficiario.mostrarPorProm()

        elif op=='e':
            print('salir')
            bandera=False