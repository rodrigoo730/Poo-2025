#Rodrgo Pastran 39791772 19456
import numpy as np
from colectivo import Colectivo
import csv

class ManejaColectivo:
    __dimesion:int
    __cantidad:int
    __incremento:int
    __colectivos=np.ndarray

    def __init__(self,dimension=0):
        self.__cantidad=0
        self.__dimesion=dimension
        self.__incremento=5
        self.__colectivos=np.empty(dimension,dtype=Colectivo)

    def cargar(self):
        archivo=open('colectivos.csv')
        reader=csv.reader(archivo,delimiter=';')
        saltar=True
        for fila in reader:
            if saltar:
                saltar=False
            else:
                colectivo=Colectivo(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregar(colectivo)

        archivo.close

    def agregar(self,colectivo):
        if self.__cantidad == self.__dimesion:
            self.__dimesion+=self.__incremento
            self.__colectivos=np.resize(self.__colectivos,self.__dimesion)
        self.__colectivos[self.__cantidad]=colectivo
        self.__cantidad+=1

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__colectivos[i].getPatente())

    def buscarDni(self,dni):
        i=0
        encontrado=False
        while i<self.__cantidad and not encontrado:
            if dni == int(self.__colectivos[i].getDniCho()):
                encontrado=True
                patente=self.__colectivos[i].getPatente()
            i+=1
        return patente
    
    def mostrarPorPatente(self,manejaT):
        for i in range(self.__cantidad):
            print('colectivo patente: {}'.format(self.__colectivos[i].getPatente()))
            patente=self.__colectivos[i].getPatente()
            manejaT.mostrarKmTotal(patente,Colectivo.getConsumo())
        pass
 