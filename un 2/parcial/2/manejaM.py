from movilidad import Movilidad
import numpy as np
import csv

class manejaMo:
    __dimencion:int
    __cantidad:int
    __incremento:int
    __movilidades:np.ndarray

    def __init__(self,dimen=0):
        self.__dimencion=dimen
        self.__cantidad=0
        self.__incremento=5
        self.__movilidades=np.empty(dimen,dtype=Movilidad)

    def agregar(self,movil):
        if self.__cantidad == self.__dimencion:
            self.__dimencion+=self.__incremento
            self.__movilidades=np.resize(self.__movilidades,self.__dimencion)
        self.__movilidades[self.__cantidad]=movil
        self.__cantidad+=1

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__movilidades[i])



    def cargar(self):
        archivo=open('movilidades.csv')
        reader=csv.reader(archivo,delimiter=';')
        saltar=True
        for fila in reader:
            if saltar:
                saltar=False    
            else:
                movil=Movilidad(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.agregar(movil)
        archivo.close

    def buscarPatente(self,patente,manejadorG):
        i=0
        encontrado=False
        importe=0
        while i < self.__cantidad and not encontrado:
            if self.__movilidades[i].getPatente() == patente:
                encontrado=True
                importe=int(self.__movilidades[i].getImportM())
                print(self.__movilidades[i])
                manejadorG.buscarPatente(patente,importe)
            i+=1
        if not encontrado:
            print('error no se encontro la patente')

    def buscarImporte(self,patente):
        
        i=0
        encontrado=False
        while i < self.__cantidad and not encontrado:
            if self.__movilidades[i].getPatente() == patente:
                print('patente: {}, marca: {}, modeli: {}'.format(self.__movilidades[i].getPatente(),self.__movilidades[i].getMarca(),self.__movilidades[i].getModelo()))
                encontrado=True
                importe=int(self.__movilidades[i].getImportM())
            i=+1

        return importe
            
       
                
        