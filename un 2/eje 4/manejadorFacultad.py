from facultad import facultad
from manejadorCarrera import ManejadorCarre
import numpy as np
import csv
class ManejadorFacu:
    __cantidad:int
    __dimension=int
    __incremento=int
    __facultades=type

    def __init__(self,dimension=0,incremento=5):
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
        self.__facultades=np.empty(dimension,dtype=facultad)

    def agregar(self,facultad):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__facultades.resize(self.__dimension)
        self.__facultades[self.__cantidad]=facultad
        self.__cantidad+=1
    
    def cargar(self):
        archivo=open('Facultades.csv')
        reader=csv.reader(archivo,delimiter=';')
        saltar=True
        for fila in reader:
            if saltar:
                saltar=False
            else:
                nuevaFacu=facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregar(nuevaFacu)
        archivo.close

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__facultades[i].getNombre())

    def getFacu(self,indice):
        return self.__facultades[indice].getNombre()
    
    def mostrarPorFacu(self,manejaCarr):
        for i in range(self.__cantidad):
            print('la {} tiene {} carreras'.format(self.__facultades[i].getNombre(), manejaCarr.cantidadPorFacu(i+1)))


    def mostrarFacu(self,cod):
        i=0
        encontrado=False
        while i< self.__cantidad and not encontrado:
            if cod == self.__facultades[i].getCod():
                encontrado=True
                nombre=self.__facultades[i].getNombre()
            i+=1
        return nombre
    
    def buscarFacu(self,nom):
        i=0
        id=0
        encontrado=False
        while i< self.__cantidad and not encontrado:
            if nom == self.__facultades[i].getNombre():
                encontrado=True
                id=self.__facultades[i].getCod()
            i+=1
        return id