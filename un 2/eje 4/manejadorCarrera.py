import numpy as np
import csv
from carrera import carrera
#from manejadorFacultad import ManejadorFacu

class ManejadorCarre:
    __cantidad:int
    __dimension=int
    __incremento=int
    __carreras=type

    def __init__(self,dimension=0,incremento=5):
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
        self.__carreras=np.empty(dimension,dtype=carrera)

    def agregar(self,carrera):
        #print(self.__cantidad,self.__dimension)
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            #print(carrera.getNombre(),self.__dimension)
            self.__carreras.resize(self.__dimension)
        self.__carreras[self.__cantidad]=carrera
        self.__cantidad+=1
    
    def cargar(self):
        archivo=open('Carreras.csv')
        reader=csv.reader(archivo,delimiter=';')
        saltar=True
        for fila in reader:
            if saltar:
                saltar=False
            else:
                nuevaCarrera=carrera(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.agregar(nuevaCarrera)
        archivo.close

    def ordenar(self):
        self.__carreras.sort()

    def mostrarCarreras(self,id):
        for i in range(self.__cantidad):
            #print(type(self.__carreras[i].getCodFacu()),type(id))
            if self.__carreras[i].getCodFacu() == id:
                print('carrera {} duracion {}'.format(self.__carreras[i].getNombre(),self.__carreras[i].getDuracion()))
        
    def cantidadPorFacu(self,cod):
        contador=0
        for i in range(self.__cantidad):
            if int(self.__carreras[i].getCodFacu()) == cod:
                contador+=1
        return contador
    '''
    def mostrarPorFacu(self,manejadorF):
        contador=0
        codFacu=1
        #print(type(codFacu))
        for carrera in self.__carreras:
            print(carrera.getNombre(),carrera.getCodFacu(),codFacu)
            #print(type(carrera.getCodFacu()))
            if (int(carrera.getCodFacu())==codFacu):
                print('entro')
                contador+=1
            else:
                print('la {} tiene {} carreras'.format(manejadorF.getFacu(codFacu-1),contador))
                contador=0
                codFacu+=1
    '''

    def buscar(self,nom):
        i=0
        encontrado=False
        while i< self.__cantidad and not encontrado:
            if nom==self.__carreras[i].getNombre():
                indice=self.__carreras[i].getCodFacu()
                encontrado=True
            i+=1
        return indice

