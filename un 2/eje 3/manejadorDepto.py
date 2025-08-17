import csv
from departamento import departamento
from accidente import accidente
class manejadorDepto:
    __deptos=list

    def __init__(self):
        self.__deptos=[]

    def cargar(self):
        archivo= open('Departamentos.csv')
        reader= csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                depto=departamento(fila[0],fila[1])
                self.__deptos.append(depto)
        archivo.close

    def mostrarMes(self,accidentes,mes):
        for depto in self.__deptos:
            print(' {}, total accidentes: {}'.format(depto.getNombre(),accidentes.getAccte(int(depto.getIdent())-1,mes-1)))

    def mostrarMax(self,accidentes,mes):
        max=0
        for depto in self.__deptos:
            if accidentes.getAccte(depto.getIdent()-1,mes-1) >max:
                max=accidentes.getAccte(depto.getIdent()-1,mes-1)
                nombre=depto.getNombre()
        print('{} tiene mayor cantidad de accidentes: {}'.format(nombre,max))

    def buscar(self,accidentes,depto):
        i=0
        encontrado=False
        while i<len(self.__deptos) and not encontrado:
            if depto==self.__deptos[i].getNombre():
                iden=self.__deptos[i].getIdent()-1
                encontrado=True
                print('se encontro')
            i+=1
        contador=0
        for j in range(3):
            print('accidente: {}'.format(accidentes.getAccte(iden,j)))
            contador+=accidentes.getAccte(iden,j)
        print('la total de accidentes por anio del depto es {}'.format(contador))

    def mostrarTabla(self,accidentes):
        print('Departamento  1   2   3   4   5   6   7   8   9   10   11   12')
        for i in range(19):
            print('{}'.format(self.__deptos[i].getNombre()),end='')
            for j in range(12):
                print(' {}  '.format(accidentes.getAccte(i,j)),end='')
            print('\n')
