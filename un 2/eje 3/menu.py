

def menu(manejador,accidente):
    bandera=False
    while not bandera:
        print('1:Accidente de departamentos por mes \n2:depto con maximo de accidentes por un mes ' 
             '\n3: total de accidente de un depto \n4:mostrar total tabla \n5: salir')
        opcion=int(input('ingrese opcion: '))
        if opcion==1:
            mes=int(input('ingrese numero de mes: '))
            manejador.mostrarMes(accidente,mes)
        elif opcion==2:
            mes=int(input('ingrese numero de mes: '))
            manejador.mostrarMax(accidente,mes)
        elif opcion==3:
            nombre=input('ingrese nombre de departamento: ')
            manejador.buscar(accidente,nombre)
        elif opcion==4:
            manejador.mostrarTabla(accidente)
        elif opcion==5:
            bandera=True
        