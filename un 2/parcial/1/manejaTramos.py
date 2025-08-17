#Rodrgo Pastran 39791772 19456
import csv
from tramo import Tramo

class ManejaTramos:
    __tramos=list

    def __init__(self):
        self.__tramos=[]
    
    def cargar(self):
        archivo=open('tramos.csv')
        reader=csv.reader(archivo,delimiter=';')
        salto=True
        for fila in reader:
            if salto:
                salto=False
            else:
                tramo=Tramo(fila[0],fila[1],fila[2],fila[3])
                self.agregar(tramo)
        
        archivo.close

    def mostrar(self):
        for tramo in self.__tramos:
            print(tramo.getOrigen())


    def agregar(self,tramo):
        self.__tramos.append(tramo)

    def mostrarPorPatente(self,patente):
        kmTotal=0
        for tramo in self.__tramos:
            if tramo.getPatente() == patente:
                kmTotal+=int(tramo.getDistancia())
                print('ciudad origen: {} destino: {} km: {}'.format(tramo.getOrigen(),tramo.getDestino(),tramo.getDistancia()))
        print('cantidad de km recorridos: {}'.format(kmTotal))

    def mostrarKmTotal(self,patente,consumo):
        kmTotal=0
        for tramo in self.__tramos:
            if tramo.getPatente() == patente:
                kmTotal+=int(tramo.getDistancia())

        print('total km recorridos: {} y el gasto en combustible: {}'.format(kmTotal,(kmTotal/100)*int(consumo)))

    def listarKm(self,distancia):
        for tramo in self.__tramos:
            if tramo > distancia:
                print('origen: ',tramo.getOrigen(),', destino: ',tramo.getDestino(),', patente: ',tramo.getPatente())
