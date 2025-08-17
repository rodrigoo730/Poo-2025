from manejaAtencion import MAtenencion
from manejaPaciente import MPaciente
from maneNumpy import Maneja

if __name__=='__main__':

    def menu():
        bandera=True
        while bandera:
            op=input('ingrese opcion a, b, c, d: ')
            if op=='a':
                fecha=input('ingrese fecha: ')
                importe=MA.buscarAtencion(fecha)
                print('el importe es {}'.format(importe))
            elif op == 'b':
                dni=int(input('ingrese dni: '))
                MP.buscarPaciente(dni,MA)
            
            elif op == 'c':
                 MP.mostrarSin(MA)

            elif op == 'd':
                MP.ordenar()
                MP.mostrar()

    numpy=Maneja(30)
    numpy.cargar()
    numpy.mostrar()

    #MA=MAtenencion(50)
    #MA.cargar()
    #MA.mostrar()
    #MP=MPaciente()
    #MP.cargar()
    #MP.mostrar()
    #menu()
