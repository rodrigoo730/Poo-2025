import csv
from gastosAbril import Gastos

class ManejaGastos:
    __gastos:list

    def __init__(self):
        self.__gastos=[]

    def agregar(self,gasto):
        self.__gastos.append(gasto)

    def cargar(self):
        archivo=open('gastosAbril2025.csv')
        reader=csv.reader(archivo,delimiter=';')
        salto=True
        for fila in reader:
            if salto:
                salto=False
            else:
                gasto=Gastos(fila[0],fila[1],fila[2],fila[3])
                self.agregar(gasto)

    def mostrar(self):
        for gasto in self.__gastos:
            print(gasto)

    def ordenar(self):
        self.__gastos.sort()

    def buscarPatente(self,patente,importe):
        print('fecha            importe          descripcion')
        for gasto in self.__gastos:
            if gasto.getPatente() == patente:
                print('{}         {}         {} '.format(gasto.getFecha(),gasto.getImporte(),gasto.getDescripcion()))
                importe+=int(gasto.getImporte())
        print('total de gasto: {} '.format(importe))

    def buscarFecha(self,fecha,manejaM):
        encontrado=False
        i=0
        importe=0
        while i < len(self.__gastos) and not encontrado:
            if fecha == self.__gastos[i].getFecha():
                print('paso')
                encontrado=True
                patente=self.__gastos[i].getPatente()
                importe=manejaM.buscarImporte(patente)
                importe+=int(self.__gastos[i].getImporte())
            i+=1
        print('gasto total: ',importe)
