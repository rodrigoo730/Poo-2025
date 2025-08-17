import numpy as np
from atencion import atencion
import csv
class MAtenencion:
    __incremento=int
    __dimension=int
    __cantidad:int
    __atenciones=np.ndarray

    def __init__(self,dimension=0):
        self.__incremento=5
        self.__dimension=dimension
        self.__atenciones=np.empty(dimension,dtype=atencion)
        self.__cantidad=0

    def cargar(self):
       
        archivo=open('atenciones.csv')
        reader=csv.reader(archivo,delimiter=';')
        saltar=True
        for fila in reader:
            if saltar:
                saltar=False
            else:
                
                atecion=atencion(fila[0],fila[1],float(fila[2]))
                self.agregar(atecion)

    def agregar(self,atencio):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__atenciones.resize(self.__dimension)
        else:
            self.__atenciones[self.__cantidad]=atencio
            self.__cantidad+=1

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__atenciones[i].getDni())

    def buscarAtencion(self,fecha):
        importe=0
        for i in range(self.__cantidad):
            if fecha == self.__atenciones[i].getFecha():
                print('dni de la atencion igual {}'.format(self.__atenciones[i].getDni()))
                importe+=self.__atenciones[i].getImporte()
        return importe
    

    def buscarPorPac(self,dni):
        cant=0
        for i in range(self.__cantidad):
            if self.__atenciones[i].getDni() == dni:
                print('paso cont')
                cant+=1
        return cant
    
    def buscarDni(self,dni):
        encontrado=False
        i=0
        while i<self.__cantidad and not encontrado:  
            #print(type(dni),' ',type(self.__atenciones[i].getDni()))
            if dni == self.__atenciones[i].getDni():
                encontrado=True
            i+=1
        return encontrado
    
    