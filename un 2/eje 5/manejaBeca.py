import csv
from beca import Beca
from manejaBeneficiario import ManejaBeneficiario
class ManejaBeca:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def cargar(self):
        archivo=open('becas.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                beca=Beca(fila[0],fila[1],fila[2])
                self.__lista.append(beca)

    def mostrar(self):
        i=0
        while i<len(self.__lista):
            print('tipo : {}'.format(self.__lista[i].getTipo()))
            i+=1

    def buscar(self,beca,manejaB):
        i=0
        encontrar=False
        while i<len(self.__lista) and not encontrar:
            if beca == self.__lista[i].getTipo():
                id=i+1
                encontrar=True
                cont=manejaB.mostrarPorBeca(id)
                print('importe total es {}'.format(cont*int(self.__lista[i].getImporte())))
            i+=1
        