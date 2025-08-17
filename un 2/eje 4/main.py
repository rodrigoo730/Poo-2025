from test import test
from manejadorCarrera import ManejadorCarre
from manejadorFacultad import ManejadorFacu
if __name__=='__main__':

    def menu():
        bandera=False
        while not bandera:
            print('1:mostrar facultad a la que pertenece una carrera \n2:mostrar cantidad de carreras por facultad ' 
                '\n3: mostrar carreras de una facultad \n5: salir')
            opcion=int(input('ingrese opcion: '))
            if opcion==1:
                nombre=input('ingrese nombre de carrera: ')
                indice=manejadorCarrera.buscar(nombre)
                nomFacu=manejadorFacultad.mostrarFacu(indice)
                print('pertenece a la {}'.format(nomFacu))
                #mes=int(input('ingrese numero de mes: '))
            elif opcion==2:
                manejadorFacultad.mostrarPorFacu(manejadorCarrera)
                #mes=int(input('ingrese numero de mes: '))
            elif opcion==3:
                nombre=input('ingrese nombre de facultad: ')
                id=manejadorFacultad.buscarFacu(nombre)
                print('paso ',id)
                if id !=0:
                    manejadorCarrera.ordenar()
                    manejadorCarrera.mostrarCarreras(id)
                else:print('no se encontro facultad')
            elif opcion==5:
                bandera=True

    print('hola')
    manejadorCarrera,manejadorFacultad=test()
    menu()
    